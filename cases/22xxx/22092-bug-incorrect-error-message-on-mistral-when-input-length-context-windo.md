# vllm-project/vllm#22092: [Bug]: Incorrect error message on Mistral when input length > context window

| 字段 | 值 |
| --- | --- |
| Issue | [#22092](https://github.com/vllm-project/vllm/issues/22092) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incorrect error message on Mistral when input length > context window

### Issue 正文摘录

### Your current environment v0.9.2 Docker container running `mistralai/Mistral-Small-3.1-24B-Instruct-2503` ### 🐛 Describe the bug There is an error message which is provided when the input length is longer than the model's max length. That error message usually is: > {'object': 'error', 'message': "This model's maximum context length is 131072 tokens. However, you requested 671051 tokens (670951 in the messages, 100 in the completion). Please reduce the length of the messages or completion. None", 'type': 'BadRequestError', 'param': None, 'code': 400} However, when using `mistralai/Mistral-Small-3.1-24B-Instruct-2503` on v0.9.2, the error message is different and nonsensical: > {'object': 'error', 'message': 'max_tokens must be at least 1, got -563072.', 'type': 'BadRequestError', 'param': None, 'code': 400} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: current environment v0.9.2 Docker container running `mistralai/Mistral-Small-3.1-24B-Instruct-2503` ### 🐛 Describe the bug There is an error message which is provided when the input length is longer than the model's max...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ncorrect error message on Mistral when input length > context window bug;stale ### Your current environment v0.9.2 Docker container running `mistralai/Mistral-Small-3.1-24B-Instruct-2503` ### 🐛 Describe the bug There is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t length > context window bug;stale ### Your current environment v0.9.2 Docker container running `mistralai/Mistral-Small-3.1-24B-Instruct-2503` ### 🐛 Describe the bug There is an error message which is provided when th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: error message which is provided when the input length is longer than the model's max length. That error message usually is: > {'object': 'error', 'message': "This model's maximum context length is 131072 tokens. However...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
