"""Shared simplified simulation of MOLLI, ShMOLLI and SASHA, used by several figures.

Simplifications (stated in the book):
- perfect inversion and saturation pulses,
- every single-shot image is replaced by ONE effective pulse of ALPHA_EFF degrees,
- images are taken at the same moment of every heartbeat (t = k * RR),
- no motion, no T2 or off-resonance effects.
"""
import numpy as np
from scipy.optimize import curve_fit

M0 = 1.0
ALPHA_EFF = 35.0     # effective angle of one single-shot image [deg]
SEQUENCES = ["MOLLI", "ShMOLLI", "SASHA"]


def schedule(seq, RR):
    """List of events (time [ms], kind). Kinds: 'inv', 'sat', 'img'."""
    events = []
    if seq in ("MOLLI", "ShMOLLI"):
        # (images after this inversion, rest heartbeats afterwards)
        pattern = [(3, 3), (3, 3), (5, 0)] if seq == "MOLLI" else [(5, 1), (1, 1), (1, 0)]
        beat = 0
        for k, (n_img, n_rest) in enumerate(pattern):
            ti_first = 100 + 80 * k                  # TI of the first image after inversion k
            events.append((beat * RR - ti_first, "inv"))
            for j in range(n_img):
                events.append(((beat + j) * RR, "img"))
            beat += n_img + n_rest
    else:  # SASHA: first image without preparation, then one saturation per heartbeat
        ts_values = np.linspace(100, RR - 150, 9)    # saturation times spread over the beat
        events.append((0.0, "img"))
        for j, ts in enumerate(ts_values, start=1):
            events.append((j * RR - ts, "sat"))
            events.append((j * RR, "img"))
    return sorted(events)


def simulate(seq, T1, RR, dt=5.0):
    """Follow Mz through the sequence. Returns (t_curve, mz_curve, events, samples),
    where samples is a list of (time after last preparation pulse, Mz at the image)."""
    events = schedule(seq, RR)
    ca = np.cos(np.deg2rad(ALPHA_EFF))
    t, mz, last_prep = events[0][0] - 300, M0, None
    t_curve, mz_curve, samples = [t], [mz], []
    for t_ev, kind in events:
        tt = np.arange(t, t_ev, dt)                             # T1 recovery until the event
        t_curve += list(tt)
        mz_curve += list(M0 - (M0 - mz) * np.exp(-(tt - t) / T1))
        mz, t = M0 - (M0 - mz) * np.exp(-(t_ev - t) / T1), t_ev
        t_curve.append(t); mz_curve.append(mz)
        if kind == "inv":
            mz, last_prep = -mz, t                              # perfect inversion
        elif kind == "sat":
            mz, last_prep = 0.0, t                              # perfect saturation
        else:
            eff = t - last_prep if last_prep is not None else np.inf
            samples.append((eff, mz))
            mz = mz * ca                                        # the image costs some Mz
        t_curve.append(t); mz_curve.append(mz)
    tt = np.arange(t, t + 1500, dt)
    t_curve += list(tt)
    mz_curve += list(M0 - (M0 - mz) * np.exp(-(tt - t) / T1))
    return np.array(t_curve), np.array(mz_curve), events, samples


def ll_model(ti, A, B, T1s):
    return A - B * np.exp(-ti / T1s)


def sasha_model(ts, A, eta, T1):
    return A * (1 - eta * np.exp(-ts / T1))


def fit(seq, samples, RR, noise=None):
    """Fit the samples. Returns (model, params, T1 estimate, number of images used).
    `noise` is an optional array added to the Mz values (one value per image)."""
    x = np.array([s[0] for s in samples])
    y = np.array([s[1] for s in samples])
    if noise is not None:
        y = y + noise
    if seq == "SASHA":
        x = np.where(np.isinf(x), 1e5, x)        # first image: fully recovered
        p, _ = curve_fit(sasha_model, x, y, p0=[1, 1, 1000],
                         bounds=([0, 0, 10], [3, 3, 5000]), maxfev=20000)
        return sasha_model, p, p[2], len(x)
    n_used = len(x)
    if seq == "ShMOLLI":
        # Book's simple rule: fit the first 5 images; keep images 6 and 7 only if
        # that T1 is shorter than half an RR interval (enough recovery in between).
        p, _ = curve_fit(ll_model, x[:5], y[:5], p0=[1, 2, 1000],
                         bounds=([0, 0, 10], [3, 6, 5000]), maxfev=20000)
        n_used = 7 if p[2] * (p[1] / p[0] - 1) < RR / 2 else 5
    p, _ = curve_fit(ll_model, x[:n_used], y[:n_used], p0=[1, 2, 1000],
                     bounds=([0, 0, 10], [3, 6, 5000]), maxfev=20000)
    A, B, T1s = p
    return ll_model, p, T1s * (B / A - 1), n_used
