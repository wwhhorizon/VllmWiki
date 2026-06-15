# vllm-project/vllm#26402: [Bug]: EAGLE incompatible w/ Compressed Tensors Quantized Target Model

| 字段 | 值 |
| --- | --- |
| Issue | [#26402](https://github.com/vllm-project/vllm/issues/26402) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: EAGLE incompatible w/ Compressed Tensors Quantized Target Model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using an EAGLE head with a compressed tensors quantized model the acceptance rate silently fails to zero and therefore the perf completely degrades. **Root Cause**: EAGLE layers are registered as further layers in the target model. But in a compressed tensors checkpoint those are not part of the `ignore` list. Hence vLLM thinks the EAGLE layers are quantized, but they aren't. Surprisingly this does not give an error, but the acceptance rate essentially drops to zero as the EAGLE head is nor rubbish. **The structural problem**: The bigger problem IMO is that the `EagleProposer` simply takes the `VllmConfig` from the target model. This is not robust whenever the draft model has some different configurations.. In principle that is also the root cause why we required the hacky fix here https://github.com/vllm-project/vllm/pull/25667 to use a non-mm drafter for a mm model. **When did this happen?** [Update]: The PR from which on the bug happens is here https://github.com/vllm-project/vllm/pull/24982 ## Steps to reproduce: I am serving Llama 3.18B with the same EAGLE head and switching between BF16 model and the compressed tensors...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: EAGLE incompatible w/ Compressed Tensors Quantized Target Model bug ### Your current environment ### 🐛 Describe the bug When using an EAGLE head with a compressed tensors quantized model the acceptance rate silen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: EAGLE incompatible w/ Compressed Tensors Quantized Target Model bug ### Your current environment ### 🐛 Describe the bug When using an EAGLE head with a compressed tensors quantized model the acceptance rate silen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: the `VllmConfig` from the target model. This is not robust whenever the draft model has some different configurations.. In principle that is also the root cause why we required the hacky fix here https://github.com/vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ) ``` SpecDecoding metrics: Mean acceptance length: 1.99, Accepted throughput: 0.17 tokens/s, Drafted throughput: 0.88 tokens/s, Accepted: 162 tokens, Drafted: 820 tokens, Per-position acceptance rate: 0.616, 0.244, 0.1...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ns is here https://github.com/vllm-project/vllm/pull/24982 ## Steps to reproduce: I am serving Llama 3.18B with the same EAGLE head and switching between BF16 model and the compressed tensors model. ``` # MODEL_PATH=met...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
