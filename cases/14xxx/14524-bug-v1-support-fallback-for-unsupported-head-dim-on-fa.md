# vllm-project/vllm#14524: [Bug]: [V1] Support Fallback For Unsupported Head Dim on FA

| 字段 | 值 |
| --- | --- |
| Issue | [#14524](https://github.com/vllm-project/vllm/issues/14524) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [V1] Support Fallback For Unsupported Head Dim on FA

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Currently, if a model has an unsupported head_dim (e.g. `microsoft/phi-2`, which has `head_dim=80`), we raise a `ValueError`. Options: - Once we support Triton backend on V0, fall back - Try to detect this at startup time and fall back to V0. The challenge with this is that the `head_dim` is not resolved until we get to the model architecture, which is too late ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: [V1] Support Fallback For Unsupported Head Dim on FA bug;stale ### Your current environment ### 🐛 Describe the bug Currently, if a model has an unsupported head_dim (e.g. `microsoft/phi-2`, which has `head_dim=80...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: th this is that the `head_dim` is not resolved until we get to the model architecture, which is too late ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatb...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ### Your current environment ### 🐛 Describe the bug Currently, if a model has an unsupported head_dim (e.g. `microsoft/phi-2`, which has `head_dim=80`), we raise a `ValueError`. Options: - Once we support Triton backend...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: [V1] Support Fallback For Unsupported Head Dim on FA bug;stale ### Your current environment ### 🐛 Describe the bug Currently, if a model has an unsupported head_dim (e.g. `microsoft/phi-2`, which has `head_dim=80...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
