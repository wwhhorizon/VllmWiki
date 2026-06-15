# vllm-project/vllm#10172: [Feature]: BASE_URL environment variable

| 字段 | 值 |
| --- | --- |
| Issue | [#10172](https://github.com/vllm-project/vllm/issues/10172) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: BASE_URL environment variable

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It would be nice to be able to add a base path env to chat completions to reduce some of the need for a reverse proxy. IE VLLM_BASE_PATH="/my-deployment" and then the service would be able to be access at https://localhost/my-deployment/v1 ### Alternatives Reverse Proxy has been brought up a few times. This would be a small enough add and bring enough quality of life to it I think it could be helpful. ### Additional context Happy to put in a PR ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rnatives Reverse Proxy has been brought up a few times. This would be a small enough add and bring enough quality of life to it I think it could be helpful. ### Additional context Happy to put in a PR ### Before submitt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: BASE_URL environment variable feature request;stale ### 🚀 The feature, motivation and pitch It would be nice to be able to add a base path env to chat completions to reduce some of the need for a reverse prox...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
