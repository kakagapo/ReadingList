# Designing Data-Intensive Applications

## Chapter 1 - Reliable, Scalable and Maintainable Applications

### Classification of faults

Hardware Faults
Software Errors - also includes systemic errors arising out of architectural issues and cascding failures
Human Errors - main culprit being configuration mistakes. Can be mitigated by using well designed abstractions, APIs and admin interfaces.
Mean Time to Failure (MTTF) of hard disk = 10 to 50 years

Maintainability

- Operability
- Simplicity
- Evolvability

### Scalability

Don't use average to measure performance. Use percentiles.
head-of-line blocking
Tail latency amplification
No one-size fits all solution when it comes to scaling

Algorithms for computing percentiles at scale

- forward decay
- t-digest
- HdrHistogram

Scaling

- Horizontal vs vertical

## Chapter 7 - Transactions

Atomicity

Consistency means different things in different contexts.
In CAP theorem, it means linearizability.
In the context of ACID, it refers to app-specific notion of DB being in good-state.

Isolation - strict sense means serializability
But, there are weaker isolation levels.

Durability