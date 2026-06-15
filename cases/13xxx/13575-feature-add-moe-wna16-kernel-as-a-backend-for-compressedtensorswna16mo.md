# vllm-project/vllm#13575: [Feature]: Add moe_wna16 kernel as a backend for CompressedTensorsWNA16MoEMethod

| 字段 | 值 |
| --- | --- |
| Issue | [#13575](https://github.com/vllm-project/vllm/issues/13575) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add moe_wna16 kernel as a backend for CompressedTensorsWNA16MoEMethod

### Issue 正文摘录

### 🚀 The feature, motivation and pitch A triton implementation to support MoE layers quantized with GPTQ or AWQ was implemented in https://github.com/vllm-project/vllm/pull/12185 It is more performant than the current Marlin MoE kernel in the case where there are many, small experts - which is why I ported it to be the default in the case of `num_experts > 32` for AWQ and GPTQMarlin configs https://github.com/vllm-project/vllm/pull/13236 We should also propagate the usage of this kernel to `compressed-tensors` that have mixed precision. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Add moe_wna16 kernel as a backend for CompressedTensorsWNA16MoEMethod feature request;unstale ### 🚀 The feature, motivation and pitch A triton implementation to support MoE layers quantized with GPTQ or AWQ w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ant than the current Marlin MoE kernel in the case where there are many, small experts - which is why I ported it to be the default in the case of `num_experts > 32` for AWQ and GPTQMarlin configs https://github.com/vll...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Add moe_wna16 kernel as a backend for CompressedTensorsWNA16MoEMethod feature request;unstale ### 🚀 The feature, motivation and pitch A triton implementation to support MoE layers quantized with GPTQ or AWQ w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oe_wna16 kernel as a backend for CompressedTensorsWNA16MoEMethod feature request;unstale ### 🚀 The feature, motivation and pitch A triton implementation to support MoE layers quantized with GPTQ or AWQ was implemented i...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: opagate the usage of this kernel to `compressed-tensors` that have mixed precision. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
