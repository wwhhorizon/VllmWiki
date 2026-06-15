# vllm-project/vllm#12602: [Feature]: separating reasoning and answer for reasoning models

| 字段 | 值 |
| --- | --- |
| Issue | [#12602](https://github.com/vllm-project/vllm/issues/12602) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: separating reasoning and answer for reasoning models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When hitting the DeepSeek R1 API at `deepseek-reasoner` ([link](https://api-docs.deepseek.com/guides/reasoning_model)), the API responds with reasoning and the answer in separate aspects of the payload. This enables clients like: - LiteLLM to house reasoning and the answer in separate fields ([link](https://docs.litellm.ai/docs/providers/deepseek)). - OpenRouter's `include_reasoning` opt-in parameter ([link](https://openrouter.ai/docs/parameters#include-reasoning)). It would be really useful if `vllm serve` had some capability for this. ### Alternatives Manually post-processing a response is error prone and arduous. It's better to do it within the model serving code. ### Additional context [DeepSeek R1 model on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-R1) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: include-reasoning)). It would be really useful if `vllm serve` had some capability for this. ### Alternatives Manually post-processing a response is error prone and arduous. It's better to do it within the model serving...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: separating reasoning and answer for reasoning models feature request ### 🚀 The feature, motivation and pitch When hitting the DeepSeek R1 API at `deepseek-reasoner` ([link](https://api-docs.deepseek.com/guide...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ion and pitch When hitting the DeepSeek R1 API at `deepseek-reasoner` ([link](https://api-docs.deepseek.com/guides/reasoning_model)), the API responds with reasoning and the answer in separate aspects of the payload. Th...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: fields ([link](https://docs.litellm.ai/docs/providers/deepseek)). - OpenRouter's `include_reasoning` opt-in parameter ([link](https://openrouter.ai/docs/parameters#include-reasoning)). It would be really useful if `vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: separating reasoning and answer for reasoning models feature request ### 🚀 The feature, motivation and pitch When hitting the DeepSeek R1 API at `deepseek-reasoner` ([link](https://api-docs.deepseek.com/guide...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
