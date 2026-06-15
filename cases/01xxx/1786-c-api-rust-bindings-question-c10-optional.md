# vllm-project/vllm#1786: C++ API -> Rust bindings question: `c10::optional`

| 字段 | 值 |
| --- | --- |
| Issue | [#1786](https://github.com/vllm-project/vllm/issues/1786) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> C++ API -> Rust bindings question: `c10::optional`

### Issue 正文摘录

Hello everbody, I am developing a Rust counterpart for `vllm`, [`candle-vllm`](https://github.com/EricLBuehler/candle-vllm`), and do not want to rewrite PagedAttention from scratch. To avoid this, I plan on using Rust bindings for the C++ API: > https://github.com/vllm-project/vllm/blob/7c600440f7560348e571f021f2b2d1469de5264d/csrc/ops.h#L3-L14C9 However, the type `c10::optional` seems to pose a problem when generating the bindings. The Rust `Option ` type is an enum, but the `c10::optional` type [appears to be a class](https://github.com/pytorch/pytorch/blob/main/c10/util/Optional.h). How can I convert this type to its Rust counterpart? I would appreciate any help!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: al.h). How can I convert this type to its Rust counterpart? I would appreciate any help!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
