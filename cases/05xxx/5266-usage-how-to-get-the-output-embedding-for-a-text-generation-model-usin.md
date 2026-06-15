# vllm-project/vllm#5266: [Usage]:how to get the output embedding for a text generation model using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#5266](https://github.com/vllm-project/vllm/issues/5266) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:how to get the output embedding for a text generation model using vllm

### Issue 正文摘录

### Your current environment Referring to the issue #5181 "The Offline Inference Embedding Example Fails", the method LLM.encode() can only work for embedding models. Is there any idea to get the output embedding for a text generation model("XXXForCausalLM" in model config) using vllm? ### How would you like to use vllm I want to get the output embedding for a text generation model("XXXForCausalLM" in model config) . I don't know how to integrate it with vllm.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]:how to get the output embedding for a text generation model using vllm usage;stale ### Your current environment Referring to the issue #5181 "The Offline Inference Embedding Example Fails", the method LLM.encode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: to get the output embedding for a text generation model using vllm usage;stale ### Your current environment Referring to the issue #5181 "The Offline Inference Embedding Example Fails", the method LLM.encode() can only...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
