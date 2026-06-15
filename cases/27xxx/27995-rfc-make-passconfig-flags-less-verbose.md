# vllm-project/vllm#27995: [RFC]: Make PassConfig flags less verbose

| 字段 | 值 |
| --- | --- |
| Issue | [#27995](https://github.com/vllm-project/vllm/issues/27995) |
| 状态 | closed |
| 标签 | help wanted;good first issue;RFC;torch.compile |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Make PassConfig flags less verbose

### Issue 正文摘录

### Motivation. Almost all `PassConfig` field names have `enable_` in the name, which is unnecessarily verbose. They are also pretty long, and sometimes not descriptive enough. Finally, `enable_fusion` should be split into rmsnorm+quant and activation+quant flags as we want to control these flags separately. ### Proposed Change. We should rename the flags: - `enable_async_tp` -> `fuse_gemm_comms` - `enable_attn_fusion` -> `fuse_attn_quant` - `enable_fi_allreduce_fusion` -> `fuse_allreduce_rms` - `enable_fusion` -> `fuse_norm_quant`, `fuse_act_quant` - `enable_noop` -> `eliminate_noops` - `enable_sequence_parallelism` -> `enable_sp` For future RoPE-based fusion passes, the flags will look like: - `enable_qknorm_rope_fusion` -> `fuse_qknorm_rope` - `enable_rope_cache_fusion` -> `fuse_rope_cache` - ... We can deprecate the original flags in the next release and map them to the new ones, and remove them 1 or even 2 releases later (shouldn't be hard to support). These flags will be used less commonly after `-O` optimization levels land anyway. ### Feedback Period. 1 week, 11/3 - 11/7 ### CC List. @zou3519 @youkaichao @mgoin @ilmarkov @nvpohanh @pavanimajety ### Any Other Things. With p...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _quant` - `enable_noop` -> `eliminate_noops` - `enable_sequence_parallelism` -> `enable_sp` For future RoPE-based fusion passes, the flags will look like: - `enable_qknorm_rope_fusion` -> `fuse_qknorm_rope` - `enable_ro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ake PassConfig flags less verbose help wanted;good first issue;RFC;torch.compile ### Motivation. Almost all `PassConfig` field names have `enable_` in the name, which is unnecessarily verbose. They are also pretty long,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: escriptive enough. Finally, `enable_fusion` should be split into rmsnorm+quant and activation+quant flags as we want to control these flags separately. ### Proposed Change. We should rename the flags: - `enable_async_tp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [RFC]: Make PassConfig flags less verbose help wanted;good first issue;RFC;torch.compile ### Motivation. Almost all `PassConfig` field names have `enable_` in the name, which is unnecessarily verbose. They are also pret...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: oposed Change. We should rename the flags: - `enable_async_tp` -> `fuse_gemm_comms` - `enable_attn_fusion` -> `fuse_attn_quant` - `enable_fi_allreduce_fusion` -> `fuse_allreduce_rms` - `enable_fusion` -> `fuse_norm_quan...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
