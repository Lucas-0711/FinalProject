---
title: 'What can go wrong'
numbering:
  enumerator: '4.%s'
  heading_2: true
  figure: true
  equation: true
---

The previous section showed that MOLLI, ShMOLLI and SASHA give different T1 values for the
same tissue. This section looks at the three most important reasons: the heart rate, noise,
and magnetization transfer.

## Heart rate

The rest periods of MOLLI are counted in heartbeats, not in milliseconds. At a high heart
rate, three heartbeats are much shorter, so $M_z$ has less time to recover before the next
inversion. The images after that inversion no longer lie on the same curve as the others,
and the fit underestimates T1. This mostly affects tissues with a **long T1**, such as
blood [@barral2018].

Heart rates vary a lot between people. A well-trained athlete can have a resting heart rate
below 50 beats per minute, while a nervous patient in the scanner can easily be above 90.
With MOLLI these two people would get different T1 values even if their hearts were
identical. An irregular heartbeat (arrhythmia), which is common in older people, makes this
worse, because the rest periods then change from one heartbeat to the next [@barral2018].
Blood T1 matters too: it is needed to calculate the ECV, and it can even be used to
estimate the hematocrit without a blood test [@barral2018].

ShMOLLI avoids most of this problem for long T1, because it then only uses the five images
after the first inversion. SASHA is not affected in the same way, since every saturation
pulse sets $M_z$ to zero [@barral2018].

:::{figure} #fig-heart-rate-output
:label: fig-heart-rate
Error of the fitted T1 as a function of heart rate for MOLLI, ShMOLLI and SASHA. The
tissue is chosen with the dropdown menu. Same simplified model as in
{numref}`fig-side-by-side`, without noise.
:::

**Try this** in {numref}`fig-heart-rate`:

- Select blood. The MOLLI error grows from −5.6% at 40 beats per minute to −15.1% at 100.
  At about 74 beats per minute it passes −10%. A patient whose heart rate goes from 60 to
  90 between two scans would see a blood T1 about 6% lower without any change in the tissue.
- Look at ShMOLLI for blood. Its error is about −5 to −6%, but it **hardly changes with
  heart rate**.
- Switch to myocardium after contrast. With T1 = 400 ms the recovery is fast enough at any
  heart rate, and all three lines stay close to zero.
- In the same view, ShMOLLI jumps from −1.4% to −2.6% between 76 and 78 beats per minute.
  This is where it switches from using all 7 images to only the first 5 (see the previous
  section). The exact heart rate of the jump comes from our simplified rule, but the
  switching itself is how ShMOLLI works.

## Noise

Every real image contains some random noise. If we measured the same heart many times, we
would get a slightly different T1 each time. Two questions then matter. Is the result right
**on average**? This is the **accuracy** of a method. And how much do the results
**scatter**? This is its **precision** [@barral2018]. Heart rate, as shown above, mainly
spoils the accuracy of MOLLI. Noise spoils the precision.

SASHA's curve goes from 0 to $M_0$, while the curves of the inversion methods go from
$-M_0$ to $M_0$. SASHA's curve is therefore only half as tall, so the same noise disturbs it
twice as much, and it has a **lower SNR** [@barral2018]. {numref}`fig-precision` repeats each
simulated scan 500 times with random noise and shows all the T1 values as a histogram.

:::{figure} #fig-precision-output
:label: fig-precision
Distribution of the fitted T1 for 500 simulated scans of native myocardium
(T1 = 1000 ms, 60 beats per minute) with random Gaussian noise, one panel per method. The
slider sets the SNR, defined as $M_0$ divided by the standard deviation of the noise, for
all three panels at once. Each panel gives the mean ± standard deviation (SD). The dashed
line marks the true T1.
:::

**Try this** in {numref}`fig-precision`:

- At SNR 40, compare where the middle of each histogram sits (accuracy) and how wide it
  is (precision). MOLLI gives 962 ± 17 ms (mean ± SD): narrow, but its mean is to the left of
  the true value. SASHA gives 1002 ± 70 ms: its mean is on the true value, but the
  histogram is about four times wider. ShMOLLI (947 ± 33 ms) lies in between, because it
  uses fewer images than MOLLI (7 instead of 11).
- Move the slider to SNR 80. All histograms become narrower, but MOLLI and ShMOLLI stay
  shifted. More signal fixes noise, not bias. To be as precise as MOLLI, SASHA would need
  about four times the SNR, which means about 16 times longer averaging.

## Magnetization transfer

Only part of the hydrogen in tissue gives an MRI signal: the hydrogen in water molecules that
move freely. Another part is bound to large molecules such as proteins. Its signal
disappears far too quickly to be measured, so it is invisible. The two parts constantly
exchange magnetization. This is called **magnetization transfer (MT)** [@hafyane2018].

MOLLI and ShMOLLI play many RF pulses during their images. These pulses also hit the
invisible hydrogen and take away some of its magnetization. Through the exchange, the
visible water then loses magnetization as well. For the visible water this acts like
additional readouts: the curve settles lower, the fit sees a faster recovery and **T1 comes
out too low**. More detailed simulations found that MT alone lowers MOLLI's T1 by at least
10%, while SASHA is affected much less [@robson2013; @hafyane2018]. {numref}`fig-mt` shows
the effect in a simple model with a visible and an invisible pool.

:::{figure} #fig-mt-output
:label: fig-mt
Toy model of magnetization transfer for native myocardium (T1 = 1000 ms, 60 beats per
minute). The slider sets the size of the invisible (bound) pool relative to the visible
water. Left: the MOLLI images and their fit with MT (blue), compared to the fit without MT
(gray). Right: the fitted T1 of all three methods as a function of the size of the
invisible pool; the diamonds mark the current slider position and the dashed line the
true T1. Each image saturates 30% of the invisible pool; inversion and saturation pulses
saturate it completely. The numbers only show the trend.
:::

**Try this** in {numref}`fig-mt`:

- Set the slider to 0%. Without MT, MOLLI gives 961 ms, the same as in
  {numref}`fig-side-by-side`.
- Move it to 10% and then 20%. The blue images settle lower than the gray curve, and MOLLI's
  T1 drops to 873 ms and 808 ms. ShMOLLI behaves the same way.
- Look at SASHA on the right: it stays at the true value. Its saturation pulses empty both
  pools before every image anyway, so the fit is not misled.

## Measurements in pig hearts

Simulations can only show what we put into them. To test whether MT really matters, six pig
hearts were measured with MOLLI, ShMOLLI, SASHA and with a slow inversion recovery scan as
the reference [@hafyane2018]. For each heart, the amount of MT and the T2 were measured as
well. After three weeks the hearts were put into formalin, a preservative that changes the
tissue, to see whether the results still hold for different tissue.

:::{figure} #fig-pig-hearts-output
:label: fig-pig-hearts
Average T1 of six ex vivo pig hearts at 3T measured with inversion recovery (reference),
MOLLI, ShMOLLI and SASHA, before and after formalin fixation (dropdown menu). Left: measured
T1, with the reference as a dashed line. Right: difference to the reference. Data from
Table 1 of [@hafyane2018]. Note that this study used a MOLLI scheme with two inversions,
5(3)3, at a simulated heart rate of 60 beats per minute.
:::

In the fresh hearts, MOLLI was 11% and ShMOLLI 17% **below** the reference, and SASHA 4%
**above** it ({numref}`fig-pig-hearts`). How large the error was in each heart depended
only weakly on T2, but strongly on the amount of MT, for all three methods and also after
fixation. So SASHA is not completely free of MT either, even though its error is small and
our toy model shows no effect for it. The conclusion is that **MT is the main reason why
cardiac T1 values are inaccurate** [@hafyane2018]. It also explains why the three methods agree well in phantoms,
which contain little MT, but disagree in real tissue [@hafyane2018; @barral2018].

## Other effects

A few more effects can bias the result. They are not part of our simulation:

- **Inversion efficiency.** The fit assumes a perfect 180° inversion, but even adiabatic
  inversion pulses only reach about 155° in tissue [@barral2018]. For a simple IR fit that
  assumes 180°, this alone makes T1 about 9% too short.
- **T2.** The bSSFP readout of MOLLI and ShMOLLI makes them sensitive to T2 in simulations
  and phantoms, while SASHA is not [@barral2018]. In the pig hearts, however, T2 explained
  much less of the error than MT [@hafyane2018].
- **Off-resonance.** A frequency offset of ±100 Hz can change MOLLI's T1 by about 6%, but
  SASHA's by less than 1% [@barral2018].
- **Partial volume.** Thick slices (8 to 10 mm) mix blood into the thin heart wall, which
  affects all methods [@barral2018].

The last section sums up the three methods.
