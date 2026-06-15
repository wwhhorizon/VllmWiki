# vllm-project/vllm#14080: [Feature]: Prefill responses for greater output control

| 字段 | 值 |
| --- | --- |
| Issue | [#14080](https://github.com/vllm-project/vllm/issues/14080) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Prefill responses for greater output control

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Similar to [Claude's Prefill responses](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response): > When using Claude, you have the unique ability to guide its responses by prefilling the Assistant message. This powerful technique allows you to direct Claude’s actions, skip preambles, enforce specific formats like JSON or XML, and even help Claude maintain character consistency in role-play scenarios. This prefill response feature basically allows us to continue the generation of the assistant message, which is super helpful for multi-turn rollout. ![Image](https://github.com/user-attachments/assets/b3cd29ff-8fa2-4183-9cf5-f4e147b53e07) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Prefill responses for greater output control feature request;stale ### 🚀 The feature, motivation and pitch Similar to [Claude's Prefill responses](https://docs.anthropic.com/en/docs/build-with-claude/prompt-e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: milar to [Claude's Prefill responses](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response): > When using Claude, you have the unique ability to guide its responses by prefill...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: allows you to direct Claude’s actions, skip preambles, enforce specific formats like JSON or XML, and even help Claude maintain character consistency in role-play scenarios. This prefill response feature basically allow...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
