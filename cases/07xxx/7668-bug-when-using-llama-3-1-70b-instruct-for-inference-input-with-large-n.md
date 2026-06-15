# vllm-project/vllm#7668: [Bug]: when using llama-3.1-70b-instruct for inference, input with large number of tokens(>8k) will result in endless output

| 字段 | 值 |
| --- | --- |
| Issue | [#7668](https://github.com/vllm-project/vllm/issues/7668) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: when using llama-3.1-70b-instruct for inference, input with large number of tokens(>8k) will result in endless output

### Issue 正文摘录

### Your current environment vllm 0.5.4 ### 🐛 Describe the bug when using llama-3.1-70b-instruct for inference, input with large number of tokens(>8k) will result in endless output. The output text is a continuous repetition of a piece of text, and the output will not stop until the limit of max_tokens is reached.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: when using llama-3.1-70b-instruct for inference, input with large number of tokens(>8k) will result in endless output bug;stale ### Your current environment vllm 0.5.4 ### 🐛 Describe the bug when using llama-3.1-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: input with large number of tokens(>8k) will result in endless output bug;stale ### Your current environment vllm 0.5.4 ### 🐛 Describe the bug when using llama-3.1-70b-instruct for inference, input with large number of t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
