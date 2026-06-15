# vllm-project/vllm#4632: [Performance] [Speculative decoding]: Support draft model on different tensor-parallel size than target model

| 字段 | 值 |
| --- | --- |
| Issue | [#4632](https://github.com/vllm-project/vllm/issues/4632) |
| 状态 | closed |
| 标签 | help wanted;performance;speculative-decoding |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance] [Speculative decoding]: Support draft model on different tensor-parallel size than target model

### Issue 正文摘录

## Overview Speculative decoding allows a speedup for memory-bound LLMs by using a fast proposal method to propose tokens that are verified in a single forward pass by the larger LLM. Papers report 2-3x speedup for bs=1, in Anyscale's fork we see up to 2x speedup with a small draft model for bs=8 (30% for bs=16) (we can improve this! see https://github.com/vllm-project/vllm/issues/4630 if you want to help). A key optimization for small models (68m/160m domain) is to use tensor-parallel degree 1, even if the target model is using tensor-parallel degree 4 or 8. In our fork, this reduces proposal time from 5ms/tok to 1.5ms/tok. This will allow a well-aligned 68m draft model to get 2x per-user throughput improvement on 70B target model. Furthermore, a 1B/7B proposer model may ideally be placed on TP=2 or TP=4, while the larger model is placed on TP=8. vLLM should support these configuration so the community can use the configuration best for their draft model. ## Design suggestions I implemented a Worker which patches the tensor parallel group to TP1 in our fork. The [code is dumped here](https://gist.github.com/cadedaniel/f8479bf5fa5543b946d2133b5db38c56). We should use this approach...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance] [Speculative decoding]: Support draft model on different tensor-parallel size than target model help wanted;performance;speculative-decoding ## Overview Speculative decoding allows a speedup for memory-bou...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance] [Speculative decoding]: Support draft model on different tensor-parallel size than target model help wanted;performance;speculative-decoding ## Overview Speculative decoding allows a speedup for memory-bou...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: rward pass by the larger LLM. Papers report 2-3x speedup for bs=1, in Anyscale's fork we see up to 2x speedup with a small draft model for bs=8 (30% for bs=16) (we can improve this! see https://github.com/vllm-project/v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2-3x speedup for bs=1, in Anyscale's fork we see up to 2x speedup with a small draft model for bs=8 (30% for bs=16) (we can improve this! see https://github.com/vllm-project/vllm/issues/4630 if you want to help). A key...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s/tok. This will allow a well-aligned 68m draft model to get 2x per-user throughput improvement on 70B target model. Furthermore, a 1B/7B proposer model may ideally be placed on TP=2 or TP=4, while the larger model is p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
