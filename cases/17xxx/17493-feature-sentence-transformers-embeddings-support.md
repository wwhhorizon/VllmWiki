# vllm-project/vllm#17493: [Feature]: Sentence transformers embeddings support

| 字段 | 值 |
| --- | --- |
| Issue | [#17493](https://github.com/vllm-project/vllm/issues/17493) |
| 状态 | open |
| 标签 | feature request;keep-open |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Sentence transformers embeddings support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Several embedding models are starting to use Sentence Transformers, for example all-mpnet-base-v2, roberta-base-squad2, and distilbert-base-cased-distilled-squad. None of these models work in vLLM today so we would like to propose adding in the functionality to support this extra class of models. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: est;keep-open ### 🚀 The feature, motivation and pitch Several embedding models are starting to use Sentence Transformers, for example all-mpnet-base-v2, roberta-base-squad2, and distilbert-base-cased-distilled-squad. No...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Sentence transformers embeddings support feature request;keep-open ### 🚀 The feature, motivation and pitch Several embedding models are starting to use Sentence Transformers, for example all-mpnet-base-v2, ro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
