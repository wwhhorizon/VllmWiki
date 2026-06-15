# vllm-project/vllm#29563: [Feature]: Improve tokenizer loading when loading GGUF models

| 字段 | 值 |
| --- | --- |
| Issue | [#29563](https://github.com/vllm-project/vllm/issues/29563) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Improve tokenizer loading when loading GGUF models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM requires tokenizer argument to load GGUF models. However, GGUF format also includes tokenizer information. ([GGUF format](https://huggingface.co/docs/transformers/gguf)) I don't know if the tokenizer information in GGUF format is enough, but it would be nice if it could be reviewed ### Alternatives As-Is: `vllm serve --tokenizer ` To-Be: `vllm serve (--tokenizer optional)` ### Additional context _Originally posted by @ivanbaldo in https://github.com/vllm-project/vllm/pull/29137#issuecomment-3582970607 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Improve tokenizer loading when loading GGUF models feature request ### 🚀 The feature, motivation and pitch vLLM requires tokenizer argument to load GGUF models. However, GGUF format also includes tokenizer in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 607 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Improve tokenizer loading when loading GGUF models feature request ### 🚀 The feature, motivation and pitch vLLM requires tokenizer argument to load GGUF models. However, GGUF format also includes tokenizer in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
