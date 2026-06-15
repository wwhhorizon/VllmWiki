# vllm-project/vllm#9479: [Feature]: supporting MllamaForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#9479](https://github.com/vllm-project/vllm/issues/9479) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: supporting MllamaForCausalLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch `MllamaForConditionalGeneration` models (such as, `meta-llama/Llama-3.2-90B-Vision-Instruct`, `meta-llama/Llama-3.2-11B-Vision`, etc.) are composed of `MllamaVisionModel` and`MllamaForCausalLM`. I want to use only `MllamaForCausualLM` and this for, i can load model using code below. ```python from transformers import AutoModelForCausalLM model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-11B-Vision-Instruct") ``` But at vllm, this feature is not supported. Is it possible to support these new function for `MllamaForCausalLM` for people like me who want to use only the text layer part of the `MllamaForConditionalGeneration` model, without using the vision layer? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: supporting MllamaForCausalLM feature request ### 🚀 The feature, motivation and pitch `MllamaForConditionalGeneration` models (such as, `meta-llama/Llama-3.2-90B-Vision-Instruct`, `meta-llama/Llama-3.2-11B-Vis...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: this for, i can load model using code below. ```python from transformers import AutoModelForCausalLM model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-11B-Vision-Instruct") ``` But at vllm, this feature...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: supporting MllamaForCausalLM feature request ### 🚀 The feature, motivation and pitch `MllamaForConditionalGeneration` models (such as, `meta-llama/Llama-3.2-90B-Vision-Instruct`, `meta-llama/Llama-3.2-11B-Vis...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
