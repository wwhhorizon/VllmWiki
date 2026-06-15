# vllm-project/vllm#15697: [Feature]: Composite model loading using `AutoWeightsLoader` for all models

| 字段 | 值 |
| --- | --- |
| Issue | [#15697](https://github.com/vllm-project/vllm/issues/15697) |
| 状态 | open |
| 标签 | good first issue;feature request;keep-open |
| 评论 | 39; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Composite model loading using `AutoWeightsLoader` for all models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch #9160 first introduced `AutoWeightsLoader` to recursively call `load_weights` on sub-modules. This lets composite models (most notably multi-modal models) use language backbones (`*Model` classes such as `LlamaModel`) without having to repeat their weight loading logic. Currently, `load_weights` is only implemented in a few language backbones. It would be great to standardize this approach and apply it to all language backbones in vLLM. The steps to do this are pretty straightforward: 1. Move the existing `load_weights` function from `*ForCausalLM` to `*Model`. 2. Create a new `load_weights` function in `*ForCausalLM` that loads the weights using `AutoWeightsLoader`. 3. Move any logic in `*Model.load_weights` that only applies to `*ForCausalLM` back to `*ForCausalLM.load_weights`. Usually, this involves `lm_head`. For reference, you can look at the implementation for models such as Llama, Gemma2/3, Qwen2 and ChatGLM. To avoid scope creep, I suggest opening a PR for updating only a few models at a time ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Composite model loading using `AutoWeightsLoader` for all models good first issue;feature request;keep-open ### 🚀 The feature, motivation and pitch #9160 first introduced `AutoWeightsLoader` to recursively ca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: reference, you can look at the implementation for models such as Llama, Gemma2/3, Qwen2 and ChatGLM. To avoid scope creep, I suggest opening a PR for updating only a few models at a time ### Alternatives _No response_ #...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: oading using `AutoWeightsLoader` for all models good first issue;feature request;keep-open ### 🚀 The feature, motivation and pitch #9160 first introduced `AutoWeightsLoader` to recursively call `load_weights` on sub-mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
