# vllm-project/vllm#375: [Feature] Return attention_map for tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#375](https://github.com/vllm-project/vllm/issues/375) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Return attention_map for tokens

### Issue 正文摘录

@zhuohan123 I have a use case where we utilize the attention map of the tokens in the prompt to decide whether to evict a section from the prompt if it’s running out of context length. It’s relatively easy to do with transformers and PyTorch but it’d be nice to get it from vllm too. I can take a crack at implementing it too.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: case where we utilize the attention map of the tokens in the prompt to decide whether to evict a section from the prompt if it’s running out of context length. It’s relatively easy to do with transformers and PyTorch bu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature] Return attention_map for tokens feature request @zhuohan123 I have a use case where we utilize the attention map of the tokens in the prompt to decide whether to evict a section from the prompt if it’s running...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
