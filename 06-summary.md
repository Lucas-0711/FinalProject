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

## Good practice

Some recommendations for using cardiac T1 maps [@barral2018; @moon2013]:

- **Know the assumptions of your model** and check them, as shown for the inversion angle
  in [](./02-gold-standard.md).
- **Validate new methods in a phantom first**, for example the T1MES phantom or the NIST
  phantom, and control the temperature, because T1 depends on it. Keep in mind that
  agreement in a phantom does not guarantee agreement in patients.
- **Use the same sequence and protocol** for follow-up scans and for comparing patients.
  Values from different methods cannot be compared directly.
- **Analyze regions carefully.** T1 values are usually averaged over regions of the
  myocardium, often using the 17-segment model of the American Heart Association. Segments
  with artifacts should be excluded, and partial volume with blood or fat should be
  avoided. If the heart moved between images, the images should be registered before the
  fit.
- **Follow the consensus statement** of the SCMR and the European Society of Cardiology,
  which gives recommendations on terminology, acquisition, quality control and analysis
  [@moon2013].

## Exercises

:::{exercise}
:label: ex-ecv
Calculate the ECV for myocardium with T1 = 1000 ms before and 450 ms after contrast,
blood with T1 = 1600 ms before and 300 ms after contrast, and a hematocrit of 0.42.
:::

:::{solution} ex-ecv
:class: dropdown
$\mathrm{ECV} = 0.58 \times \frac{1/450 - 1/1000}{1/300 - 1/1600}
= 0.58 \times \frac{0.00122}{0.00271} \approx 0.26$, so about 26% of the myocardium is
extracellular space.
:::

:::{exercise}
:label: ex-choose
A hospital wants to measure native T1 in patients with irregular and fast heart rates and
wants to compare the values with published normal values from another hospital. Which
method would you suggest, and what should they keep in mind?
:::

:::{solution} ex-choose
:class: dropdown
SASHA or ShMOLLI, because they are less sensitive to heart rate than MOLLI
({numref}`fig-heart-rate`). SASHA is also closer to the true T1, but its lower precision
({numref}`fig-precision`) has to be compensated with a higher SNR. In any case, normal
values from another hospital are only useful if they were measured with the same
sequence and protocol, ideally checked with a phantom at both sites.
:::

:::{exercise}
:label: ex-why-not-gold
After reading this book, explain in two or three sentences why cardiac T1 mapping does
not simply use the gold-standard inversion recovery from [](./02-gold-standard.md).
:::

:::{solution} ex-why-not-gold
:class: dropdown
Gold-standard IR needs one inversion per point and a long recovery after each, which
takes about 6 minutes per point in the heart ([](#ex-inversion-time)). The heart moves,
so the whole measurement has to fit into one breath-hold of about 20 s with one image per
heartbeat. This is only possible with Look-Locker-type methods, which are faster but less
accurate.
:::
