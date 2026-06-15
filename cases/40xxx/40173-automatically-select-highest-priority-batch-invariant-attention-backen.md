# vllm-project/vllm#40173: Automatically select highest priority batch-invariant attention backend

| 字段 | 值 |
| --- | --- |
| Issue | [#40173](https://github.com/vllm-project/vllm/issues/40173) |
| 状态 | closed |
| 标签 | help wanted;good first issue |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Automatically select highest priority batch-invariant attention backend

### Issue 正文摘录

By default, attention backends are selected according to the attention backend priority list. This can be overriden using `--attention-backend` (and equivalent CLI/Python flags). However, if batch invariance is enabled (`VLLM_BATCH_INVARIANT=1`), the batch invariant init requires an explicit selection. If nothing is specified, it produces the following error: ``` RuntimeError: VLLM batch_invariant mode requires an attention backend in ['FLASH_ATTN', 'TRITON_ATTN', 'FLASH_ATTN_MLA', 'TRITON_MLA'], but got 'None'. Please use --attention-backend or ``` Instead, the attention backend selector should be aware of batch-invariance, and select the highest priority backend that supports batch invariance. This will likely require adding a `supports_batch_invariance` to the `AttentionBackend` class so the selector can query it. Reviewers: @yewentao256 @MatthewBonanni

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Automatically select highest priority batch-invariant attention backend help wanted;good first issue By default, attention backends are selected according to the attention backend priority list. This can be overriden us...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ing `--attention-backend` (and equivalent CLI/Python flags). However, if batch invariance is enabled (`VLLM_BATCH_INVARIANT=1`), the batch invariant init requires an explicit selection. If nothing is specified, it produ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed (`VLLM_BATCH_INVARIANT=1`), the batch invariant init requires an explicit selection. If nothing is specified, it produces the following error: ``` RuntimeError: VLLM batch_invariant mode requires an attention backend...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
