---
title: 'Look-Locker: one inversion, many readouts'
numbering:
  enumerator: '3.%s'
  heading_2: true
  figure: true
  equation: true
---

## The idea

Gold-standard IR is slow because it only gets one point per inversion. After the image
at time TI, $M_z$ has to recover completely before the next inversion can be played.
For four points this already takes 24 minutes in the heart (see
[](./02-gold-standard.md)).

The Look-Locker method inverts only once and then takes many short readouts while $M_z$
recovers [@look1968; @barral2018]. In {numref}`fig-look-locker`, for example, one readout
is taken every 100 ms, which gives 50 points on the curve in only 5 s, short enough for a single breath-hold.

Every readout needs an RF pulse. A 90° pulse would tip all of $M_z$ into the transverse
plane and destroy the recovery we are trying to measure. Look-Locker therefore uses a
small flip angle $\alpha$ of a few degrees. It tips only a small part of the
magnetization, enough for the signal, and leaves most of $M_z$ along z.

## Every readout costs a bit of $M_z$

After a pulse with flip angle $\alpha$, only the fraction $\cos\alpha$ of $M_z$ remains
along z. For $\alpha = 8°$ this is $\cos 8° \approx 0.99$, so each readout removes about
1% of $M_z$ [@barral2018]. A single readout has almost no effect, but after 50 readouts
the difference becomes visible. The table compares muscle (T1 = 1130 ms) with and
without readouts for $\alpha = 8°$ and one readout every 100 ms:

| Time after inversion | $M_z/M_0$ without readouts | $M_z/M_0$ with readouts |
|---|---|---|
| 0 ms | −1.00 | −1.00 |
| 500 ms | −0.29 | −0.26 |
| 1000 ms | 0.18 | 0.19 |
| 3000 ms | 0.86 | 0.80 |
| 4900 ms | 0.97 | 0.89 |

Two things can be seen in the table:

1. At the beginning the curve with readouts is slightly ahead. As long as $M_z$ is
   negative, each pulse also makes it smaller in magnitude, which pushes it towards zero
   and helps the recovery. The curve therefore looks as if it recovered faster than T1
   would allow.
2. Later it falls behind and does not reach $M_0$. Close to the top, the recovery between
   two pulses only adds a little magnetization, and at some point this is exactly as much
   as one pulse removes. In this example the curve settles at about 0.9 instead of 1.

When an exponential is fitted to these points, the resulting time constant is too
short. It is called the apparent T1 and written T1\*. With $\alpha = 8°$ and a readout
every 100 ms, T1\* is about 1018 ms instead of 1130 ms, so 10% too short.

## The equations

The readouts still follow an exponential curve, only with different parameters
[@barral2018]:

```{math}
:label: eq-ll-signal
S(\mathrm{TI}) = A - B\, e^{-\mathrm{TI}/T1^*}
```

Here $A$ is the level the curve settles at ($A \approx 0.905$ in the example) and $B$ is
the distance from the first point to this level ($B \approx 0.905 + 1 = 1.905$).

How much shorter T1\* is depends on the flip angle $\alpha$ and on the time $\tau$
between two readouts [@deichmann1992; @barral2018]:

```{math}
:label: eq-ll-t1star
\frac{1}{T1^*} = \frac{1}{T1} - \frac{\ln(\cos\alpha)}{\tau}
```

Since $\ln(\cos\alpha)$ is negative, **T1\* is always shorter than T1**. The difference
becomes larger with a larger flip angle and with readouts closer together. For the
example, $1/1130 - \ln(\cos 8°)/100$ gives T1\* ≈ 1018 ms. In the literature $\tau$ is
often written TR, but here we use $\tau$ so that it is not confused with the TR of the
gold-standard IR scan.

## Getting the true T1 back

There are two ways to get T1 from T1\*:

- Solve {eq}`eq-ll-t1star` for T1. This requires the exact flip angle, but in a real scan
  the flip angle varies over the image and is never known exactly.
- Use $A$ and $B$ from the fit [@barral2018]:

  ```{math}
  :label: eq-ll-correction
  T1 = T1^* \left(\frac{B}{A} - 1\right)
  ```

  For the example this gives $1018 \times (1.905/0.905 - 1) \approx 1125$ ms, which is
  within 0.5% of the true 1130 ms. This correction **does not need the flip angle**, since
  all values come from the fit. The cardiac methods in the next section use it.

:::{admonition} Why does the $B/A$ correction work? (optional)
:class: dropdown
With a perfect inversion the curve starts at $-M_0$, so $B = A + M_0$ and
$B/A - 1 = M_0/A$. The more the readouts lower the final level (small $A$), the more
they also speed up the curve (short T1\*). For small flip angles the two effects are
linked in such a way that $M_0/A \approx T1/T1^*$, so multiplying by T1\* gives back T1.
:::

Look-Locker only works well if some conditions are met [@barral2018]:

| Condition | Reason |
|---|---|
| Small flip angle ($\alpha$ below about 10°) | with larger angles the correction becomes inaccurate |
| T1 much longer than $\tau$ | there are many readouts per recovery, so the points follow a smooth curve |
| $\tau$ much longer than T2, or spoiling | the transverse signal from one readout has to be gone before the next one |

{numref}`fig-look-locker` shows these effects for different flip angles.

:::{figure} #fig-look-locker-output
:label: fig-look-locker
Look-Locker sampling of muscle (T1 = 1130 ms) after a single perfect inversion. Left:
$M_z$ before each of 50 readouts spaced $\tau = 100$ ms apart, for the flip angle chosen
with the slider, compared to the recovery without readouts (gray). The dashed line is the
fit of {eq}`eq-ll-signal`, and the dotted line shows the final level $A$. Right: T1\*/T1
from {eq}`eq-ll-t1star` for three readout spacings. The simulation assumes perfect
spoiling and no noise.
:::

At $\alpha = 1°$ the points lie on the gray curve, so the readouts have almost no effect.
At 8°, the points recover faster than the gray curve and settle at about 0.9. The fit
gives T1\* ≈ 1018 ms, but the corrected T1 of about 1125 ms is within 0.5% of the true
value. At 15°, T1\* drops to about 812 ms (28% too short). The correction still works
reasonably well (about 1111 ms), but the error has grown to almost 2% because the
small-angle assumption no longer holds. The right plot shows that for the same flip angle
the effect is stronger when the readouts are closer together.

## Exercise

:::{exercise}
:label: ex-ll-mistake
A colleague measures Look-Locker data with $\alpha = 12°$ and fits it with
{eq}`eq-ll-signal`. She reports T1 = 904 ms for the muscle from
{numref}`fig-look-locker`. What went wrong and how large is the error?
:::

:::{solution} ex-ll-mistake
:class: dropdown
She reported T1\* instead of T1 and forgot the correction. The true T1 is 1130 ms, so
her value is 20% too short. With {eq}`eq-ll-correction` she would get about 1118 ms.
:::

The heart adds one more problem, because it moves. The next section shows how MOLLI,
ShMOLLI and SASHA deal with this.
