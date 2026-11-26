---
title: 'From inversion recovery to Look-Locker'
numbering:
  enumerator: '2.%s'
  heading_2: true
  figure: true
  equation: true
---

## Inversion recovery in short

In inversion recovery (IR), a 180° pulse flips $M_z$ from $+M_0$ to $-M_0$. After a time
TI an image is taken, and this is repeated for several TI values. Fitting an exponential to
these points gives T1, using one of the
[signal models](https://qmrlab.org/mooc/t1-mapping#signal-modelling) for inversion recovery.

The important point for the heart is the waiting. Before each new inversion, $M_z$ has to
recover almost completely, which takes about 5 T1. With four TI values and about 6 minutes
per point, an inversion recovery scan of the heart would take **24 minutes**, which is 72
breath-holds of 20 s [@barral2018].

## The Look-Locker idea

The [Look-Locker method](https://qmrlab.org/mooc/t1-mapping#other-saturation-recovery-t1-mapping-techniques)
inverts only once and then takes many short readouts while $M_z$ recovers
[@look1968; @barral2018]. With one readout every 100 ms, for example, it gets 50 points on
the curve in only 5 s. It is one of the most widely used T1 mapping techniques, and all
cardiac methods are built on it.

Every readout needs an RF pulse. A 90° pulse would tip all of $M_z$ into the transverse
plane and destroy the recovery we are trying to measure. Look-Locker therefore uses a
small flip angle $\alpha$ of a few degrees. It tips just enough of the magnetization to
get a signal and leaves most of $M_z$ along z.

## What each readout does to $M_z$

A readout pulse tilts the magnetization by $\alpha$ away from the z-axis, towards the
transverse plane. Only the part $M_z \cos\alpha$ stays along z. The tilted part,
$M_z \sin\alpha$, gives the signal and is then destroyed (spoiled) before the next readout
[@barral2018]. Each readout therefore makes $M_z$ **smaller in size, towards zero**. What
this means depends on where $M_z$ is:

- When $M_z$ is negative (arrow pointing down), towards zero means up. The tip **helps the
  recovery**, which is why the curve is ahead at the start.
- When $M_z$ is positive (arrow pointing up), towards zero means down. The tip **works
  against the recovery**, which is why the curve never reaches $M_0$.

:::{figure} #fig-ll-tip-output
:label: fig-ll-tip
One Look-Locker readout after another for muscle (T1 = 1130 ms), with a readout every
200 ms. The flip angle is exaggerated to 20° so that the tip is easy to see. Left: the
magnetization as an arrow (black) and, for comparison, without readouts (gray). At each
readout the arrow is tipped by $\alpha$; the blue part stays along z, the orange part is
the signal and is then spoiled. Right: $M_z$ at each readout compared to the recovery
without readouts. The slider moves through time, with two positions per readout (before
and after the tip).
:::

**Try this** in {numref}`fig-ll-tip`:

- Move the slider to "0.0 s tip". The arrow points down, and the tip turns it towards the
  transverse plane. Its z-part (blue) is now a bit shorter, so closer to zero.
- Move to 1.0 s. The black points are slightly **above** the gray curve (0.23 instead of
  0.18): so far the readouts have helped.
- Move to 2.0 s and then to the end. Now the arrow points up and every tip pulls it down.
  At 3.8 s it is only at 0.74, while the gray arrow is already at 0.93.

(ll-correction)=
## T1\*: what we actually measure

When we fit an exponential to the Look-Locker points, we get the time constant of the
*measured* curve. It is not the T1 of the tissue, because every readout disturbs the
recovery. We call it the apparent T1, written T1\*. **T1 is a property of the tissue, T1\*
is a property of the tissue and the measurement**: it also depends on the flip angle and on
how often we read out. With a flip angle of 8° and a readout every 100 ms, which is close
to a real scan, muscle (T1 = 1130 ms) gives T1\* ≈ 1018 ms, so 10% too short
[@deichmann1992].

The true T1 can be recovered from the fitted curve. If $A$ is the level the curve settles
at and $B$ the distance from the first point to this level, then
$T1 = T1^* \left(B/A - 1\right)$ [@barral2018]. This correction uses only values from the
fit, so it **does not need the flip angle**, which is never known exactly in a real scan.
MOLLI and ShMOLLI in the next section use exactly this correction.

Look-Locker solves the speed problem, but the heart adds another one: it moves. The next
section shows how MOLLI, ShMOLLI and SASHA fit the readouts into the heartbeat.
