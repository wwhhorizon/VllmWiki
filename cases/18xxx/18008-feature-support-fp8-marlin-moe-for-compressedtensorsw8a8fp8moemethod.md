# vllm-project/vllm#18008: [Feature]: Support FP8 Marlin MoE for CompressedTensorsW8A8Fp8MoEMethod

| 字段 | 值 |
| --- | --- |
| Issue | [#18008](https://github.com/vllm-project/vllm/issues/18008) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support FP8 Marlin MoE for CompressedTensorsW8A8Fp8MoEMethod

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Like what was added in https://github.com/vllm-project/vllm/pull/16850 for enabling marlin in fp8.py MoE layers, we should enable FP8 Marlin MoE for compressed tensors models to support users wanting to run them on older hardware. Basically you want to take the changes in fp8.py's moe method (https://github.com/vllm-project/vllm/pull/16850/files#diff-5511bfcc9c53f7d96517ad43e4087f6777bef21302da983f42cafae40a866644) and apply them to `CompressedTensorsW8A8Fp8MoEMethod` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Support FP8 Marlin MoE for CompressedTensorsW8A8Fp8MoEMethod good first issue;feature request ### 🚀 The feature, motivation and pitch Like what was added in https://github.com/vllm-project/vllm/pull/16850 for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: p8.py MoE layers, we should enable FP8 Marlin MoE for compressed tensors models to support users wanting to run them on older hardware. Basically you want to take the changes in fp8.py's moe method (https://github.com/v...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Feature]: Support FP8 Marlin MoE for CompressedTensorsW8A8Fp8MoEMethod good first issue;feature request ### 🚀 The feature, motivation and pitch Like what was added in https://github.com/vllm-project/vllm/pull/16850 for...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: arlin MoE for CompressedTensorsW8A8Fp8MoEMethod good first issue;feature request ### 🚀 The feature, motivation and pitch Like what was added in https://github.com/vllm-project/vllm/pull/16850 for enabling marlin in fp8....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
