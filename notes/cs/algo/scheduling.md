# Scheduling

## Examples in opensource world
### Apache YRAN (Yet Another Resource Negotiator)
- Scheduler and ApplicationsManager
- Pluggable schedulers - CapacityScheduler and FairScheduler
- Resoruce reservation supported - takes as input profile of resources over-time and temporal constraints
- Federation supported (to link up mutiple YARN sub-clusters)

#### Capacity Scheduler
- 

# Job shop scheduling
- Optimization problem in CS and Operations Research(OR)
- Variant of optimal job scheduling
- NP hard
- Traveling Salesman problem is a simplfied case of this problem

## Scheduling metrics
- makespan - length of schedule for a set of jobs
- Avg (or total) flow-time (aka, job completion-time) - same as response time

## High level job scheduling
- confirm if the jobs form a DAG
- Create topo sort (better option is to construct a disjunctive graph)
- At the end of each window check for runnning job completion and if a running job had completed then loop over sorted results starting from the first unscheduled job 
- Loop over sorted result
    - At each node check if all parents have been visited
- confirm if the currently unblocked jobs 

# Further Reading
## Graphene: Packing and Dependency-aware Scheduling for Data-Parallel Clusters
    - not fair, heuristics bsed, heterogeneous DAGs
    - evaluated on 200-server cluster using traces of prod DAGs
    - results: median job completion time up by 25%, cluster throughput by 30%
    - 
### notes from intro section
    - Dryad, SparkSQL and Tez compile user scripts to DAGs
    - optimal schedule of heterogeneous DAGs is intractable
    - properties of pathologically bad schedules according to authors
        - long-running taks have no other work to overlap with them, which reduces parallelism
        - tasks that are runnable do not pack well with each other, which increases resource fragmentation
### other schedulers references in the paper
- Critical path (longest path from the task to the job output)-based schedulers
- Tetris - maximize the number of concurrently running tasks, greedily picks task with the highest value of the dot product between task's demand vector and the avaialble resource vector
### Intuition of Graphene
- trouble some tasks(very long or hard to pack) placed first onto virtual resource-time space (`d+1` dimensions, `d` dimensions for resources, `+1` for time)
