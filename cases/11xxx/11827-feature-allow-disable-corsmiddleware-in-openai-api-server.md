# vllm-project/vllm#11827: [Feature]: allow disable CORSMiddleware in openai api_server

| 字段 | 值 |
| --- | --- |
| Issue | [#11827](https://github.com/vllm-project/vllm/issues/11827) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: allow disable CORSMiddleware in openai api_server

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In some production environments, inference services may be located behind a gateway that may automatically add cross domain related settings. If vllm api server also adds cross domain settings (such as fields in the response header) at this time, it will cause service exceptions. Therefore, I believe there should be a setting to support disabling cross domain middleware. ### Alternatives There are some ways to achieve this feature: 1. add server args such as --disable-cors 2. add related environment variables 3. modify the source code which is not recommend ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: allow disable CORSMiddleware in openai api_server feature request;stale ### 🚀 The feature, motivation and pitch In some production environments, inference services may be located behind a gateway that may aut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: allow disable CORSMiddleware in openai api_server feature request;stale ### 🚀 The feature, motivation and pitch In some production environments, inference services may be located behind a gateway that may aut...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
