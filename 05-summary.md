---
title: Summary
numbering:
  enumerator: '5.%s'
  heading_2: true
  figure: true
  equation: true
---

## Key points

- Inversion recovery is too slow for the heart. All cardiac methods are based
  on the **Look-Locker** idea: one preparation, many readouts, and a corrected T1\*
  ([](./02-look-locker.md)).
- Because the heart moves, they take **one image per heartbeat**. MOLLI and ShMOLLI use
  several inversions with rest heartbeats in between, SASHA uses a saturation pulse before
  every image ([](./03-molli-shmolli-sasha.md)).
- **MOLLI is precise but underestimates T1**, especially for long T1 at high heart rates.
  ShMOLLI is faster and less sensitive to heart rate, but less precise. **SASHA is closer to
  the true T1 but noisier.**
- In real tissue, the biggest source of error is **magnetization transfer**, which mainly
  lowers the T1 of MOLLI and ShMOLLI ([](./04-issues.md)).
- T1 values from different methods cannot be compared directly. Normal values are **only
  valid for the method they were measured with**.

## The three methods at a glance

| | MOLLI | ShMOLLI | SASHA |
|---|---|---|---|
| Preparation | 3 inversions | 3 inversions | saturation before each image |
| Scheme | 3(3)3(3)5 | 5(1)1(1)1 | 1 + 9 saturated images |
| Breath-hold (60 beats per minute) | 17 heartbeats | 9 heartbeats | 10 heartbeats |
| Images in the fit | 11 | 5 (long T1) or 7 (short T1) | 10 |
| How T1 is obtained | Look-Locker fit + $B/A$ correction | Look-Locker fit + $B/A$ correction | saturation-recovery fit |
| Accuracy, simulation (native myocardium) | −4% | −5% | exact |
| Accuracy, pig hearts [@hafyane2018] | −11% | −17% | +4% |
| Precision, simulation (SD at SNR 40) | 17 ms (best) | 33 ms | 70 ms (worst) |
| Blood at 90 beats per minute, simulation | −13% | −6% | exact |
| Sensitive to MT | strongly | strongly | less, but measurable |
| Sensitive to T2 and off-resonance | yes | yes | hardly |
| Main strength | most precise | short breath-hold, little effect of heart rate | closest to the true T1 |
| Main weakness | heart rate, MT | less precise than MOLLI | noisy |

The simulation values come from {numref}`fig-side-by-side`, {numref}`fig-heart-rate` and
{numref}`fig-precision`; they show trends, not exact clinical values. The sensitivities to
MT, T2 and off-resonance are taken from [@barral2018; @robson2013; @hafyane2018].
