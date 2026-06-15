# vllm-project/vllm#26014: [Bug]: Bugs in the new logprobs_mode

| 字段 | 值 |
| --- | --- |
| Issue | [#26014](https://github.com/vllm-project/vllm/issues/26014) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Bugs in the new logprobs_mode

### Issue 正文摘录

### 🐛 Describe the bug The new logprobs_mode has many bugs. When set to logprobs_mode = 'processed_logprobs', it returns the same values as logprobs_mode = 'raw_logprobs'. Additionally, when set to 'processed_logits' or 'raw_logits', it does not produce any meaningful output the logprobs are all -inf except for rank = 1, which gives 0. I am using MODEL_ID = "Qwen/Qwen3-30B-A3B-Thinking-2507-FP8"

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the logprobs are all -inf except for rank = 1, which gives 0. I am using MODEL_ID = "Qwen/Qwen3-30B-A3B-Thinking-2507-FP8"
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: , which gives 0. I am using MODEL_ID = "Qwen/Qwen3-30B-A3B-Thinking-2507-FP8"
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Bugs in the new logprobs_mode bug;stale ### 🐛 Describe the bug The new logprobs_mode has many bugs. When set to logprobs_mode = 'processed_logprobs', it returns the same values as logprobs_mode = 'raw_logprobs'....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
