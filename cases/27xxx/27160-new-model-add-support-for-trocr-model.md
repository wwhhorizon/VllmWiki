# vllm-project/vllm#27160: [New Model]: Add support for TrOCR model

| 字段 | 值 |
| --- | --- |
| Issue | [#27160](https://github.com/vllm-project/vllm/issues/27160) |
| 状态 | closed |
| 标签 | new-model;stale;multi-modality |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Add support for TrOCR model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have trained a TrOCR model and would like to deploy it on production with vLLM. However, I have noticed that there is currently no support for this model. ### Alternatives _No response_ ### Additional context The LLM component is quite similar to Bart, so I believe that the implementation would be straightforward. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rd. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: Add support for TrOCR model new-model;stale;multi-modality ### 🚀 The feature, motivation and pitch I have trained a TrOCR model and would like to deploy it on production with vLLM. However, I have noticed t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Add support for TrOCR model new-model;stale;multi-modality ### 🚀 The feature, motivation and pitch I have trained a TrOCR model and would like to deploy it on production with vLLM. However, I have noticed t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
