# vllm-project/vllm#14277: [Misc]: running multiple vLLM instances on a single ray cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#14277](https://github.com/vllm-project/vllm/issues/14277) |
| 状态 | closed |
| 标签 | ray;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: running multiple vLLM instances on a single ray cluster

### Issue 正文摘录

### Anything you want to discuss about vllm. When running the vLLM OpenAI server on a Ray cluster(with nodes A/B/C/D), I want to specify particular nodes(e.g., node A and B) for deployment, enabling better control over multiple vLLM instances within a single Ray cluster. Currently, it seems that Ray integration appears limited to specifying tp and pp. Is supporting custom placement group a feasible option? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he vLLM OpenAI server on a Ray cluster(with nodes A/B/C/D), I want to specify particular nodes(e.g., node A and B) for deployment, enabling better control over multiple vLLM instances within a single Ray cluster. Curren...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: running multiple vLLM instances on a single ray cluster ray;stale ### Anything you want to discuss about vllm. When running the vLLM OpenAI server on a Ray cluster(with nodes A/B/C/D), I want to specify particul...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
