# vllm-project/vllm#17991: [Usage]: Values of logprobs using vllm as external server

| 字段 | 值 |
| --- | --- |
| Issue | [#17991](https://github.com/vllm-project/vllm/issues/17991) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Values of logprobs using vllm as external server

### Issue 正文摘录

### Your current environment - ### How would you like to use vllm Hello 👋 I am currently using the latest stable vllm library to get responses and logprobs of specific tokens. Is it normal to get array filed with almost all zeros when deploying vllm as external service (OpenAI format, both chat formats)? When using the same prompt during offline inference, logprobs seems to be calculated properly. Any ideas how to bypass this? Following question, is there any way to update model's weights (offline mode) during my custom main loop like loading LoRA adapters in `run time` with OpenAI type server? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ed with almost all zeros when deploying vllm as external service (OpenAI format, both chat formats)? When using the same prompt during offline inference, logprobs seems to be calculated properly. Any ideas how to bypass...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: using the latest stable vllm library to get responses and logprobs of specific tokens. Is it normal to get array filed with almost all zeros when deploying vllm as external service (OpenAI format, both chat formats)? Wh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Values of logprobs using vllm as external server usage;stale ### Your current environment - ### How would you like to use vllm Hello 👋 I am currently using the latest stable vllm library to get responses and lo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ### How would you like to use vllm Hello 👋 I am currently using the latest stable vllm library to get responses and logprobs of specific tokens. Is it normal to get array filed with almost all zeros when deploying vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
