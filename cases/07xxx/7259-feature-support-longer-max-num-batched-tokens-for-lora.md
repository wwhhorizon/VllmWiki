# vllm-project/vllm#7259: [Feature]: support longer max_num_batched_tokens for lora

| 字段 | 值 |
| --- | --- |
| Issue | [#7259](https://github.com/vllm-project/vllm/issues/7259) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support longer max_num_batched_tokens for lora

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Support longer max_num_batched_tokens for lora to free long context ablitity of many models have long context such as qwen2(128k). ### Alternatives _No response_ ### Additional context https://github.com/vllm-project/vllm/blob/main/vllm/config.py#L1379-L1386

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r max_num_batched_tokens for lora to free long context ablitity of many models have long context such as qwen2(128k). ### Alternatives _No response_ ### Additional context https://github.com/vllm-project/vllm/blob/main/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: support longer max_num_batched_tokens for lora feature request ### 🚀 The feature, motivation and pitch Support longer max_num_batched_tokens for lora to free long context ablitity of many models have long con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
