# vllm-project/vllm#36308: [Feature]: Include kv_transfer_params in Streaming Responses to optimize TTFT in P/D Disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#36308](https://github.com/vllm-project/vllm/issues/36308) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Include kv_transfer_params in Streaming Responses to optimize TTFT in P/D Disaggregation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Current Problem**: In Prefill/Decode disaggregation, `kv_transfer_params` are only available in non-streaming responses, preventing streaming of the first token generated during prefill. **Proposed Solution**: Add `kv_transfer_params` field to `ChatCompletionStreamResponse` and populate it in the first streaming chunk (that has the first token generated) when KV transfer is configured. **Benefits**: - Enables streaming prefill in P/D disaggregation - Reduces TTFT by parallelizing first token send to User + KV transfer to Decode - Maintains compatibility (optional field, only set for P/D)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ms in Streaming Responses to optimize TTFT in P/D Disaggregation feature request ### 🚀 The feature, motivation and pitch **Current Problem**: In Prefill/Decode disaggregation, `kv_transfer_params` are only available in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: streaming chunk (that has the first token generated) when KV transfer is configured. **Benefits**: - Enables streaming prefill in P/D disaggregation - Reduces TTFT by parallelizing first token send to User + KV transfer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
