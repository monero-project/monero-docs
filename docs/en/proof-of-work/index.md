---
title: Proof of Work
---
# Proof of Work

> Proof of work is a way to legitimize untrusted parties

### What exactly is proof of work?

Proof of work is a cryptographic proof that an untrusted party has committed significant computational resources to solve an artificial problem.

Technically, the "proof" is simply a solution to the problem at hand.

### It's all about legitimizing an untrusted party

How could an untrusted party on the Internet earn any level of your trust?

It can prove its commitment by solving an agreed-upon computationally hard problem.

For example, by requiring the untrusted party to perform a hard computation before you accept their connection, you limit connections only to "committed" parties.

As another example, you could require PoW to be attached to incoming e-mails to make spam prohibitively expensive.

### Work must be otherwise useless

The work on and solution to "computationally hard problems" cannot be useful in any other way than to prove the commitment.

If the work is useful elsewhere then it doesn't prove commitment to you.

The problem must be artificial. Otherwise incentives are skewed and the whole scheme breaks.

### Strong asymmetry

The requirement for a proof of work scheme is strong asymmetry for work vs verification resources.

The work must be arbitrarily hard. At the same time, proof verification must remain dirt cheap (in terms of computational resources).  

Cheap verification is critical because at this stage we are dealing with a potentially huge number of untrusted parties,
who could DoS the verifier by submitting invalid proofs. Such proofs should be trivial to discard.
