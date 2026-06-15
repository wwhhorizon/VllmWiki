# vllm-project/vllm#10774: [Feature]: Unblock LLM while handling long sequences / Handling multiple prefills at the same time

| 字段 | 值 |
| --- | --- |
| Issue | [#10774](https://github.com/vllm-project/vllm/issues/10774) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Unblock LLM while handling long sequences / Handling multiple prefills at the same time

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Motivation If an engine is currently handling a single long sequence in the prefill stage any other incoming sequence has to wait untill the LLM is done with the long one before it gets to be handled. This means that in a situation with multiple users it can easily happen that a single user's ill-conceived (or simply long) request makes the LLM unresponsive for all other users. ## Initial ideas There are a couple of ways one can currently approach this. - Simply accepting this fact. We do first come first serve and people have to wait. - Upscale the LLM and host multiple replicas or scale a single replica over multiple GPUs to alleviate this a little bit. - Use priority scheduling and give longer requests lower priority However, most of these ideas either come with their own problems and/or don't actually solve the problem. ## Suggestion I don't know of any approach that would work without chunked prefill. However, if we do do chunked prefill the following approach could work: - Introduce a new parameter to the engine `min_num_concurrent_sequences` (with default set to 1 which is just the current behaviour) - While scheduling, first sched...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Unblock LLM while handling long sequences / Handling multiple prefills at the same time feature request;stale ### 🚀 The feature, motivation and pitch ## Motivation If an engine is currently handling a single...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Feature]: Unblock LLM while handling long sequences / Handling multiple prefills at the same time feature request;stale ### 🚀 The feature, motivation and pitch ## Motivation If an engine is currently handling a single...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ing this fact. We do first come first serve and people have to wait. - Upscale the LLM and host multiple replicas or scale a single replica over multiple GPUs to alleviate this a little bit. - Use priority scheduling an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: me. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
