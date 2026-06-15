# vllm-project/vllm#11360: [Feature]: meta-llama/Prompt-Guard-86M Usage Value Error.

| 字段 | 值 |
| --- | --- |
| Issue | [#11360](https://github.com/vllm-project/vllm/issues/11360) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: meta-llama/Prompt-Guard-86M Usage Value Error.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Model architectures ['DebertaV2ForSequenceClassification'] are not supported for now. Here is how I try to load the model: model_id_prompt_guard = "/path/to/model/Prompt-Guard-86M" tokenizer_prompt_guard = AutoTokenizer.from_pretrained(model_id_prompt_guard) prompt_guard_model = LLM(model=model_id_prompt_guard, gpu_memory_utilization=0.1, max_model_len=256) I want to use this model in my pipeline, meta-llama/Prompt-Guard-86M. I got the aformentioned error. Can you guys know how to manually add or are you planning to add this one? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: meta-llama/Prompt-Guard-86M Usage Value Error. feature request;stale ### 🚀 The feature, motivation and pitch Model architectures ['DebertaV2ForSequenceClassification'] are not supported for now. Here is how I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: meta-llama/Prompt-Guard-86M Usage Value Error. feature request;stale ### 🚀 The feature, motivation and pitch Model architectures ['DebertaV2ForSequenceClassification'] are not supported for now. Here is how I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or. feature request;stale ### 🚀 The feature, motivation and pitch Model architectures ['DebertaV2ForSequenceClassification'] are not supported for now. Here is how I try to load the model: model_id_prompt_guard = "/path...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
