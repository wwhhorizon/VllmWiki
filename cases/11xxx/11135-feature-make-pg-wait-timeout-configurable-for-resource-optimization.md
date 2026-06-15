# vllm-project/vllm#11135: [Feature]: Make PG_WAIT_TIMEOUT configurable for resource optimization

| 字段 | 值 |
| --- | --- |
| Issue | [#11135](https://github.com/vllm-project/vllm/issues/11135) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make PG_WAIT_TIMEOUT configurable for resource optimization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In environments where resources are scarce, a shorter timeout may help to quickly release requests for placement groups that could not be successfully created, allowing these resources to be utilized sooner by other tasks or services. Conversely, in environments with abundant resources, a longer timeout could increase the success rate of creating placement groups. Now, PG_WAIT_TIMEOUT is hardcoded and we need to make this configurable to adapt to different environments https://github.com/vllm-project/vllm/blob/85362f028c0324d8d00b0438f29c3d9f64737b9a/vllm/executor/ray_utils.py#L17 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: re]: Make PG_WAIT_TIMEOUT configurable for resource optimization feature request;stale ### 🚀 The feature, motivation and pitch In environments where resources are scarce, a shorter timeout may help to quickly release re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Make PG_WAIT_TIMEOUT configurable for resource optimization feature request;stale ### 🚀 The feature, motivation and pitch In environments where resources are scarce, a shorter timeout may help to quickly rele...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
