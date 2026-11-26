---
title: 'Why measure T1 in the heart?'
numbering:
  enumerator: '1.%s'
  heading_2: true
  figure: true
  equation: true
---

## Recap on T1

[T1](https://qmrlab.org/mooc/t1-mapping#introduction) is the time constant with which the
longitudinal magnetization $M_z$ grows back after an RF pulse.
After one T1, $M_z$ has come about 63% of the way back, and after about 5 T1 the recovery
is practically complete. In a T1-weighted image, a tissue with a **short T1** has recovered
more by the time of the next pulse and appears **brighter**, while a tissue with a **long
T1** appears **darker**. A T1 map goes one step further: from several images taken at
different times during the recovery, a curve is fitted in every pixel, which gives T1 in
milliseconds [@barral2018].

## What T1 tells us about the heart

About 75% of the heart's volume consists of muscle cells. The remaining 25% is
extracellular space with collagen, other proteins and blood vessels [@barral2018].
Diseases change this composition. Scarring adds collagen and inflammation adds water, and
both **increase native T1**, which is T1 measured without contrast agent. A gadolinium
contrast agent shortens T1 and stays outside the cells, so comparing T1 before and after
contrast tells us how much extracellular space there is (the ECV) [@barral2018].

A well-known example is **myocarditis**, an inflammation of the heart muscle that can
follow a viral infection. The inflamed muscle contains more water, which raises native
T1, and an increased T1 or ECV is one of the two main criteria for diagnosing myocarditis
with MRI [@ferreira2018]. During the COVID-19 pandemic, US university sports conferences
used cardiac MRI, including these criteria, to check athletes for myocarditis before they
were allowed to play again [@daniels2021].

## Why the heart is difficult

The heart beats and the patient breathes. To get sharp images, the scan is triggered by
the ECG, so that images are always taken at the same moment of the heartbeat, and the
whole measurement has to fit into **one breath-hold of less than about 20 s**
[@barral2018].

Gold-standard [inversion recovery](https://qmrlab.org/mooc/t1-mapping#irintroduction) is much
too slow for this. With
a typical cardiac image size, each point on the recovery curve takes about **6 minutes**
[@barral2018]. Cardiac methods therefore give up some accuracy to be faster. How they do
this, and what it costs, is described in the following sections.
