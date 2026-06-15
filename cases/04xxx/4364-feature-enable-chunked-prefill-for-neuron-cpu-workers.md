# vllm-project/vllm#4364: [Feature]: Enable chunked prefill for neuron & cpu workers

| 字段 | 值 |
| --- | --- |
| Issue | [#4364](https://github.com/vllm-project/vllm/issues/4364) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable chunked prefill for neuron & cpu workers

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently these two model runner doesn't support chunked prefill because their input prep code is not compatible. When https://github.com/vllm-project/vllm/pull/4309 is merged, I can point exactly what's needed to support chunked prefill! ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Enable chunked prefill for neuron & cpu workers feature request;stale ### 🚀 The feature, motivation and pitch Currently these two model runner doesn't support chunked prefill because their input prep code is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: quest;stale ### 🚀 The feature, motivation and pitch Currently these two model runner doesn't support chunked prefill because their input prep code is not compatible. When https://github.com/vllm-project/vllm/pull/4309 i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
