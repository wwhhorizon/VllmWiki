# vllm-project/vllm#39963: benchmark_serving: throughput collapses at 50K+ context due to aiohttp read buffer and shared session

| 字段 | 值 |
| --- | --- |
| Issue | [#39963](https://github.com/vllm-project/vllm/issues/39963) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;hardware_porting;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | fp8 |
| 症状 | mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> benchmark_serving: throughput collapses at 50K+ context due to aiohttp read buffer and shared session

### Issue 正文摘录

## Bug: `vllm bench serve` throughput drops ~10x at long context (50K+) due to client-side bottleneck ### Summary When running `vllm bench serve` with high concurrency at long context lengths (50K+ input tokens), throughput collapses dramatically — not because of the server, but because of the benchmark client's aiohttp session configuration. ### Evidence We benchmarked the same server (MiniMax-M2.5, 8x RTX 6000, EP=8) with two different bench tools using identical parameters (`--random-output-len 256`, `ignore_eos=True`, same prompt sizes): | Context (multi-user) | Tool A tok/s | vLLM bench tok/s | Tool A TTFT | vLLM bench TTFT | |---|---|---|---|---| | 8K | 503 | 494 | 1,493ms | 3,226ms | | 32K | 591 | 640 | 790ms | 3,757ms | | **50K** | **486** | **44** | 1,331ms | **134,173ms** | | **100K** | **298** | **25** | 1,016ms | **97,115ms** | At 8K/32K both tools report similar numbers. At 50K+ the vLLM bench tool collapses to ~10% throughput with TTFT exploding to 2+ minutes. **The server is identical** — this is purely a client-side measurement artifact. ### Root Cause (code analysis) **1. aiohttp `read_bufsize` — default 64KB is too small** `vllm/benchmarks/serve.py` creates the s...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ronment - vLLM bench: latest (cloned 2026-04-16) - Server: MiniMax-M2.5 FP8, 8x RTX 6000 Pro Blackwell, EP=8 - Dataset: random, `--random-output-len 256` - Multi-user: `--request-rate inf` (all at once) ### Impact Anyon...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: uration. ### Evidence We benchmarked the same server (MiniMax-M2.5, 8x RTX 6000, EP=8) with two different bench tools using identical parameters (`--random-output-len 256`, `ignore_eos=True`, same prompt sizes): | Conte...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: benchmark_serving: throughput collapses at 50K+ context due to aiohttp read buffer and shared session ## Bug: `vllm bench serve` throughput drops ~10x at long context (50K+) due to client-side bottleneck ### Summary Wh
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: bench serve` at long context (50K+) with high concurrency will see artificially low numbers — the bottleneck is the bench tool, not the server. This can lead to incorrect conclusions about server performance. correctnes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: otal=6 * 60 * 60), ) ``` At 50K+ context with many concurrent streaming requests, the server sends large chunks. The 64KB buffer fills up before the client can consume it, creating backpressure that cascades into the se...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
