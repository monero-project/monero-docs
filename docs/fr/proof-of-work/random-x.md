---
title: "RandomX"

translationOutdated: "yes"
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
*06/05/19*
_**Monero y Arweave a validar el algoritmo de Prueba-de-Trabajo.**_

¿Qué año es? Parece que sólo fue ayer cuando decían que una moneda privada no podía reducir su tamaño de almacenamiento y que los ASICs ganarían al final. Pero aquí estamos... reduciendo el tamaño del almacenamiento y hablando de RandomX... con los cascos espaciales puestos. RandomX aún debe pasar por un proceso de prueba y autenticidad, pero es una parte emocionante del desarrollo de Monero. Esta guía da una descripción general de su naturaleza y plan, y, para que puedas aprender más.

## _¿Qué es RandomX?_

RandomX es un algoritmo de prueba-de-trabajo (PoW - siglas en inglés) nuevo que está programado para ser usado en la próxima actualización de Monero. RandomX está diseñado para ser resistente a los ASIC al utilizar códigos de ejecución aleatorios y técnicas de memoria exigentes para prevenir la dominación de la red por hardware de minería especializado. Siendo el propósito general de RandomX optimizar los CPUs, la distribución de la recompensa en la red será más descentralizada e igual para todos.

Howard Chu (hyc) estará hablando sobre RandomX en la conferencia de Monero, [Monero Konferenco](https://monerokon.com/), mientras tanto, visita el [repositorio en Github de RandomX](https://github.com/tevador/RandomX) para más detalles. Al momento de escribir este artículo, RandomX está empezando el proceso de ser auditado por [Trail Of Bits](https://www.trailofbits.com/), [X41](https://www.x41-dsec.de/), [Quarkslab](https://www.quarkslab.com/en/) y el [Grupo Kudelski](https://www.nagra.com/). RandomX está programado a lanzarse en la próxima actualización en la red de Monero.

## _¿Qué va a cambiar?_

Los ASICs serán los principales afectados por RandomX, y como será optimizado para los CPUs, los GPUs no tendrán el mismo incremento en el hashrate o en el índice de procesamiento. Referencias anteriores en las tarjetas de video [Nvidia (CUDA)](https://github.com/SChernykh/RandomX_CUDA) revelan un incremento del hashrate entre un 100% y un 150%, y se espera que se mejore con mayor optimización. Trabajo para los GPUs AMD (OpenCL) está en camino. Al ser RandomX exigente en memoria, se espera que los botnets y el malware en la minería se reduzca al ser el consumo de la memoria fácilmente detectado por los administradores. Una reducción en general del total del hashrate en la red incrementará la recompensa a los mineros legítimos, sin importar si minan con CPUs o GPUs.

RandomX tiene dos modalidades con diferentes requerimientos y rendimientos de memoria. El Modo rápido requiere de 2 GB de memoria compartida pero tiene 4-6 veces más del rendimiento del Modo ligero que solo requiere de 256 MB de memoria RAM. El Modo rápido está destinado a mineros dedicados. El Modo ligero está diseñado para permitir a los nodos completos validar bloques sin necesitar las 2+GB de memoria RAM, para que los dispositivos pequeños (como los computadores ARM con board único, por ejemplo, el Rock64) puedan seguir siendo usados como nodos independientes.

| CPU | Sistema Operativo | Núcleos | RAM | CryptoNight-R (v8) | RandomX Modo Rápido | RandomX Modo Ligero |
|--|--|--|--|--|--|--|
| AMD Ryzen 7 1700 | Ubuntu 16.04 | 8 | 16 GB DDR4 | 650 H/s | 4100 H/s | 620 H/s |
| Intel Core i7-8550U | Windows 10 | 4 | 16 GB DDR4 | 240 H/s | 1700 H/s | 350 H/s |
| Intel Core i3-3220 | Ubuntu 16.04 | 4 | 4 GB DDR3 | 75 H/s | 510 H/s | 150 H/s |

| GPU | Frecuencia | CryptoNight-R (v8) | RandomX |
|--|--|--|--|
| GTX 1660 Ti | 2070/13760 MHz | 626 H/s (98 W) | 660 H/s (103 W) |
| GTX 1080 Ti | 1930/10010 MHz | 787 H/s (145 W) | 1136 H/s (190 W) |

## _Cooperación para RandomX_

RandomX fue desarrollado para Monero por tevador, hyc, vielmetti, antanst y SChernykh. Otras organizaciones están ya interesadas en adoptarlo. [Arweave](https://www.arweave.org/), un habilitador de almacenaje sin servidor, le donó la auditoría de Trail Of Bits a la comunidad de Monero y estará implementando RandomX para su aplicación antes que Monero. Arweave provee una innovadora propuesta basada en criptomonedas para descentralizar en el largo plazo el almacenamiento de la información. La minería de Arweave depende tanto de la prueba-de-trabajo y en un nuevo concepto único para Arweave, prueba-de-acceso.

[Wownero](http://wownero.org/) también estará lanzando RandomX en su próxima actualización v0.6 y le llamará RandomWOW. El código de RandomX será actualizado después de que las auditorías estén completas, para entonces habrán algunas diferencia en el código para el momento de la bifurcación en octubre. Otra diferencia es que RandomWOW tendrá un almacenamiento local menor interno para hashing, 1 MB en vez de 2 MB, un menor número de iteraciones en las ejecuciones de la máquina virtual (VM - siglas en inglés) y un incremento encadenado en las ejecuciones de la VM por hash para incrementar el costo programático de compilación para los GPUs.
