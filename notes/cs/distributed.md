# Distributed systems

## Unavoiddable issues in practical distributed systesms

- Network delays
- partitions
- packet loss, duplication and reordering

## Consensus

- Paxos
- Raft

## Paxos

### Paxos problems

- Difficult to understand
- does not provide good foundation for practical implementation

### Paxos variants

- Single decree paxos
- Multi-paxos
- Egalitarian Paxos (EPaxos)

## Notes from Raft paper

- Title: In Search of an Understandable Consensus Algorithm
- Authors: Diego Ongaro and John Ousterhout, Stanford University
- Stronger from of leadership - lgo entries flow only from leader
- Uses randomized timers for leader election
- Joint consensus - majorities of 2 configurations overlap during transitions
- Properties of practical consensus algorithms
  - Safety under all non-Byzantine conditions
  - Available as long as majority of the servers are operational and communicate with each other and with clients

### Techniques used to improve understandability

- Problem decomposed into separate sub-problems
  - leader election
  - log replication
  - safety
  - membership changes
- State space reduction
- Logs are not allowed to have holes
- Radomization used to reduce understandability but at the cost of introducing non-determinism

## Large-scale systems with single cluster leader

- GFS and HDFS
- RAMCloud

## Invariants

- `Election Safety`: at most one leader can be elected in a given term.
- `Leader Append-Only`: a leader never overwrites or deletes entries in its log; it only appends new entries.
- `Log Matching`: if two logs contain an entry with the same index and term, then the logs are identical in all entries up through the given index.
- `Leader Completeness`: if a log entry is committed in a given term, then that entry will be present in the logs of the leaders for all higher-numbered terms.
- `State Machine Safety`: if a server has applied a log entry at a given index to its state machine, no other server will ever apply a different log entry for the same index.

## Node states

- Follower
- Candidate
- Leader

### Leader election

- candidate wins an election if it receives votes from a majority
- randomized election timeouts

### Log replication

- Comitted - 