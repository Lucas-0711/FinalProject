---
title: 'MOLLI, ShMOLLI and SASHA'
numbering:
  enumerator: '4.%s'
  heading_2: true
  figure: true
  equation: true
---

## Why plain Look-Locker does not work in the heart

The Look-Locker method from the previous section takes a readout every few milliseconds.
In the heart, these readouts would be spread over the whole cardiac cycle, so every
point would show the heart in a different position. Instead, cardiac methods take **one
complete image per heartbeat**, always at the same moment of the cycle (in diastole, when
the heart moves least). Each image is a single-shot image: the whole image is acquired
in one short window of a single heartbeat [@barral2018].

This changes how the recovery curve is sampled. With one image per heartbeat, the
points on the curve are about one RR interval apart, which is roughly 1 s at a heart rate
of 60 beats per minute. All three methods below solve this problem in a different way.

## MOLLI

MOLLI uses several inversions within one breath-hold [@messroghli2004; @barral2018].
After each inversion, a few images are taken in consecutive heartbeats. Then the sequence
waits a few heartbeats without imaging so that $M_z$ can recover before the next
inversion. The first version is called 3(3)3(3)5 [@barral2018]:

- 3 images after the first inversion, then 3 heartbeats of rest,
- 3 images after the second inversion, then 3 heartbeats of rest,
- 5 images after the third inversion.

This adds up to 11 images in 17 heartbeats. The trick is that the inversions are timed
so that the first image after each inversion has a slightly different TI (in our
simulation 100, 180 and 260 ms). When all 11 images are sorted by their TI, they fill
the recovery curve much more densely than one image per second would.

The curve is then fitted with the Look-Locker model {eq}`eq-ll-signal` and corrected with
{eq}`eq-ll-correction`. MOLLI uses a bSSFP readout, for which {eq}`eq-ll-t1star` is no
longer valid, so the correction with $A$ and $B$ is the one used in practice. Strictly
speaking it is an empirical correction for MOLLI [@barral2018].

## ShMOLLI

ShMOLLI ("shortened MOLLI") needs only 9 heartbeats, which makes the breath-hold shorter
[@piechnik2010; @barral2018]. Its scheme is 5(1)1(1)1: five images after the first
inversion, one heartbeat of rest, one image after the second inversion, one heartbeat of
rest and one image after the third inversion.

The shorter breath-hold is especially useful for patients who are short of breath, for
example because of heart failure, and cannot hold their breath for 17 heartbeats.

One heartbeat of rest is not enough for full recovery if T1 is long. The last two images
are therefore only used when T1 is short enough for $M_z$ to recover almost completely
in between. For longer T1, only the first five images are fitted [@barral2018]. In our
simulation we use a simple version of this rule: the last two images are only used if the
T1 from the first five images is shorter than half an RR interval. The real ShMOLLI
decides this in a more refined way [@piechnik2010].

## SASHA

SASHA uses saturation instead of inversion [@chow2014; @barral2018]. A saturation pulse
sets **$M_z$ to zero, no matter what it was before**. Because this erases the history of the
magnetization, there is no need to wait for recovery between images, and SASHA can take
one image in every heartbeat. It uses ten heartbeats:

- The first image is taken without any preparation pulse, so it shows the fully
  recovered magnetization.
- Before each of the other nine images, a saturation pulse is played. Its position within
  the heartbeat changes from beat to beat, so each image has a different saturation
  time TS. In the original version these times are spread over the whole cardiac cycle
  [@barral2018].

The signal after saturation is

```{math}
:label: eq-sasha
S(\mathrm{TS}) = A \left(1 - \eta\, e^{-\mathrm{TS}/T1}\right)
```

where $\eta$ is the saturation efficiency ($\eta = 1$ for a perfect saturation). With
$\eta$ fitted as a third parameter this is a 3-parameter model. Assuming perfect
saturation ($\eta = 1$) gives a 2-parameter model, which is less accurate
[@barral2018]. Since the curve starts at zero instead of $-M_0$, SASHA has only half the
dynamic range of the inversion methods, which makes it more sensitive to noise. This is
one of the issues discussed in the next section.

## Comparing the three methods

{numref}`fig-sampling` simulates all three methods at 60 beats per minute for native
myocardium, blood and myocardium after contrast.

:::{figure} #fig-sampling-output
:label: fig-sampling
Simulated MOLLI, ShMOLLI and SASHA acquisitions at 60 beats per minute, chosen with the
dropdown menu. Top: $M_z$ during the scan with the heartbeats, the preparation pulses
(inversion or saturation) and the images. Bottom: the same images sorted by their time
after the last preparation pulse, with the fitted curve. Orange images are not used in
the fit. For SASHA, the first image without saturation is drawn at the right edge. Simplified model: perfect inversion and
saturation, no noise, and each image treated as a single pulse of 35°.
:::

For MOLLI with myocardium, the top plot shows the three inversions and the rest
heartbeats in between. Each inversion only gives three or five points, but in the bottom
plot the 11 images together form one smooth curve. Switching to ShMOLLI shows the five
images after the first inversion, followed by two short inversions. For SASHA there are
no rest heartbeats at all, and every image starts again from zero after its saturation
pulse.

The fitted values also differ. In this simulation, MOLLI gives about 961 ms instead of
1000 ms for native myocardium, and about 1477 ms instead of 1600 ms for blood. The
underestimation is larger for blood because three rest heartbeats are not enough for full
recovery when T1 is long. After contrast (T1 = 400 ms) recovery is fast and MOLLI is
almost exact (399 ms). SASHA finds the correct value in all three cases, because the
saturation erases everything that happened before. These differences are the topic of the next section.

:::{note} About the simulation
Real MOLLI and ShMOLLI images are acquired with many bSSFP pulses, which also depend on
T2 and off-resonance. Here every image is replaced by one effective pulse, so the exact
numbers should not be compared with measurements. The simulation only shows the timing
and the trends.
:::

## Exercises

:::{exercise}
:label: ex-molli-sorted
In {numref}`fig-sampling` (MOLLI, myocardium), what is the TI of the second image after
the first inversion? Why is this image not taken at 200 ms?
:::

:::{solution} ex-molli-sorted
:class: dropdown
1100 ms. The images are triggered by the ECG, so the second image comes one heartbeat
(1000 ms) after the first one at 100 ms.
:::

:::{exercise}
:label: ex-shmolli-blood
Select ShMOLLI with blood and then with myocardium after contrast in
{numref}`fig-sampling`. Why are the last two images only used in the second case?
:::

:::{solution} ex-shmolli-blood
:class: dropdown
The last two images come after only one heartbeat of rest. With T1 = 1600 ms, $M_z$
cannot recover in this time, so these images do not lie on the same curve as the first
five and would bias the fit. With T1 = 400 ms the recovery is almost complete, and the
two extra images add information.
:::

