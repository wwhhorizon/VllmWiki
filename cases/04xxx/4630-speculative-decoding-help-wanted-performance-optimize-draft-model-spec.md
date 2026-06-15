# vllm-project/vllm#4630: [Speculative decoding] [Help wanted] [Performance] Optimize draft-model speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#4630](https://github.com/vllm-project/vllm/issues/4630) |
| 状态 | closed |
| 标签 | help wanted;performance;speculative-decoding |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Speculative decoding] [Help wanted] [Performance] Optimize draft-model speculative decoding

### Issue 正文摘录

### Proposal to improve performance With the end-to-end correctness tests merged in https://github.com/vllm-project/vllm/pull/3951, now we will optimize the implementation to get ~50% speedup on 70B model with temperature 1.0. ### Work required: P0/P1 -- priority (Small/Medium/Large) -- relative size estimate * Optimizing proposal time - [x] P0 (Large) Reduce draft model control-plane communication from O(num_steps) to O(1) - [x] P0 (Medium) Support draft model on different tensor-parallel-size than target model https://github.com/vllm-project/vllm/issues/4632 * Optimizations for scoring time - [x] P0 (Medium) Re-enable bonus tokens to increase % accepted tokens https://github.com/vllm-project/vllm/issues/4212 - [ ] P1 (Large) Replace CPU-based batch expansion with multi-query attention kernel call - [ ] P1 (Medium) Automate speculative decoding https://github.com/vllm-project/vllm/issues/4565 * Optimizations for both proposal and scoring time https://github.com/vllm-project/vllm/issues/5561 - [x] P0 (Medium) Decouple sampling serialization from sampling - [x] P1 (Large) Amortize `prepare_inputs` over multiple forward passes * Optimizations for scheduling time - [x] P0 (Medium) Pr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Speculative decoding] [Help wanted] [Performance] Optimize draft-model speculative decoding help wanted;performance;speculative-decoding ### Proposal to improve performance With the end-to-end correctness tests merged...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Speculative decoding] [Help wanted] [Performance] Optimize draft-model speculative decoding help wanted;performance;speculative-decoding ### Proposal to improve performance With the end-to-end correctness tests merged i
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ing ### Proposal to improve performance With the end-to-end correctness tests merged in https://github.com/vllm-project/vllm/pull/3951, now we will optimize the implementation to get ~50% speedup on 70B model with tempe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Q ### What should the target configuration be for 50% speedup? In the Anyscale fork we saw a 50% speedup on bs=8 with a 68m-sized draft model on TP1/70B target model on TP8 and a 7B draft model on TP(1|8)/70B target mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n 70B model with temperature 1.0. ### Work required: P0/P1 -- priority (Small/Medium/Large) -- relative size estimate * Optimizing proposal time - [x] P0 (Large) Reduce draft model control-plane communication from O(num...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
