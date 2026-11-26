---
title: 'MOLLI, ShMOLLI and SASHA side by side'
numbering:
  enumerator: '3.%s'
  heading_2: true
  figure: true
  equation: true
---

## One image per heartbeat

Plain Look-Locker takes a readout every few milliseconds. In the heart, these readouts would
be spread over the whole cardiac cycle, so every point would show the heart in a different
position. Cardiac methods therefore take **one complete image per heartbeat**, always at the
same moment of the cycle (in diastole, when the heart moves least). Each image is a
single-shot image, acquired in one short window of a single heartbeat [@barral2018].

An image is **not** another inversion. It is a short burst of many RF pulses, packed into a
short window of one heartbeat (a bSSFP readout) [@barral2018]. Like the Look-Locker
readouts from the previous section, this burst takes away some $M_z$.

The price of one image per heartbeat is that the points on the recovery curve are now
about one RR interval apart, roughly 1 s at 60 beats per minute. One inversion therefore
only gives a few points. MOLLI, ShMOLLI and SASHA solve this problem in three different
ways. {numref}`fig-side-by-side` shows all three at once, and the sections below explain
what you see in each row.

:::{figure} #fig-side-by-side-output
:label: fig-side-by-side
Simulated MOLLI (top), ShMOLLI (middle) and SASHA (bottom) at 60 beats per minute. The
tissue is chosen with the dropdown menu. Left: $M_z$ during the scan with the heartbeats,
the preparation pulses (inversion or saturation) and the images, on the same time axis for
all three methods. The diamonds give $M_z$ just before each inversion; the dashed line
marks full recovery. Right: the same images sorted by their time after the last preparation
pulse, with the fitted curve and the resulting T1. Both panels of a row use the same
y-axis, and each image has the same colour on both sides: the colour shows after which
inversion (or saturation) it was taken. Hollow images are not used in the fit. Hovering
over an image shows its number, its TI or TS and its $M_z$.
For SASHA, the first image without saturation is drawn at the right edge. Simplified model:
perfect inversion and saturation, no noise, and each image treated as a single pulse of
35°.
:::

## MOLLI

MOLLI uses several inversions within one breath-hold [@messroghli2004; @barral2018]. After
each inversion, a few images are taken in consecutive heartbeats. Then the sequence waits a
few heartbeats without imaging so that $M_z$ can recover before the next inversion. The
original scheme is called 3(3)3(3)5 [@barral2018]: 3 images after the first inversion,
3 heartbeats of rest, 3 images after the second inversion, 3 heartbeats of rest, and
5 images after the third inversion. That is 11 images in 17 heartbeats.

The inversions are timed so that the first image after each inversion has a slightly
different TI (in our simulation 100, 180 and 260 ms). When all 11 images are sorted by
their TI, they fill the recovery curve much more densely than one image per second would.
The curve is fitted with the Look-Locker model and corrected with the $B/A$ correction from
the [previous section](#ll-correction). Since MOLLI uses a bSSFP readout, this
correction is an empirical one [@barral2018].

## ShMOLLI

ShMOLLI ("shortened MOLLI") needs only 9 heartbeats [@piechnik2010; @barral2018]. Its
scheme is 5(1)1(1)1: five images after the first inversion, then only one heartbeat of rest
before each of the two following inversions, which give one image each. The shorter
breath-hold helps patients who are short of breath, for example because of heart failure,
and cannot hold their breath for 17 heartbeats.

Images 1 to 5 all come after the first inversion, which starts from a fully recovered
$M_z$. After that there is only one heartbeat of rest before the next inversion. For a
**long T1**, $M_z$ has not recovered by then: for blood it is only at 0.88 before the
second inversion and 0.48 before the third. Images 6 and 7 would then lie on a lower curve
and pull T1 down, so they are **dropped** [@barral2018]. For a **short T1**, $M_z$ is back
to almost 1, and the two images add points at TI = 180 and 260 ms, exactly where a fast
curve still changes. Without them, only one of the five points (at 100 ms) lies in the
steep part of a curve with T1 = 400 ms. In a simulation with noise (SNR 40), adding them
makes the result **more than twice as precise**: 398 ± 9 ms instead of 388 ± 21 ms. Our
simulation uses a simple version of this rule (images 6 and 7 only if T1 is shorter than
half an RR interval), while the real ShMOLLI decides in a more refined way
[@piechnik2010].

## SASHA

SASHA uses saturation instead of inversion [@chow2014; @barral2018]. A saturation pulse sets
**$M_z$ to zero, no matter what it was before**. This erases the history of the
magnetization, so there is no need to wait for recovery, and SASHA takes one image in every
heartbeat, ten in total. The first image has no preparation pulse and shows the fully
recovered magnetization. Before each of the other nine images, a saturation pulse is played
at a different time, so each image has a different saturation time TS [@barral2018]. The
signal is

```{math}
:label: eq-sasha
S(\mathrm{TS}) = A \left(1 - \eta\, e^{-\mathrm{TS}/T1}\right)
```

where $\eta$ is the saturation efficiency, which is fitted as a third parameter. Since the
curve starts at zero instead of $-M_0$, SASHA covers only half the signal range of the
inversion methods, which makes it more sensitive to noise [@barral2018].

## Comparing them

**Try this** in {numref}`fig-side-by-side`:

- Start with native myocardium and compare the length of the three rows. MOLLI needs about
  17 s, ShMOLLI and SASHA about 9 to 10 s.
- In the MOLLI row, follow the gray $M_z$ curve. After each inversion it is pushed down and
  then climbs back during the rest heartbeats. In the right panel, the 11 images from three
  different inversions (red, green, purple) line up on one curve. Follow the colours to
  see how the groups interleave: each inversion fills different gaps.
- Switch to **blood** (T1 = 1600 ms). Recovery is slower now. Look at the diamonds: in the
  MOLLI row $M_z$ only reaches 0.95 before the second inversion (0.99 for myocardium), and
  MOLLI gives 1477 ms instead of 1600 ms (−7.7%). In the ShMOLLI row the diamonds show
  0.88 and 0.48, and the last two images (green and purple) are hollow because they are not used.
- Look at the SASHA row. Every image starts again from zero after its saturation pulse, so
  nothing from the previous heartbeat matters, and the fit finds the true T1.
- Switch to **myocardium after contrast** (T1 = 400 ms). All diamonds are close to 1, so
  every inversion starts from full recovery, and all three methods are almost exact. In
  the ShMOLLI row images 6 and 7 are filled again and fill the steep early part of the
  curve. It is the **short T1** that helps here, not the contrast agent itself.

The table summarizes how the three methods work.

| | MOLLI | ShMOLLI | SASHA |
|---|---|---|---|
| Preparation | 3 inversions | 3 inversions | saturation before each image |
| Scheme | 3(3)3(3)5 | 5(1)1(1)1 | 1 + 9 saturated images |
| Heartbeats | 17 | 9 | 10 |
| Images in the fit | 11 | 5 (long T1) or 7 (short T1) | 10 |

:::{note} About the simulation
Real MOLLI and ShMOLLI images are acquired with many bSSFP pulses, which also depend on T2,
off-resonance and magnetization transfer. Here every image is replaced by one effective
pulse, so the exact numbers should not be compared with measurements. The simulation only
shows the timing and the trends.
:::

The next section looks at what makes these methods differ in practice: heart rate, noise and
magnetization transfer.
