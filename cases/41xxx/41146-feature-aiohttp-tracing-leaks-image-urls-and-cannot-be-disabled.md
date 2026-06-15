# vllm-project/vllm#41146: [Feature]: aiohttp tracing leaks image urls and cannot be disabled

| 字段 | 值 |
| --- | --- |
| Issue | [#41146](https://github.com/vllm-project/vllm/issues/41146) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: aiohttp tracing leaks image urls and cannot be disabled

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This code creates opentelemetry spans with URLs in those, which might have sensitive info: https://github.com/vllm-project/vllm/blob/de3da0b97cd9db8b1d429312992a5759c89ef881/vllm/multimodal/utils.py#L284 aiohttp support sanitizing it https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/util/opentelemetry-util-http/src/opentelemetry/util/http/__init__.py#L338 But there is no way to configure it from the vLLM: https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/instrumentation/opentelemetry-instrumentation-aiohttp-client/src/opentelemetry/instrumentation/aiohttp_client/__init__.py#L484 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: com/vllm-project/vllm/blob/de3da0b97cd9db8b1d429312992a5759c89ef881/vllm/multimodal/utils.py#L284 aiohttp support sanitizing it https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/util/opentelemetry...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: aiohttp tracing leaks image urls and cannot be disabled feature request ### 🚀 The feature, motivation and pitch This code creates opentelemetry spans with URLs in those, which might have sensitive info: https...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eature]: aiohttp tracing leaks image urls and cannot be disabled feature request ### 🚀 The feature, motivation and pitch This code creates opentelemetry spans with URLs in those, which might have sensitive info: https:/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
