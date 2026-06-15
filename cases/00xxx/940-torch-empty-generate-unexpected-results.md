# vllm-project/vllm#940: torch.empty generate unexpected results

| 字段 | 值 |
| --- | --- |
| Issue | [#940](https://github.com/vllm-project/vllm/issues/940) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> torch.empty generate unexpected results

### Issue 正文摘录

I think below torch.empty should change to torch.zeros. https://github.com/vllm-project/vllm/blob/ce741ba3e4fea00bacd2e1c609ca587ec35eb161/vllm/worker/cache_engine.py#L75 https://github.com/vllm-project/vllm/blob/ce741ba3e4fea00bacd2e1c609ca587ec35eb161/vllm/worker/cache_engine.py#L80 As torch.empty return uninitialized data causes an unexpected failure in inference. https://pytorch.org/docs/stable/generated/torch.empty.html

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
