# Blogs posts from top companies

## Twitter

- [Jan 2017 - The Infrastructure Behind Twitter: Scale](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2017/the-infrastructure-behind-twitter-scale)
- [Jul 2020 - Building Twitter’s ad platform architecture for the future](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2020/building-twitters-ad-platform-architecture-for-the-future)
- [Dec 2020 - Kafka as a storage system](https://blog.twitter.com/engineering/en_us/topics/infrastructure/2020/kafka-as-a-storage-system)

## Facebook

- [Use of BGP for routing in large-scale data centers](https://datatracker.ietf.org/doc/html/draft-ietf-rtgwg-bgp-routing-large-dc-09)

## Discord

- [Sep 2018 - How Discord Handles Two and Half Million Concurrent Voice Users using WebRTC](https://blog.discord.com/how-discord-handles-two-and-half-million-concurrent-voice-users-using-webrtc-ce01c3187429)
- [Feb 2020 - Why Discord is switching from Go to Rust](https://blog.discord.com/why-discord-is-switching-from-go-to-rust-a190bbca2b1f)

## Youtube

- [Youtube Architecture](http://highscalability.com/youtube-architecture)
- [Apr 2021 - Reimagining video infrastructure to empower YouTube](https://blog.youtube/inside-youtube/new-era-video-infrastructure/)

## Flipkart

- [Optimizing Flipkart’s Serviceability Data from 300 GB to 150 MB in-memory](https://tech.flipkart.com/remodelling-flipkarts-serviceability-data-an-optimization-journey-from-300-gb-to-150-mb-in-memory-5c7e9c38bde)

## Google

- [Jupiter Rising: A Decade of Clos Topologies and Centralized Control in Google’s Datacenter Network](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43837.pdf)
- [File Storage on Compute Engine](https://cloud.google.com/architecture/filers-on-compute-engine?hl=en)

## General reading list and information sources

- https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/saga/saga
- https://cloud.google.com/architecture
- [SRE Book - Introducing Non-Abstract Large System Design](https://sre.google/workbook/non-abstract-design/)
- [Nov 2008 - High Scalability - Google Architecture]http://highscalability.com/google-architecture

### Reimagining video infrastructure to empower YouTube

- Trascoding done using custom chip that Youtube folks call as Video (trans)Coding Unit (VCU)
- Resulted in 20-33x improvements in compute efficiency
- 500 hours of video uploaded every minute
- Video consumption went up during Covid-19 pandemic (1st quarter of 2020 - 25 percent increase)
- About Video codes:
  - VP9 - uses more computer resources(5x more) to encode compared to H.264
  - NExt-gen chip will have AV1 (compresses better than VP9 but is more computationally expensive)
- Talks about a unexpected issue caused by a loose screw shorting out one of the voltage regulators which in turn prevented the chip from comping up.

### The Infrastructure Behind Twitter: Scale

- Data from Pie chart listed in dsec. order of percentage. Last few rows don't have number associated with them because the pie-chart is missing that info but from the size of the slice i can clearly see that the relative order is as it is listed here.

| Component       | Percentage of machines|
|-----------------|-----------------------|
| Mesos           | 35.9 |
| Key-value store | 21.2 |
| Hadoop          | 19.6 |
| Front-end       | 10.7 |
| Cache           | 5.9  |
| Other services  | - |
| Messaging       | - |
| Database        | - |

- Started migrating from third-party hosting in 2010
- Late 2010 n/w arch finalized based on learnings from scale and service issues encountered in the hosted colo
- Deep buffer ToRs to support bursty service traffic, carrier grande core switches with no oversubscription at that layer
- Now PoPs (Points of Presence) in 5 continents, DCs with 100s of thousands of servers
- Early 2015 - reached a point when full mesh topology can't be supported and DC Interior Gateway Protocol(IGP) started to behave unexpectedly because of the scale and topology complexity
- Moved to Clos topology + BGP (done on a live network with minimal impact)

#### Highlights of the new approach

- Smaller blast radius of a single device failure.
- Horizontal bandwidth scaling capabilities.
- Lower routing engine CPU overhead; far more efficient processing of route updates.
- Higher route capacity due to lower CPU overhead.
- More granular control of routing policy on a per device and link basis.
- No longer exposed to several known root causes of prior major incidents: increased protocol reconvergence times, route churn issues and unexpected issues with inherent Open Shortest Path First (OSPF) complexities.
- Enables non-impacting rack migrations.

Traffic is split into 3 groups

- Data center traffic
- Backbone traffic - traffic between DCs
- Edge traffic

## AWS vs Azure vs Google cloud

### AWS

- Notes from https://www.rackspace.com/blog/aws-101-regions-availability-zones
- 16 regions, 42 avaialability zones.
- us-east-1, has five zones

### Azure

- https://docs.microsoft.com/en-us/azure/availability-zones/az-overview

### Glossary

- Availability Zone: Unique physical locations within a region. Each zone is made up of one or more datacenters equipped with independent power, cooling, and networking
