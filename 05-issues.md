---
title: 'What can go wrong: issues and limitations'
numbering:
  enumerator: '5.%s'
  heading_2: true
  figure: true
  equation: true
---

## Heart rate

The rest periods of MOLLI are counted in heartbeats, not in milliseconds. At a high heart
rate, three heartbeats are much shorter than at a low heart rate, so $M_z$ has less time to
recover before the next inversion. The next inversion then starts from a smaller $M_z$,
the images after it no longer lie on the same curve as the others, and the fit
underestimates T1. This mostly affects tissues with a **long T1**, such as blood, which
need more time to recover [@barral2018]. The effect can be reduced by using a single
inversion or more rest heartbeats [@barral2018].

Heart rates vary a lot between people. A well-trained athlete can have a resting heart
rate below 50 beats per minute, while a nervous patient in the scanner can easily be
above 90. With MOLLI these two people would get different T1 values even if their hearts
were identical. The problem is even larger with an irregular heartbeat (arrhythmia),
which is common in older people, because then the rest periods change from one
heartbeat to the next [@barral2018].

Blood T1 is not only a by-product of the scan. It is needed to calculate the ECV (see
[](./06-summary.md)), and it can even be used to estimate the hematocrit without a blood
test [@barral2018]. A wrong blood T1 therefore affects more than one number.

ShMOLLI avoids most of this problem for long T1 because it then only uses the five images
after the first inversion [@barral2018]. SASHA is not affected in the same way, since every
saturation pulse sets $M_z$ to zero regardless of the previous heartbeat. Its weak point
is a different one: each SASHA image is acquired over a long window of about 175 ms,
which costs spatial resolution [@barral2018]. {numref}`fig-heart-rate` shows the effect
of the heart rate in our simulation.

:::{figure} #fig-heart-rate-output
:label: fig-heart-rate
Error of the fitted T1 as a function of heart rate for MOLLI, ShMOLLI and SASHA. The
tissue is chosen with the dropdown menu. Same simplified model as in
{numref}`fig-sampling`, without noise.
:::

For blood (T1 = 1600 ms), the MOLLI error grows from −5.6% at 40 beats per minute to
−15.1% at 100 beats per minute. For native myocardium the effect is smaller (from −3.6%
to −5.9%), and after contrast it practically disappears, because a T1 of 400 ms recovers
fully even during short rest periods. ShMOLLI has an error of about −5 to −6% for blood,
but this error **hardly changes with heart rate**. In our model SASHA is exact at every
heart rate. Real SASHA measurements are not perfect either, but their errors come from
other sources, which are listed at the end of this page.

## Noise

Heart rate mainly affects the **accuracy** of a method, meaning how close the result is to
the true T1 on average. Noise affects its **precision**, meaning how much repeated
measurements of the same tissue scatter. A constant error can be acceptable as long as
the method is reproducible, but poor precision makes it hard to detect small differences
between healthy and diseased tissue [@barral2018].

SASHA starts from zero after each saturation pulse, while the inversion methods start
from $-M_0$. The recovery curve of SASHA therefore covers only half the signal range, which
gives it a **lower SNR** [@barral2018]. MOLLI also uses more images (11) than ShMOLLI (7).
To see what this means, {numref}`fig-precision` repeats each simulated scan 500 times
with random noise and shows how the fitted T1 values are distributed.

:::{figure} #fig-precision-output
:label: fig-precision
Distribution of the fitted T1 for 500 simulated scans of native myocardium
(T1 = 1000 ms, 60 beats per minute) with random Gaussian noise. The slider sets the SNR,
defined as $M_0$ divided by the standard deviation of the noise. The legend gives the mean
and the standard deviation (SD) of each method. The dashed line marks the true T1.
:::

At an SNR of 40, MOLLI gives 962 ± 17 ms (mean ± SD), ShMOLLI 947 ± 33 ms and SASHA
1002 ± 70 ms. MOLLI is therefore the most precise method but underestimates T1, while
SASHA is correct on average but its values scatter about four times more. ShMOLLI lies
in between, since it uses fewer images than MOLLI. Doubling the SNR halves the SD of all
three methods, but it does not change the bias of MOLLI and ShMOLLI.

## Other sources of error

Several important effects are not part of our simple simulation. The table summarizes
how they affect the methods [@barral2018]:

| Factor | MOLLI / ShMOLLI | SASHA |
|---|---|---|
| T2 | Sensitive, because of the bSSFP readout and the imperfect inversion | Not sensitive |
| Heart rate | Underestimation for long T1 at high heart rates ({numref}`fig-heart-rate`) | Not sensitive, but the long acquisition window (about 175 ms) reduces resolution |
| SNR | Higher | Lower, because the curve starts at zero; fitting magnitude instead of complex data adds a bias |
| Off-resonance | Significant, worse at higher field and larger flip angles: ±100 Hz can cause about 6% error | Negligible: ±100 Hz causes less than 1% error |
| Flip angle | T1 is underestimated for larger flip angles | A larger flip angle increases the SNR, up to the SAR limit |
| Inversion or saturation efficiency | Assumes a perfect inversion, which causes a significant bias (see [](./02-gold-standard.md)); adiabatic pulses help | The saturation profile over the slice is not perfect and depends on T1 and T2 |
| Fitting model | Magnitude data are a problem when an image is close to the zero crossing, because its SNR is low | The 2-parameter model is biased; the 3-parameter model avoids this |
| Inflow (blood T1) | More sensitive, because blood flows in during the long sampling after the inversion | Less sensitive, because it samples before fresh blood has flowed in |
| Partial volume | Both: thick slices (8 to 10 mm) and small matrices mix blood into the myocardium | |
| Magnetization transfer | The inversion pulses cause MT, which lowers T1 | Not affected |

Because of these effects, the methods agree well in phantoms but not in patients. In a
phantom study, MOLLI, ShMOLLI and SASHA all matched the spin-echo reference closely, while
in the myocardium of a healthy subject at 3T MOLLI and ShMOLLI gave about 1200 ms and
SASHA about 1500 ms [@barral2018; @teixeira2016]. The main reasons are effects that are
much weaker in phantoms, such as magnetization transfer, B1 inhomogeneity and imperfect
spoiling [@barral2018].

## Exercises

:::{exercise}
:label: ex-hr-molli
In {numref}`fig-heart-rate` (blood), at which heart rate does the MOLLI error exceed
−10%? What would that mean for a patient whose heart rate changed from 60 to 90 beats per
minute between two scans?
:::

:::{solution} ex-hr-molli
:class: dropdown
At about 74 beats per minute. Between 60 and 90 beats per minute the error changes from
about −7.7% to −13.1%, so the measured blood T1 would drop by about 6% even though the
tissue did not change.
:::

:::{exercise}
:label: ex-snr-sasha
In {numref}`fig-precision`, MOLLI has an SD of about 17 ms at an SNR of 40. Roughly which
SNR would SASHA need for the same SD? Since the SNR grows with the square root of the
number of averages, how much longer would the scan take?
:::

:::{solution} ex-snr-sasha
:class: dropdown
SASHA has an SD of about 34 ms at SNR 80. Because the SD is inversely proportional to the
SNR, it needs about SNR 160, which is four times the SNR of MOLLI. This requires
$4^2 = 16$ times more averaging, so about 16 times the scan time.
:::

The last page summarizes the three methods and gives some recommendations for using
cardiac T1 maps in practice.
