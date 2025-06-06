
# RandomX
*06/05/19*  
_**Monero et Arweave à la validation de l'algorithme de preuve de travail.**_ 

En quelle année sommes-nous ? Il semble qu'hier encore, ils disaient qu'une cryptomonnaie confidentielle ne pouvait être "élaguée" et que les ASIC finiraient par l'emporter. Mais nous voilà... sur le point de l'élaguer et de parler de RandomX... et de porter nos casques d'astronautes. RandomX doit encore faire ses preuves, mais c'est une étape passionnante du développement de Monero. Ce guide présente un aperçu de sa nature et de ses plans, et indique où vous pourrez en apprendre davantage. 

## _Qu'est-ce que RandomX ?_ 

RandomX est un nouvel algorithme de preuve de travail (PoW) dont Monero commencera l'expérimentation lors de la prochaine mise à jour du réseau. RandomX est conçu pour résister aux ASICs grâce à de l'exécution de code aléatoire et des techniques contraignantes en mémoire pour empêcher le matériel minier spécialisé de dominer le réseau. Comme RandomX est optimisé pour les processeurs généralistes, le réseau deviendra plus décentralisé et plus égalitaire dans la distribution des récompenses de blocs. 

Howard Chu (hyc) parlera de RandomX à la prochaine [Monero Konferenco](https://monerokon.com/), d'ici là, visitez le dépôt [GitHub RandomX](https://github.com/tevador/RandomX) pour plus de détails. Pour le moment, RandomX commence son processus d'audit avec [Trail Of Bits](https://www.trailofbits.com/), [X41](https://www.x41-dsec.de/), [Quarkslab](https://www.quarkslab.com/en/) et le [Groupe Kudelski](https://www.nagra.com/). RandomX devrait être activé lors de la prochaine mise à jour du réseau Monero.

## _Qu'est-ce qui va changer ?_

Les ASICs sont les principales victimes de RandomX, mais comme il est optimisé pour les CPU, les GPUs n'auront plus le même avantage de taux de hachage. Les premières [évaluations Nvidia (CUDA)](https://github.com/SChernykh/RandomX_CUDA) indiquent des augmentation du taux de hachage de 100 à 150%, et cela devrait continuellement s'améliorer. Le travail est en cours pour les GPUs AMD (OpenCL). Comme RandomX est contraignant en mémoire, on s'attend à ce que la proportion de botnets et de malwares diminue car ils se feront plus facilement remarquer par les administrateurs de part leur forte consommation de mémoire. Une baisse du taux de hachage du réseau augmentera proportionnellement les récompenses de blocs versées aux mineurs légitimes, qu'ils utilisent des CPUs ou des GPUs. 

RandomX dispose de deux modes avec des besoins en mémoire et des performances différents. Le mode rapide nécessite 2 Go de mémoire partagée, mais offre 4 à 6 fois les performance du mode allégé qui ne nécessite que 256 Mo de RAM. Le mode rapide est destiné aux stations d'extraction minière dédiées. Le mode allégé est conçu pour permettre aux nœuds complets de valider des blocs sans avoir besoin de 2+Go de RAM, de sorte que de petits périphériques (tel que des ordinateurs monocartes ARM comme Rock64) puissent toujours être utilisés comme des nœuds autonomes. 

| CPU | OS | Processus | RAM | CryptoNight-R (v8) | RandomX mode rapide | RandomX mode allégé |
|--|--|--|--|--|--|--|
| AMD Ryzen 7 1700 | Ubuntu 16.04 | 8 | 16 GB DDR4 | 650 H/s | 4100 H/s | 620 H/s |
| Intel Core i7-8550U | Windows 10 | 4 | 16 GB DDR4 | 240 H/s | 1700 H/s | 350 H/s |
| Intel Core i3-3220 | Ubuntu 16.04 | 4 | 4 GB DDR3 | 75 H/s | 510 H/s | 150 H/s |  

| GPU | Cadence | CryptoNight-R (v8) | RandomX |
|--|--|--|--|
| GTX 1660 Ti | 2070/13760 MHz | 626 H/s (98 W) | 660 H/s (103 W) |
| GTX 1080 Ti | 1930/10010 MHz | 787 H/s (145 W) | 1136 H/s (190 W) |  

## _La Collaboration RandomX_ 

RandomX a été développé pour Monero par tevador, hyc, vielmetti, antanst et SChernykh. D'autres organisations sont déjà intéressées par son adoption. [Arweave](https://www.arweave.org/), un facilitateur de stockage sans serveur a fait don de l'audit Trail of Bits à la communauté Monero et va implémenter RandomX avant Monero pour leur propre utilisation. Arweave fournit une approche innovante basée sur les cryptomonnaies pour le stockage décentralisé à long terme des données. L'extraction minière sur Arweave repose à la fois sur une preuve de travail et, c'est un nouveau concept propre à Arweave, sur une preuve d'accès. Les mineurs d'Arweave sont incités par cette preuve d'accès à dupliquer et à avoir un accès rapide aux données stockées sur le réseau. 

[Wownero](http://wownero.org/) lance également RandomX dans sa prochaine mise à jour v0.6 et l'appellera RandomWOW. Le code RandomX sera mis à jour une fois les audits terminés, il y aura donc quelques divergences du code lors de la prochaine mise à jour du réseau Monero. Une autre différence réside dans le presse-papier de hachage plus petit de RandomWOW, 1Mo au lieu de 2Mo, le plus petit nombre d'itérations d'exécution de VMs, et l'augmentation du chaînage des exécutions de VMs afin augmenter le coût de compilation du programme pour les GPU. 

