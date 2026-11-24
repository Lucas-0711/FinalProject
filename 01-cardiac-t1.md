---
title: Cardiac T1 Mapping
numbering:
  heading_2: true
  figure: true
  equation: true
---

## Why measure T1 in the heart?

### Recap on T1

After an RF pulse tips the magnetization away from equilibrium, the longitudinal
magnetization $M_z$ grows back towards its equilibrium value $M_0$. This regrowth is
exponential, and its time constant is called **T1** [@barral2018]. A tissue with a short
T1 recovers quickly; a tissue with a long T1 recovers slowly.

**What this means for the image.** In a *T1-weighted image*, the next RF pulse comes
before every tissue has fully recovered (short TR). A tissue with a **short T1** has
regrown more of its $M_z$ by then, so it gives more signal and looks **brighter**. A
tissue with a **long T1** has regrown less, so it looks **darker**. Fat, for example, has
a short T1 and appears bright, while fluids have a long T1 and appear dark. A gadolinium
contrast agent shortens T1, which is why tissue that takes up contrast lights up — in the
heart, this makes scarred (infarcted) tissue bright [@barral2018].

A T1-weighted image only tells you that one tissue is brighter or darker than another,
in arbitrary units. A *T1 map* instead gives every pixel a number in milliseconds, so
values can be compared between patients, scanners and visits [@barral2018].

### What T1 tells us about the heart

About 75% of the heart's volume is made of muscle cells (myocytes). The remaining 25% is
the extracellular space: fibroblasts, collagen, other proteins and blood vessels
[@barral2018]. Diseases change this mix. For example, scarring adds collagen and
inflammation adds water, and both change T1.

Cardiac T1 mapping is used in two ways [@barral2018]:

- **Native T1** (no contrast agent). It can help separate healthy myocardium from acute
  injury with edema and from scarring. It is the method of choice when a contrast agent
  is too risky, for example in patients with chronic kidney disease.
- **ECV.** A gadolinium contrast agent shortens T1 and stays outside the cells. Comparing
  T1 before and after contrast gives the fraction of tissue that is extracellular space,
  which is a marker of fibrosis.

### Why the heart is difficult

The heart beats, and the patient breathes. To get sharp images, the scan is
**triggered by the ECG** (images are taken at the same moment of every heartbeat), and
the whole measurement must fit into **one breath-hold of less than about 20 s**
[@barral2018].

The gold-standard method used in the brain (next section) is far too slow for this:
with a typical cardiac image size, each point on the recovery curve takes about
**6 minutes** to acquire [@barral2018]. Cardiac methods therefore trade some accuracy for
speed. The rest of this book is about that trade-off.

## The gold standard and its hidden assumptions

### Inversion recovery

In **IR**, a 180° pulse flips $M_z$ from $+M_0$ to $-M_0$. We then wait a time TI and
take an image. Repeating this for several TI values samples the recovery curve, and
fitting an exponential to those points gives T1 [@barral2018].

If the inversion is perfect (exactly 180°) and TR is long enough for full recovery
(TR much longer than T1), the signal is

```{math}
:label: eq-ir-2p
S(\mathrm{TI}) = c \left(1 - 2\, e^{-\mathrm{TI}/T1}\right)
```

This is a **2-parameter model**: the unknowns are the scaling $c$ and T1. Right after the
inversion (TI = 0) the signal is $-c$ (fully inverted), and for long TI it approaches
$+c$ (fully recovered).

### Every model is a list of assumptions

{eq}`eq-ir-2p` is the simplest version of a more general model. Each simplification
removes an unknown, but only by assuming something about the scan [@barral2018]:

| Model | Equation | Extra assumption |
|---|---|---|
| 4-parameter | $S = e^{i\phi}\left(r_a + r_b\, e^{-\mathrm{TI}/T1}\right)$ | Instantaneous pulses, perfect spoiling, no off-resonance |
| 3-parameter | $S = c\left(1 - (1-\cos\theta)\, e^{-\mathrm{TI}/T1}\right)$ | + TR much longer than T1 |
| 2-parameter | $S = c\left(1 - 2\, e^{-\mathrm{TI}/T1}\right)$ | + inversion angle $\theta = 180°$ |

So whenever you use a model, you have to check that its assumptions really hold
[@barral2018]. For example, if the model assumes that TR is much longer than T1, check
that the T1 you measured is indeed much shorter than your TR.

### Is the inversion really 180°?

The 2-parameter model assumes a perfect 180° inversion. In practice, even special
*adiabatic* inversion pulses [@tannus1997] do not achieve this, because the pulse's
effect depends on the tissue's own T1 and T2. A simulation of such a pulse for muscle at
1.5T (T1 = 1130 ms, T2 = 35 ms) gives an effective angle of only about **155°**
[@barral2018]. The correct signal is then

```{math}
:label: eq-ir-155
S(\mathrm{TI}) = c \left(1 - 1.9\, e^{-\mathrm{TI}/T1}\right)
\quad\text{instead of}\quad
S(\mathrm{TI}) = c \left(1 - 2\, e^{-\mathrm{TI}/T1}\right)
```

because $1 - \cos(155°) \approx 1.9$. That looks like a small change. {numref}`fig-inversion`
shows what it does to the T1 value.

:::{figure} #fig-inversion-output
:label: fig-inversion
**Effect of an imperfect inversion.** *Left:* simulated IR data (dots) for muscle
(T1 = 1130 ms) with the actual inversion angle set by the slider. The dashed lines are
fits with the 2-parameter model ({eq}`eq-ir-2p`, assumes 180°) and the 3-parameter model
(angle is fitted). *Right:* error of the fitted T1 when the 2-parameter model is used, for
three example T1 values. The marker shows the current slider position. The four TI
values are 50, 400, 1100 and 2500 ms, a recommended set for gold-standard IR
[@barral2018]. Data are noise-free and polarity-restored (signed) to isolate the bias.
:::

**How to read the figure:**

1. Start at 180°. Both fits go through the dots and the error is 0%.
2. Move the slider to 155°. The curve no longer starts at $-c$: the dots lie *above* the
   2-parameter fit at short TI. The 2-parameter model "explains" this by choosing a
   **shorter T1**, so it underestimates T1 by about 9%.
3. The 3-parameter model fits the angle as an extra unknown, so its T1 stays correct.
   The price is one more unknown, which needs more data or more SNR.

Two more practical points [@barral2018]:

- The edges of a real slice see an even weaker inversion, so the effective angle is an
  average over the slice profile.
- Always **look at the fit**: plot the data points and the fitted curve for a few regions
  and check that the curve passes through the points.

### Exercises

:::{exercise}
:label: ex-inversion-5
In {numref}`fig-inversion`, find the inversion angle at which the 2-parameter model
underestimates T1 by about 5%.
:::

:::{solution} ex-inversion-5
:class: dropdown
About 160°. At this angle $1 - \cos(160°) \approx 1.94$, only 3% less than 2, but the
fitted T1 is already about 5–6% too short.
:::

:::{exercise}
:label: ex-inversion-t1
Does the error in {numref}`fig-inversion` (right) depend strongly on the tissue's T1?
What does that mean for a clinic that compares patients using the 2-parameter model?
:::

:::{solution} ex-inversion-t1
:class: dropdown
Only weakly: all three curves lie close together. So the bias is mostly a constant
percentage. Patients scanned with the *same* sequence can still be compared
(reproducibility), but the values are not *accurate* and should not be compared with
another sequence or site without care.
:::

:::{exercise}
:label: ex-inversion-time
Each point on the recovery curve takes about 6 minutes in the heart. How long would a
gold-standard IR scan with the four TI values from {numref}`fig-inversion` take? How many
breath-holds of 20 s is that?
:::

:::{solution} ex-inversion-time
:class: dropdown
$4 \times 6 = 24$ minutes, which is $24 \times 60 / 20 = 72$ breath-holds. This is why
the heart needs faster methods.
:::
