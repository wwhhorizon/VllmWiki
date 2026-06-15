# vllm-project/vllm#117: Do not initialize process group when using a single GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#117](https://github.com/vllm-project/vllm/issues/117) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Do not initialize process group when using a single GPU

### Issue 正文摘录

Currently we call `torch.distributed.init_process_group` even for a single GPU. This is redundant and causes errors when the LLM object is created multiple times.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
