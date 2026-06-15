# vllm-project/vllm#42882: [Feature]: Make DS layout used by default

| 字段 | 值 |
| --- | --- |
| Issue | [#42882](https://github.com/vllm-project/vllm/issues/42882) |
| 状态 | open |
| 标签 | performance;feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make DS layout used by default

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently vLLM uses SMM Conv state layout set as `SD` `(state_len, dim)`. Recent PR [[Kernel] Mamba support different layout for Conv state#37416](https://github.com/vllm-project/vllm/pull/37416) has created support for transposed `DS` layout `(dim, state_len)`. Based on perf numbers showed in this PR `DS` layout has ~1.5x better TTFT compared to `SD` layout (perf numbers were taken from PR #37416 description Benchmark section): ``` ================================================================================ BENCHMARK SUMMARY ================================================================================ DS: ------------------------------------------------------------ TP | Req/s | Tok/s | TTFT(ms) | TPOT(ms) ------------------------------------------------------------ 1 | 20.61 | 4009.30 | 128.67 | 23.50 2 | 24.15 | 4686.47 | 119.85 | 21.18 4 | 28.48 | 5556.18 | 112.23 | 18.23 SD: ------------------------------------------------------------ TP | Req/s | Tok/s | TTFT(ms) | TPOT(ms) ------------------------------------------------------------ 1 | 20.34 | 3954.31 | 142.86 | 23.78 2 | 23.86 | 4681.23 | 161.49 | 20.92 4 | 26.63 | 5182.43 | 1...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: pared to `SD` layout (perf numbers were taken from PR #37416 description Benchmark section): ``` ================================================================================ BENCHMARK SUMMARY =======================...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ure request ### 🚀 The feature, motivation and pitch Currently vLLM uses SMM Conv state layout set as `SD` `(state_len, dim)`. Recent PR [[Kernel] Mamba support different layout for Conv state#37416](https://github.com/v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: Make DS layout used by default performance;feature request ### 🚀 The feature, motivation and pitch Currently vLLM uses SMM Conv state layout set as `SD` `(state_len, dim)`. Recent PR [[Kernel] Mamba support d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Make DS layout used by default performance;feature request ### 🚀 The feature, motivation and pitch Currently vLLM uses SMM Conv state layout set as `SD` `(state_len, dim)`. Recent PR [[Kernel] Mamba support d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
