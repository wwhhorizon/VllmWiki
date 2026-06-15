# vllm-project/vllm#32268: [Feature]: Refactor Int8ScaledMMLinearLayerConfig to use QuantKey

| 字段 | 值 |
| --- | --- |
| Issue | [#32268](https://github.com/vllm-project/vllm/issues/32268) |
| 状态 | open |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Refactor Int8ScaledMMLinearLayerConfig to use QuantKey

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Replace boolean configuration fields in [ScaledMMLinearLayerConfig](https://github.com/vllm-project/vllm/blob/510265472cb216daf7d8e83db6fa03ce48b0f5fc/vllm/model_executor/layers/quantization/kernels/scaled_mm/ScaledMMLinearKernel.py#L10C1-L10C2) with QuantKey objects to provide a more structured, type-safe quantization configuration API. Ideally we should change this: ```python @dataclass class ScaledMMLinearLayerConfig(ScaledMMLinearLayerConfig): is_static_input_scheme: bool is_channelwise: bool input_symmetric: bool ``` to this: ```python @dataclass class ScaledMMLinearLayerConfig(ScaledMMLinearLayerConfig): weight_quant_key: QuantKey activation_quant_key: QuantKey input_symmetric: bool ``` A parallel work found here #27814 , has split the configuration into Int8 and Fp8 config classes and uses Quantkey for the FP8 config class. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Refactor Int8ScaledMMLinearLayerConfig to use QuantKey help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch Replace boolean configuration fields in [ScaledMMLinearLayerConfig](...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Refactor Int8ScaledMMLinearLayerConfig to use QuantKey help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch Replace boolean configuration fields in [ScaledMMLinearLayerConfig](...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: MMLinearLayerConfig to use QuantKey help wanted;good first issue;feature request ### 🚀 The feature, motivation and pitch Replace boolean configuration fields in [ScaledMMLinearLayerConfig](https://github.com/vllm-projec...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
