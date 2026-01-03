---
title: "RandomX"

translationOutdated: "no"
contentOutdated: "no"
---

<!-- If the English version is outdated, all versions (for all languages) will be outdated. No need to check the state of the translations. -->
{% if contentOutdated == "yes" %}
## **{{ notices.outdatedContent }}**

<!-- If page is translated but the English version was updated, the translation is outdated -->
{% elif translationOutdated == "yes" %}
## **{{ notices.outdatedTranslation }}**
{% endif %}

<!-- Show the body -->
# RandomX
!!! info ""
    **_Written in 2019_**
    Pulled from [Monero Outreach](https://github.com/monero-ecosystem/outreach-docs/blob/master/monero-outreach-docs%2Fen%2Fstoryboard%2FrandomX_en.md).

**Monero and Arweave to Validate the Proof-of-Work Algorithm. - 5th of June, 2019**

What year is it? It seems like only yesterday they were saying that a privacy coin couldn’t be pruned and that ASICs will win in the end. But here we are...about to prune and talking about RandomX...wearing our space helmets. RandomX still must go through the process of becoming tried and true, but it’s an exciting part of Monero’s pipeline. This guide gives an overview of its nature and plans, and where you can learn more.

### _What is RandomX?_

RandomX is a new Proof-of-Work (PoW) algorithm that Monero is scheduled to begin using in the next network update. RandomX is designed to be ASIC resistant by using random code execution and memory-hard techniques to prevent specialized mining hardware from dominating the network. Because RandomX is optimized for general-purpose CPUs, the network will become more decentralized and egalitarian in the distribution of block rewards.

Visit the [github.com/tevador/RandomX](https://github.com/tevador/RandomX) for more details or watch Howard Chu (hyc) speak about [RandomX at Monero Konferenco](https://github.com/monero-ecosystem/outreach-docs/blob/master/monero-outreach-docs%2Fen%2Ftranscriptions%2Fmonero-konferenco-2019%2FASIC-Resistant_Proof_of_Work-Fact_or_Fantasy.md). At the time of writing, RandomX is beginning the auditing process with [Trail Of Bits](https://www.trailofbits.com/), [X41](https://www.x41-dsec.de/), [Quarkslab](https://www.quarkslab.com/) and the [Kudelski Group](https://www.nagra.com/). RandomX is scheduled to go live during the next Monero network update.

RandomX has two modes with different memory requirements and performance. _Fast Mode_ requires 2GB of shared memory but has 4x-6x the performance of _Light Mode_ which only requires 256MB of RAM. _Fast mode_ is intended for dedicated miners. _Light mode_ is designed to allow fullnodes to validate blocks without requiring the 2+GB of RAM, so that small devices (like ARM single-board computers, e.g. Rock64) can still be used as standalone nodes.

| CPU | OS | Threads | RAM | CryptoNight-R (v8) | RandomX Fast Mode | RandomX Light Mode |
|--|--|--|--|--|--|--|
| AMD Ryzen 7 1700 | Ubuntu 16.04 | 8 | 16 GB DDR4 | 650 H/s | 4100 H/s | 620 H/s |
| Intel Core i7-8550U | Windows 10 | 4 | 16 GB DDR4 | 240 H/s | 1700 H/s | 350 H/s |
| Intel Core i3-3220 | Ubuntu 16.04 | 4 | 4 GB DDR3 | 75 H/s | 510 H/s | 150 H/s |

| GPU | Clockspeed | CryptoNight-R (v8) | RandomX |
|--|--|--|--|
| GTX 1660 Ti | 2070/13760 MHz | 626 H/s (98 W) | 660 H/s (103 W) |
| GTX 1080 Ti | 1930/10010 MHz | 787 H/s (145 W) | 1136 H/s (190 W) |

### _RandomX Collaboration_

RandomX was developed for Monero by tevador, hyc, vielmetti, antanst and SChernykh. Already other organizations are interested in adopting it. [Arweave](https://www.arweave.org/), a serverless storage enabler donated the Trail of Bits audit to the Monero community and will be implementing RandomX before Monero for their unique application. Arweave provides an innovative cryptocurrency-based approach to decentralized, long-term data storage. Mining on Arweave relies on both proof of work and—as a new concept unique to Arweave—proof of access. Arweave miners are incentivized through proof of access to replicate and have quick access to data stored in the network.

[Wownero](http://wownero.org/) is also launching RandomX in their upcoming v0.6 update and will call it RandomWOW. RandomX code will be updated after the audits are complete, so there will be some code divergence by the time Monero forks in October. Another difference is that RandomWOW will have a smaller scratchpad for hashing, 1MB instead of 2MB, smaller number of VM execution iterations, and increased chained VM executions per hash to increase program compilation cost for GPUs.

### _Learn More_

- Howard Chu (hyc) at Monero Konferenco: [ASIC-Resistant Proof of Work: Fact or Fantasy?](https://github.com/monero-ecosystem/outreach-docs/blob/master/monero-outreach-docs%2Fen%2Ftranscriptions%2Fmonero-konferenco-2019%2FASIC-Resistant_Proof_of_Work-Fact_or_Fantasy.md)
- Press Release with Arweave: [Monero Arweave Team to Validate the Proof-of-Work](https://github.com/monero-ecosystem/outreach-docs/blob/master/monero-outreach-docs%2Fen%2Fwebsite-sections%2Fnews%2Fmonero_arweave_pow_en.md)
- MoneroTalk 6/5/19 - Howard Chu & Sam Williams of Arweave: [monerotalk.live/randomx-progress-w-howard-chu-and-sam-williams-of-arweave](https://www.monerotalk.live/randomx-progress-w-howard-chu-and-sam-williams-of-arweave)
- MoneroTalk 3/27/19 - Howard Chu, Tevador & Needmoney90: [youtube.com/watch?v=vGMTrA6NmeM](https://www.youtube.com/watch?v=vGMTrA6NmeM)
