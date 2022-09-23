# Gossip protocols

## Gossip objectives

## Types of protocols
1. Dissemination protocols or rumor-mongering protocols
2. 

## SWIM: Scalable Weakly-consistent Infection-style Process Group Membership Protocol
- piggybacks gossip messages on top of probe/ack messages
- no full syncs
- deletes dead node state immediately upon learning that the node is dead

## Serf
- membership, failure detection adn recovery and Custom event propagation
- over UDP with a configurable but fixed fanout and interval
- makes heavy use of Lamport's clocks (logical clock used for ordering events in distributed systems)
- Improvements over vanilla SWIM
    - periodic full sync over TCP
    - dedicated gossip msg + piggybacking support
- Flap dampening solution known as Lifeguard
