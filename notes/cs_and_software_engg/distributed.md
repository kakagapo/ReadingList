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

- "In Search of an Understandable Consensus Algorithm" by Diego Ongaro and John Ousterhout, Stanford University
- Directly address the replicated state machine problem
- Stronger from of leadership - log entries flow only from leader
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
- State space reduction - basically uses less variables to store internal state
- Logs are not allowed to have holes - how does this help ???
- Radomization used (in leader election) to reduce understandability but at the cost of introducing non-determinism
- Uses RPC and the whole algorithm uses 2 main calls, `AppendEntries` and `RequestVote`. One additional call, `InstallSnapshot`, to do log compaction.

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

- uses heartbeats to trigger election
- candidate wins an election if it receives votes from a majority
- randomized election timeouts

### Log replication

- Log entry is `comitted` once a it is replicated to a majority of the nodes and the leader applies the change to its local state machine
- todo: fill in more details

## Jupiter Rising: A Decade of Clos Topologies and Centralized Control in Google’s Datacenter Network

Todo

### Things to consider and balance

- Diversity of componets vs unformity : former guarantess that a singe issue does not take out the whole system, latter gives you ease of maintenance and mgmt.
- placing workloads closeby to efficiently communicate vs placing workloads farther apart for redundancy.
