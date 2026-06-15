# vllm-project/vllm#895: qwen-7b：maximum context length is 2048 tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#895](https://github.com/vllm-project/vllm/issues/895) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> qwen-7b：maximum context length is 2048 tokens

### Issue 正文摘录

Using the `vllm` method in `fastchat` to start more than 2k contexts results in: `maximum context length is 2048 tokens`, while using the normal service does not have this problem.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: qwen-7b：maximum context length is 2048 tokens Using the `vllm` method in `fastchat` to start more than 2k contexts results in: `maximum context length is 2048 tokens`, while using the normal service does not have this pr

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
