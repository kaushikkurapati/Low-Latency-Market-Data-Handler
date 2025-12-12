# Low Latency Market Data Handler

A C++ high-frequency trading market data feed handler for NASDAQ ITCH 5.0.
Designed to process multicast UDP feeds with microsecond-level latency using lock-free data structures.

## Development Roadmap

### Phase 1: Network & Architecture
- [ ] Implement Python UDP feed generator (Dummy Data)
- [ ] Implement C++ UDP Receiver (`recvfrom` loop)
- [ ] Implement Lock-Free Ring Buffer (SPSC)
- [ ] Thread Pinning (Producer/Consumer isolation)

### Phase 2: Protocol Parsing (NASDAQ ITCH 5.0)
- [ ] Parse System Event Messages (Type 'S')
- [ ] Parse Add Order Messages (Type 'A')
- [ ] Parse Order Executed Messages (Type 'E')
- [ ] Cast raw bytes to structs (Zero-Copy)

### Phase 3: Benchmarking & Optimization
- [ ] Instrument code with `rdtsc` / high_resolution_clock
- [ ] Generate Latency Histogram (P50, P99, P99.9)
- [ ] Optimize compiler flags (`-O3`, `-march=native`)