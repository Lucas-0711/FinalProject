---
title: 'The gold standard and its hidden assumptions'
numbering:
  enumerator: '2.%s'
  heading_2: true
  figure: true
  equation: true
---

## Inversion recovery

In IR, a 180° pulse flips $M_z$ from $+M_0$ to $-M_0$. After waiting a time TI, an image
is taken. Repeating this for several TI values samples the recovery curve, and fitting an
exponential to these points gives T1 [@barral2018].

If the inversion is perfect (exactly 180°) and TR is long enough for full recovery
(TR much longer than T1), the signal is

```{math}
:label: eq-ir-2p
S(\mathrm{TI}) = c \left(1 - 2\, e^{-\mathrm{TI}/T1}\right)
```

This is a 2-parameter model, with the scaling $c$ and T1 as unknowns. Directly after the
inversion (TI = 0) the signal is $-c$, and for long TI it approaches $+c$.

## Every model is a list of assumptions

{eq}`eq-ir-2p` is the simplest version of a more general model. Each simplification
removes one unknown, but only because we assume something about the scan
[@barral2018]:

| Model | Equation | Extra assumption |
|---|---|---|
| 4-parameter | $S = e^{i\phi}\left(r_a + r_b\, e^{-\mathrm{TI}/T1}\right)$ | Instantaneous pulses, perfect spoiling, no off-resonance |
| 3-parameter | $S = c\left(1 - (1-\cos\theta)\, e^{-\mathrm{TI}/T1}\right)$ | + TR much longer than T1 |
| 2-parameter | $S = c\left(1 - 2\, e^{-\mathrm{TI}/T1}\right)$ | + inversion angle $\theta = 180°$ |

This means that whoever uses a model has to check whether its assumptions hold
[@barral2018]. If the model assumes that TR is much longer than T1, for example, the
measured T1 should actually be much shorter than the TR that was used.

## Is the inversion really 180°?

The 2-parameter model assumes a perfect 180° inversion. In practice, even adiabatic
inversion pulses [@tannus1997] do not reach this, because the effect of the pulse depends
on the T1 and T2 of the tissue. A simulation of such a pulse for muscle at 1.5T
(T1 = 1130 ms, T2 = 35 ms) gives an effective angle of only about 155° [@barral2018].
The correct signal is then

```{math}
:label: eq-ir-155
S(\mathrm{TI}) = c \left(1 - 1.9\, e^{-\mathrm{TI}/T1}\right)
\quad\text{instead of}\quad
S(\mathrm{TI}) = c \left(1 - 2\, e^{-\mathrm{TI}/T1}\right)
```

since $1 - \cos(155°) \approx 1.9$. {numref}`fig-inversion` shows how much this changes
the fitted T1.

:::{figure} #fig-inversion-output
:label: fig-inversion
Effect of an imperfect inversion on the fitted T1. Left: simulated IR signal of muscle
(T1 = 1130 ms) for the inversion angle chosen with the slider, fitted with the
2-parameter model ({eq}`eq-ir-2p`) and the 3-parameter model. Right: error of the
2-parameter fit as a function of the inversion angle for three T1 values. The TI values
are 50, 400, 1100 and 2500 ms, as recommended for gold-standard IR [@barral2018]. The
data are noise-free.
:::

At 180° both fits go through the data points and the error is zero. At 155° the curve
no longer starts at $-c$, and at short TI the points lie above the 2-parameter fit. The
2-parameter model compensates for this with a shorter T1, which **underestimates T1 by
about 9%**. The 3-parameter model fits the angle as an additional unknown and still finds
the correct T1, but one more unknown also needs more data or a higher SNR.

Two more points are important in practice [@barral2018]. First, the edges of a slice get
an even weaker inversion, so the effective angle is an average over the slice profile.
Second, the fit should always be checked visually: plotting the data and the fitted curve
for a few regions shows quickly whether the model describes the data.

## Exercises

:::{exercise}
:label: ex-inversion-5
In {numref}`fig-inversion`, find the inversion angle at which the 2-parameter model
underestimates T1 by about 5%.
:::

:::{solution} ex-inversion-5
:class: dropdown
About 160°. At this angle $1 - \cos(160°) \approx 1.94$, which is only 3% less than 2,
but the fitted T1 is already 5 to 6% too short.
:::

:::{exercise}
:label: ex-inversion-t1
Does the error in {numref}`fig-inversion` (right) depend strongly on T1? What does this
mean for a clinic that compares patients using the 2-parameter model?
:::

:::{solution} ex-inversion-t1
:class: dropdown
Only weakly, the three curves are close together. The bias is therefore roughly a
constant percentage. Patients measured with the same sequence can still be compared
(reproducibility), but the values are not accurate and should not be compared with other
sequences or sites without care.
:::

:::{exercise}
:label: ex-inversion-time
Each point on the recovery curve takes about 6 minutes in the heart. How long would a
gold-standard IR scan with the four TI values from {numref}`fig-inversion` take, and how
many breath-holds of 20 s would that be?
:::

:::{solution} ex-inversion-time
:class: dropdown
$4 \times 6 = 24$ minutes, which corresponds to $24 \times 60 / 20 = 72$ breath-holds.
This is why the heart needs faster methods.
:::

The next section introduces the Look-Locker method, which measures the whole recovery
curve after a single inversion.
