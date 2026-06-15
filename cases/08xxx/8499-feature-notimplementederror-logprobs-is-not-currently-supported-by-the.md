# vllm-project/vllm#8499: [Feature]: NotImplementedError: logprobs is not currently supported by the TPU backend

| 字段 | 值 |
| --- | --- |
| Issue | [#8499](https://github.com/vllm-project/vllm/issues/8499) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: NotImplementedError: logprobs is not currently supported by the TPU backend

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello, is there a plan to support logprobs on TPUs with vLLM? We currently cannot run `lm-eval-harness` for certain evals that require logprobs. https://github.com/vllm-project/vllm/blob/main/vllm/worker/tpu_model_runner.py#L459 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tedError: logprobs is not currently supported by the TPU backend feature request;stale ### 🚀 The feature, motivation and pitch Hello, is there a plan to support logprobs on TPUs with vLLM? We currently cannot run `lm-ev...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: plan to support logprobs on TPUs with vLLM? We currently cannot run `lm-eval-harness` for certain evals that require logprobs. https://github.com/vllm-project/vllm/blob/main/vllm/worker/tpu_model_runner.py#L459 ### Alte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: re]: NotImplementedError: logprobs is not currently supported by the TPU backend feature request;stale ### 🚀 The feature, motivation and pitch Hello, is there a plan to support logprobs on TPUs with vLLM? We currently c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ogprobs. https://github.com/vllm-project/vllm/blob/main/vllm/worker/tpu_model_runner.py#L459 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
