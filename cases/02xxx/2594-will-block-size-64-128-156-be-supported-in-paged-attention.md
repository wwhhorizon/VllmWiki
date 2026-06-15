# vllm-project/vllm#2594: Will block_size 64/128/156 be supported in paged attention?

| 字段 | 值 |
| --- | --- |
| Issue | [#2594](https://github.com/vllm-project/vllm/issues/2594) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Will block_size 64/128/156 be supported in paged attention?

### Issue 正文摘录

When I try to use paged attention. I met `RuntimeError: Unsupported block size: 64`. From source code we can know paged attention does not support block_size = 1/2/4/64/128/256 to reduce the compilation time ([attention_kernels.cu#L663~L664](https://github.com/vllm-project/vllm/blob/2832e7b9f92e2d1dd7dfe37951e5837c61d3db20/csrc/attention/attention_kernels.cu#L663~L664)). So: - Will those block_size numbers be supported in the further? - Or users can instance kernel and compile manually? Will the correctness and performance be guaranteed?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: numbers be supported in the further? - Or users can instance kernel and compile manually? Will the correctness and performance be guaranteed?
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Will block_size 64/128/156 be supported in paged attention? When I try to use paged attention. I met `RuntimeError: Unsupported block size: 64`. From source code we can know paged attention does not support block_size =...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
