# vllm-project/vllm#3667: [Misc]: Prefix caching in the BlockManagerV2

| 字段 | 值 |
| --- | --- |
| Issue | [#3667](https://github.com/vllm-project/vllm/issues/3667) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Prefix caching in the BlockManagerV2

### Issue 正文摘录

Recently, we refactored the block manager subsystem to improve testability by separating concerns of each layer. See https://github.com/vllm-project/vllm/pull/3492 for more information. The following features are missing to support prefix caching: * Eviction policies based on last access time * Eviction policies based on length of prefix (necessary for correctness as our prefix caching attention only supports contiguous prefixes) * Tracking the `computed` bit in prefix caching * E2E correctness test comparing greedy generation equality with prefix caching vs. without prefix caching (see [this test](https://github.com/vllm-project/vllm/blob/321dc1619ad60b6df74fa86ac6299bc83c223996/tests/core/block/e2e/test_correctness.py) for inspiration, which compares greedy generation equality between v1 and v2 block managers) * Performance profiling of v2 + prefix caching For design, https://github.com/vllm-project/vllm/pull/3492 has more details (also feel free to reach out to me). One key is to understand how prefix caching promotion works in the new design: ![image](https://github.com/vllm-project/vllm/assets/950914/51003476-6eff-4cf2-8e89-ea473a56e6a0)

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Misc]: Prefix caching in the BlockManagerV2 Recently, we refactored the block manager subsystem to improve testability by separating concerns of each layer. See https://github.com/vllm-project/vllm/pull/3492 for more i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ManagerV2 Recently, we refactored the block manager subsystem to improve testability by separating concerns of each layer. See https://github.com/vllm-project/vllm/pull/3492 for more information. The following features...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: following features are missing to support prefix caching: * Eviction policies based on last access time * Eviction policies based on length of prefix (necessary for correctness as our prefix caching attention only suppo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ach layer. See https://github.com/vllm-project/vllm/pull/3492 for more information. The following features are missing to support prefix caching: * Eviction policies based on last access time * Eviction policies based o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
