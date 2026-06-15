# vllm-project/vllm#10440: [Bug]: Input prompt (35247 tokens) is too long and exceeds limit of 1000

| 字段 | 值 |
| --- | --- |
| Issue | [#10440](https://github.com/vllm-project/vllm/issues/10440) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Input prompt (35247 tokens) is too long and exceeds limit of 1000

### Issue 正文摘录

I am trying to send a rather long prompt (36k tokens) to VLLM supported models, in particular llama3_8B_Instruct. However I am getting the error below: scheduler.py:648] Input prompt (36893 tokens) is too long and exceeds limit of 1000 How can I fix this? Is 1000 tokens the max context length for llama3_8B_Instruct? Are there any VLLM supported models that accept longer input context windows? Thank you!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: I am trying to send a rather long prompt (36k tokens) to VLLM supported models, in particular llama3_8B_Instruct. However I am getting the error below: scheduler.py:648] Input prompt (36893 tokens) is too long and excee...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: Input prompt (35247 tokens) is too long and exceeds limit of 1000 bug;stale I am trying to send a rather long prompt (36k tokens) to VLLM supported models, in particular llama3_8B_Instruct. However I am getting the e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
