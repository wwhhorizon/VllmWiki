# vllm-project/vllm#2675: Tmp Directory Locked

| 字段 | 值 |
| --- | --- |
| Issue | [#2675](https://github.com/vllm-project/vllm/issues/2675) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Tmp Directory Locked

### Issue 正文摘录

When multiple users are using vLLM on the same machine, we get the following permission denied error regarding a .lock file ``` Permission denied: '/tmp/meta-llama-Llama-2-70b-chat-hf.lock ``` This was also mentioned in #2232 and #2179.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on denied error regarding a .lock file ``` Permission denied: '/tmp/meta-llama-Llama-2-70b-chat-hf.lock ``` This was also mentioned in #2232 and #2179.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
