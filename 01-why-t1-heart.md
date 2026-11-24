---
title: 'Why measure T1 in the heart?'
numbering:
  enumerator: '1.%s'
  heading_2: true
  figure: true
  equation: true
---

## Recap on T1

After an RF pulse tips the magnetization away from equilibrium, the longitudinal
magnetization $M_z$ grows back towards its equilibrium value $M_0$. This regrowth is
exponential and its time constant is called T1 [@barral2018]. After one T1, $M_z$ has
come about 63% of the way back to $M_0$, and after about 5 T1 the recovery is practically
complete. A tissue with a short T1 recovers quickly, a tissue with a long T1 recovers
slowly.

In a T1-weighted image the next RF pulse comes before every tissue has fully recovered
(short TR). A tissue with a **short T1** has regrown more of its $M_z$ by then, so it gives
more signal and appears **brighter**. A tissue with a **long T1** has regrown less and appears
**darker**. Fat, for example, has a short T1 and is bright, while fluids have a long T1 and
are dark. Gadolinium contrast agents shorten T1, so tissue that takes up contrast becomes
brighter. Scarred (infarcted) tissue has more space between the cells, where the gadolinium
collects, so after contrast the scar becomes bright [@barral2018].

A T1-weighted image only tells us that one tissue is brighter or darker than another, in
arbitrary units. A T1 map is calculated from several images taken at different times
during the recovery. In every pixel a recovery curve is fitted to these images, which
gives a T1 value in milliseconds. These values can be compared between patients, scanners
and visits [@barral2018].

## What T1 tells us about the heart

About 75% of the heart's volume consists of muscle cells (myocytes). The remaining 25% is
extracellular space, made of fibroblasts, collagen, other proteins and blood vessels
[@barral2018]. Diseases change this composition. Scarring adds collagen and inflammation
adds water, and both **increase native T1**.

Cardiac T1 mapping is used in two ways [@barral2018]:

- Native T1, measured without contrast agent. It can help to separate healthy myocardium
  from acute injury with edema and from scars. It is also the method of choice when a
  contrast agent is too risky, for example in patients with chronic kidney disease.
- ECV. A gadolinium contrast agent shortens T1 and stays outside the cells. Comparing T1
  before and after contrast gives the fraction of tissue that is extracellular space,
  which is a marker of fibrosis.

A well-known example is **myocarditis**, an inflammation of the heart muscle that can
follow a viral infection. The inflamed muscle contains more water, which **raises native
T1**, and an increased T1 or ECV is one of the two main criteria for diagnosing myocarditis
with MRI [@ferreira2018]. During the COVID-19 pandemic, US university sports conferences
used cardiac MRI, including these criteria, to check athletes for myocarditis before they
were allowed to play again [@daniels2021].

## Why the heart is difficult

The heart beats and the patient breathes. To get sharp images, the scan is triggered by
the ECG, so that images are always taken at the same moment of the heartbeat. In
addition, the whole measurement has to fit into **one breath-hold of less than about 20 s**
[@barral2018].

The gold-standard method used in the brain (next section) is much too slow for this.
With a typical cardiac image size, each point on the recovery curve takes about
**6 minutes** [@barral2018]. Cardiac methods therefore give up some accuracy to be faster,
and most of this chapter is about this trade-off.
