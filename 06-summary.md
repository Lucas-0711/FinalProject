---
title: Summary and recommendations
numbering:
  enumerator: '6.%s'
  heading_2: true
  figure: true
  equation: true
---

## The three methods side by side

All three cardiac methods are based on the same idea as Look-Locker: they collect the
recovery curve within one breath-hold, with one image per heartbeat. They differ in how
they prepare the magnetization and which images they use. The table summarizes the
previous pages.

| | MOLLI | ShMOLLI | SASHA |
|---|---|---|---|
| Preparation | 3 inversions | 3 inversions | saturation before each image |
| Scheme | 3(3)3(3)5 | 5(1)1(1)1 | 1 + 9 saturated images |
| Heartbeats | 17 | 9 | 10 |
| Images in the fit | 11 | 5 (long T1) or 7 (short T1) | 10 |
| Accuracy | underestimates T1 | underestimates T1 | close to the true T1 |
| Precision | highest | medium | lowest |
| Heart rate | sensitive for long T1 | mostly insensitive | insensitive |
| Main other issues | T2, off-resonance, MT, inversion efficiency | same as MOLLI | low SNR, long acquisition window, saturation profile |

No method is best in every respect. **MOLLI is precise but biased**, which is fine for
comparing patients measured with the same protocol. **SASHA is more accurate but
noisier**, so it needs a higher SNR to detect small differences. ShMOLLI trades some
precision for a shorter breath-hold.

## From T1 to ECV

T1 itself depends on the sequence, the scanner and many other factors. A quantity that
is closer to the tissue biology is the ECV. Gadolinium stays in the extracellular space,
so the change of T1 after contrast is related to how much extracellular space there is.
With T1 measured in myocardium and blood before (pre) and after (post) contrast, the ECV
is [@barral2018]

```{math}
:label: eq-ecv
\mathrm{ECV} = (1 - \mathrm{Hct})\,
\frac{\dfrac{1}{T1_\text{myo,post}} - \dfrac{1}{T1_\text{myo,pre}}}
     {\dfrac{1}{T1_\text{blood,post}} - \dfrac{1}{T1_\text{blood,pre}}}
```

where Hct is the hematocrit, the fraction of the blood volume taken up by red blood
cells. It is needed because gadolinium stays in the plasma and does not enter red blood
cells [@barral2018]. The ECV still depends on the sequence, but it is **more robust than
the post-contrast T1** alone and has shown prognostic value [@barral2018].


## Exercise

:::{exercise}
:label: ex-ecv
a) Calculate the ECV for myocardium with T1 = 1000 ms before and 450 ms after contrast,
blood with T1 = 1600 ms before and 300 ms after contrast, and a hematocrit of 0.42.

b) The same patient is measured with MOLLI at 90 beats per minute. In our simulation
({numref}`fig-heart-rate`) this gives 948 ms and 448 ms for the myocardium and 1390 ms
and 302 ms for the blood. Calculate the ECV again. What do you notice?
:::

:::{solution} ex-ecv
:class: dropdown
a) $\mathrm{ECV} = 0.58 \times \frac{1/450 - 1/1000}{1/300 - 1/1600}
= 0.58 \times \frac{0.00122}{0.00271} \approx 0.26$, so about 26% of the myocardium is
extracellular space.

b) $\mathrm{ECV} = 0.58 \times \frac{1/448 - 1/948}{1/302 - 1/1390} \approx 0.26$ again
(26.3% instead of 26.2%). Blood T1 is 13% too low, but the myocardium is also
underestimated, and in the ratio most of the error cancels. This is one reason why the
ECV is **more robust than the T1 values** it is calculated from.
:::

