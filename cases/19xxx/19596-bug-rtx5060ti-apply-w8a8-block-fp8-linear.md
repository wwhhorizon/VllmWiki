# vllm-project/vllm#19596: [Bug]:rtx5060ti apply_w8a8_block_fp8_linear

| 字段 | 值 |
| --- | --- |
| Issue | [#19596](https://github.com/vllm-project/vllm/issues/19596) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:rtx5060ti apply_w8a8_block_fp8_linear

### Issue 正文摘录

_本地原始数据中没有 issue 正文。_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]:rtx5060ti apply_w8a8_block_fp8_linear bug;stale
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]:rtx5060ti apply_w8a8_block_fp8_linear bug;stale
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]:rtx5060ti apply_w8a8_block_fp8_linear bug;stale
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]:rtx5060ti apply_w8a8_block_fp8_linear bug;stale

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
