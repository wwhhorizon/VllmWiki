# vllm-project/vllm#19902: [Feature]: `kv_transfer_params` not returned for multiple subrequests

| 字段 | 值 |
| --- | --- |
| Issue | [#19902](https://github.com/vllm-project/vllm/issues/19902) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: `kv_transfer_params` not returned for multiple subrequests

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, when handling HTTP requests with multiple subrequests, the response only includes `kv_transfer_params` for one subrequest, making it impossible to access KV transfer information for other subrequests. Related PR: #17751 Reference code: https://github.com/vllm-project/vllm/blob/e384f2f10824df7789c6da35256cf957788c0208/vllm/entrypoints/openai/serving_completion.py#L514-L520 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: `kv_transfer_params` not returned for multiple subrequests feature request;stale ### 🚀 The feature, motivation and pitch Currently, when handling HTTP requests with multiple subrequests, the response only inc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: params` for one subrequest, making it impossible to access KV transfer information for other subrequests. Related PR: #17751 Reference code: https://github.com/vllm-project/vllm/blob/e384f2f10824df7789c6da35256cf957788c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
