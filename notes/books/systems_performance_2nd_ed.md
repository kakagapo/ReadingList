# Peformance related books

## Systems Performance, 2nd Edition By Brendan Gregg

### Some areas w.r.t to performance

- kernel performance
- client performance
- language performance (e.g., Java)
- runtime performance (e.g., the JVM)
- performance tooling

### Observability

Observability tools use counters, profiling and tracing

#### Counters, Statistics, and Metrics

#### Profiling

#### Tracing

##### Static instrumentation

- Linumx kernel static instrumentation done via `tracepoints`
- For user-space software - `user statically defined tracing (USDT)` - used by libraries (eg., libc)
- Tool using USDT is `execsnoop` - traces new processes, showing the filename executed and argument list
- execsnoop is useful for revealing short-lived processes that may be missed by other observability tools such as top

##### Dynamic instrumentation

- 2004 - kprobes - difficult to use
- Popular dynamic tracing tool - `DTrace` (launched in 2005)

## BPF

- BPF Orginally stood for Berkeley Packet Filter
- powers the latest dynamic tracing tools in Linux
- originated as a mini in-kernel VM for speeding up the execution of tcpdump
- extended in 2013 to become a generic in-kernel execution env

## Other tracing tools

- perf and ftrace

### Experimentation

- tools in this catergory mainly include benchmarking tools
- Macro(simulated real-world workloads) vs micro(targets a specific component) benchmarking
- Micro-benchmarking example: run iperf on a idle server to figure out TCP n/w throughput
- `iperf -c 100.65.33.90 -i 1 -t 10` - run for 10 seconds and produce per-second averages
