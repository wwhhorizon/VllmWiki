# vllm-project/vllm#32367: [Performance]: why compressed-tensors only support sym quantization?

| 字段 | 值 |
| --- | --- |
| Issue | [#32367](https://github.com/vllm-project/vllm/issues/32367) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: why compressed-tensors only support sym quantization?

### Issue 正文摘录

### Proposal to improve performance As [compressed-tensors-moe](https://github.com/vllm-project/vllm/blob/8471b27df97c3eb79f891802fc0e858f8f7ac6a0/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py#L1136) shown, it only support sym quantization. Is there any constraint for asym quantization？ ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s there any constraint for asym quantization？ ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Performance]: why compressed-tensors only support sym quantization? performance;stale ### Proposal to improve performance As [compressed-tensors-moe](https://github.com/vllm-project/vllm/blob/8471b27df97c3eb79f891802fc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/8471b27df97c3eb79f891802fc0e858f8f7ac6a0/vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py#L1136) shown, it only support sym quantization. Is there any const...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: rmance;stale ### Proposal to improve performance As [compressed-tensors-moe](https://github.com/vllm-project/vllm/blob/8471b27df97c3eb79f891802fc0e858f8f7ac6a0/vllm/model_executor/layers/quantization/compressed_tensors/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
