---
title: Edwards25519 Elliptic Curve
---
# Edwards25519 Elliptic Curve

!!! note
    Author is nowhere close to being a cryptographer. Be sceptical on accuracy.

!!! note
    This article is only about the underlying curve. Public key derivation and signing algorithm will be treated separately. 

Monero employs edwards25519 elliptic curve as a basis for its key pair generation.

The curve comes from the Ed25519 signature scheme. While Monero takes the curve unchanged, it does not exactly follow rest of the Ed25519.

The edwards25519 curve is [birationally equivalent to Curve25519](https://tools.ietf.org/html/rfc7748#section-4.1).

## Definition

This is the standard edwards25519 curve definition, no Monero specific stuff here,
except the naming convention. The convention comes from the CryptoNote
whitepaper and is widely used in Monero literature.

### Curve equation

    −x^2 + y^2 = 1 − (121665/121666) * x^2 * y^2

Note:

* curve is in two dimensions (nothing fancy, like all the curves is high school)
* curve is symmetric about the x axis due to `y^2` part of the equation (and about the y axis due to `x^2`)

### Base point: `G`
 
The base point is a specific point on the curve. It is used
as a basis for further calculations. It is an arbitrary choice
by the curve authors, just to standardize the scheme.
 
Note that it is enough to specify the y value and the sign of the x value.
That's because the specific x can be calculated from the curve equation.
    
    G = (x, 4/5)  # take the point with the positive x
    
    # The hex representation of the base point
    5866666666666666666666666666666666666666666666666666666666666666    

### Prime order of the base point: `l`

In laymen terms, the "canvas" where the curve is drawn is assumed
to have a finite "resolution", so point coordinates must "wrap around"
at some point. This is achieved by working modulo the prime `q` (see below).

The `l` value (lowercase L) is a different number; it is the order of the base point `G`,
meaning that multiplying `G` by `l` will give back the neutral element of the curve.
In other words, the `l` defines the maximum scalar usable.

    l = 2^252 + 27742317777372353535851937790883648493
    # => 7237005577332262213973186563042994240857116359379907606001950938285454250989

The `l` is a prime number specified by the curve authors.

In practice this is the private key's strength.

### Total number of points on the curve

Point coordinates are integers modulo the prime number:

    q = 2^255 - 19

The total number of points on the curve is not a prime number. It is `8 * l`
(the curve has a cofactor of 8), and the base point `G` generates the subgroup of `l` points.

In practice not all points are "useful" and so the private key strength is limited to `l` describe above.

## Implementation

Monero uses (apparently modified) Ref10 implementation by Daniel J. Bernstein.

## Reference

* [A (Relatively Easy To Understand) Primer on Elliptic Curve Cryptography](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)
* [RFC 8032 defining EdDSA](https://tools.ietf.org/html/rfc8032)
* [Understanding Monero Cryptography](https://steemit.com/monero/@luigi1111/understanding-monero-cryptography-privacy-introduction) - excellent writeup by Luigi
* [StackOverflow answer](https://monero.stackexchange.com/questions/2290/why-how-does-monero-generate-public-ed25519-keys-without-using-the-standard-publ)
* [Python implementation](https://github.com/monero-project/mininero/blob/master/ed25519.py) - not the reference one but easier to understand
* [Encoding point to hex](https://monero.stackexchange.com/questions/6050/what-is-the-base-point-g-from-the-whitepaper-and-how-is-it-represented-as-a)
* [EdDSA on Wikipedia](https://en.wikipedia.org/wiki/EdDSA)
