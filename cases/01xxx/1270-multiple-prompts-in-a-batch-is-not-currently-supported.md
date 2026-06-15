# vllm-project/vllm#1270: multiple prompts in a batch is not currently supported

| 字段 | 值 |
| --- | --- |
| Issue | [#1270](https://github.com/vllm-project/vllm/issues/1270) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> multiple prompts in a batch is not currently supported

### Issue 正文摘录

Is this planned? Seems like good idea to support full OpenAI behavior and any batching is already handled well by vLLM, so should be relatively easy I would guess? https://github.com/vllm-project/vllm/blob/acbed3ef40f015fcf64460e629813922fab90380/vllm/entrypoints/openai/api_server.py#L396-L401

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
