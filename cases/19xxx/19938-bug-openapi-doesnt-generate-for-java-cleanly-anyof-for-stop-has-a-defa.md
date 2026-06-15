# vllm-project/vllm#19938: [Bug]: openapi doesnt generate for Java cleanly AnyOf for Stop has a default value

| 字段 | 值 |
| --- | --- |
| Issue | [#19938](https://github.com/vllm-project/vllm/issues/19938) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: openapi doesnt generate for Java cleanly AnyOf for Stop has a default value

### Issue 正文摘录

### Your current environment OpenJDK 25, target java 17 org.openapitools. openapi-generator-maven-plugin, 7.13.0 ### 🐛 Describe the bug The Any of for the Stop class has a default value of [] Swagger generates private Stop stop = [] But in java Objects can not have a default value of [] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: doesnt generate for Java cleanly AnyOf for Stop has a default value bug;stale ### Your current environment OpenJDK 25, target java 17 org.openapitools. openapi-generator-maven-plugin, 7.13.0 ### 🐛 Describe the bug The A...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
