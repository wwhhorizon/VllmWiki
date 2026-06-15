# vllm-project/vllm#12910: [Feature]: Add logits for classification task

| 字段 | 值 |
| --- | --- |
| Issue | [#12910](https://github.com/vllm-project/vllm/issues/12910) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add logits for classification task

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I noticed that for models with only single class output of true/false (e.g. [RankLLaMA](https://huggingface.co/castorini/rankllama-v1-7b-lora-passagehttps://huggingface.co/castorini/rankllama-v1-7b-lora-passage)) because it only one class output everything from vLLM is marked as true, even though the logit may be below zero. I don't see how to change how this functions in the code, so it would be great to get the logits so that this could be done by the user. ### Alternatives You could provide a threshold value or something for classification for single-class prediction outputs as well. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ture request ### 🚀 The feature, motivation and pitch I noticed that for models with only single class output of true/false (e.g. [RankLLaMA](https://huggingface.co/castorini/rankllama-v1-7b-lora-passagehttps://huggingfa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: pitch I noticed that for models with only single class output of true/false (e.g. [RankLLaMA](https://huggingface.co/castorini/rankllama-v1-7b-lora-passagehttps://huggingface.co/castorini/rankllama-v1-7b-lora-passage))...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add logits for classification task feature request ### 🚀 The feature, motivation and pitch I noticed that for models with only single class output of true/false (e.g. [RankLLaMA](https://huggingface.co/castor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
