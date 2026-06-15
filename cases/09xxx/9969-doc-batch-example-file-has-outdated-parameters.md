# vllm-project/vllm#9969: [Doc]: batch example file has outdated parameters

| 字段 | 值 |
| --- | --- |
| Issue | [#9969](https://github.com/vllm-project/vllm/issues/9969) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: batch example file has outdated parameters

### Issue 正文摘录

### 📚 The doc issue in examples/offline_inference_openai.md, the linked examples/openai_example_batch.jsonl uses max_completion_tokens instead of max_tokens, causing an error when the example is run. ### Suggest a potential alternative/fix PR incoming ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ;stale ### 📚 The doc issue in examples/offline_inference_openai.md, the linked examples/openai_example_batch.jsonl uses max_completion_tokens instead of max_tokens, causing an error when the example is run. ### Suggest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ing ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: batch example file has outdated parameters documentation;stale ### 📚 The doc issue in examples/offline_inference_openai.md, the linked examples/openai_example_batch.jsonl uses max_completion_tokens instead of max...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
