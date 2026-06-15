# vllm-project/vllm#19300: [Feature]: Add token-level progress bar for `LLM.beam_search` inference

| 字段 | 值 |
| --- | --- |
| Issue | [#19300](https://github.com/vllm-project/vllm/issues/19300) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add token-level progress bar for `LLM.beam_search` inference

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm working on LLM inference using the [`LLM.beam_search`](https://docs.vllm.ai/en/stable/models/generative_models.html#llmbeam_search) function. One major usability issue I've encountered is the lack of progress visibility during inference. When running beam search, I don’t know how long to wait or how far along the process is, which makes development feel unsafe and unpredictable. A similar request was previously raised https://github.com/vllm-project/vllm/issues/11835#issue-2774761012, but it was closed. However, the need still exists and is especially relevant for anyone using beam search in long sequences or production loops. The beam search logic is currently implemented using a token-level loop, not per-instance logic, as seen in: https://github.com/vllm-project/vllm/blob/ca27f0f9c1452a0e73126be2b1666c3067cf6290/vllm/entrypoints/llm.py#L605 https://github.com/vllm-project/vllm/blob/ca27f0f9c1452a0e73126be2b1666c3067cf6290/vllm/entrypoints/llm.py#L622-L627 Because of this, implementing an instance-level progress bar (like in `LLM.generate` and `LLM.chat`) isn’t straightforward. However, a token-level progress bar would still provide ma...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 2774761012, but it was closed. However, the need still exists and is especially relevant for anyone using beam search in long sequences or production loops. The beam search logic is currently implemented using a token-l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Add token-level progress bar for `LLM.beam_search` inference feature request;stale ### 🚀 The feature, motivation and pitch I'm working on LLM inference using the [`LLM.beam_search`](https://docs.vllm.ai/en/st...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e]: Add token-level progress bar for `LLM.beam_search` inference feature request;stale ### 🚀 The feature, motivation and pitch I'm working on LLM inference using the [`LLM.beam_search`](https://docs.vllm.ai/en/stable/mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: M inference using the [`LLM.beam_search`](https://docs.vllm.ai/en/stable/models/generative_models.html#llmbeam_search) function. One major usability issue I've encountered is the lack of progress visibility during infer...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e in usability and developer confidence is high.** This also helps in CI/testing pipelines where inference time needs to be monitored. ### Before submitting a new issue... - [x] Make sure you already searched for releva...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
