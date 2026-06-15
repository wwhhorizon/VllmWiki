# vllm-project/vllm#687: vllm doesn't work on long_context?

| 字段 | 值 |
| --- | --- |
| Issue | [#687](https://github.com/vllm-project/vllm/issues/687) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm doesn't work on long_context?

### Issue 正文摘录

thanks a lot for your extraordinary work! when i use vllm to test long-text , i see a warning happened: `Input prompt (15681 tokens) is too long and exceeds limit of 2560` so vllm doesn't work on long_context? is there a special reason?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ceeds limit of 2560` so vllm doesn't work on long_context? is there a special reason?
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ng_context? thanks a lot for your extraordinary work! when i use vllm to test long-text , i see a warning happened: `Input prompt (15681 tokens) is too long and exceeds limit of 2560` so vllm doesn't work on long_contex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
