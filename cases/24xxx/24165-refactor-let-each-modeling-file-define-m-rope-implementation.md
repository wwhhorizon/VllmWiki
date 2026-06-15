# vllm-project/vllm#24165: [Refactor]: Let each modeling file define M-RoPE implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#24165](https://github.com/vllm-project/vllm/issues/24165) |
| 状态 | closed |
| 标签 | good first issue;multi-modality |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Refactor]: Let each modeling file define M-RoPE implementation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, M-RoPE is implemented inside a single file (https://github.com/vllm-project/vllm/blob/main/vllm%2Fmodel_executor%2Flayers%2Frotary_embedding%2Fmrope.py) just like other RoPE methods. However when running the model, the model type in the HF config is used to further select the model-specific M-RoPE implementation. This is not maintainable in the long run as the number of models that use M-RoPE increases. Considering that much of the M-RoPE code is shared between models, with the main difference being how to get the input positions, I propose a `SupportsMRoPE` interface for the model class to define this step inside each modeling file. This interface should include a flag variable and also a `get_mrope_input_positions` method to get the input positions specific to that model. We can also use this interface to determine whether a model supports M-RoPE, instead of having to set this flag in the HF config. ### Alternatives _No response_ ### Additional context cc @ywang96 @Isotr0py ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Refactor]: Let each modeling file define M-RoPE implementation good first issue;multi-modality ### 🚀 The feature, motivation and pitch Currently, M-RoPE is implemented inside a single file (https://github.com/vllm-proj...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ain difference being how to get the input positions, I propose a `SupportsMRoPE` interface for the model class to define this step inside each modeling file. This interface should include a flag variable and also a `get...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , the model type in the HF config is used to further select the model-specific M-RoPE implementation. This is not maintainable in the long run as the number of models that use M-RoPE increases. Considering that much of...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
