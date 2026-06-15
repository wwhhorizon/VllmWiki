# vllm-project/vllm#3000: How can I use the Lora Adapter for a model with Vocab size 40960?

| 字段 | 值 |
| --- | --- |
| Issue | [#3000](https://github.com/vllm-project/vllm/issues/3000) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How can I use the Lora Adapter for a model with Vocab size 40960?

### Issue 正文摘录

The error occurs when I call the LLMEngine object. The error below appears. ``` ValueError: When using LoRA, vocab size must be 32000 >= vocab_size <= 33024 ``` Does the method using the Lora Adapter not apply to models that expand the vocab or have a vocab size larger than 32000?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How can I use the Lora Adapter for a model with Vocab size 40960? stale The error occurs when I call the LLMEngine object. The error below appears. ``` ValueError: When using LoRA, vocab size must be 32000 >= vocab_size...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: How can I use the Lora Adapter for a model with Vocab size 40960? stale The error occurs when I call the LLMEngine object. The error below appears. ``` ValueError: When using LoRA, vocab size must be 32000 >= vocab_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
