# vllm-project/vllm#28042: [Bug]: RotaryEmbedding forward_native cannot match as expected for QKNormRoPEFusionPass

| 字段 | 值 |
| --- | --- |
| Issue | [#28042](https://github.com/vllm-project/vllm/issues/28042) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RotaryEmbedding forward_native cannot match as expected for QKNormRoPEFusionPass

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description I'm working on the fusion pass for QK Normalization and RoPE (as part of PR #27165), and I've hit a tricky pattern-matching issue. The fusion works correctly **only when RoPE is registered as a custom op**. When RoPE uses the native (PyTorch) forward implementation, the pattern fails to match—even if RMSNorm is a custom op. ### Observed Behavior | RMSNorm | RoPE | Pattern Match? | |-------------|-------------|----------------| | custom | custom | ✅ Yes | | native | custom | ✅ Yes | | custom | native | ❌ No | | native | native | ❌ No | ### Example Dump Pattern #### ✅ Working case: RMSNorm custom + RoPE custom (pattern_0) ``` # rms_norm custom, rope custom def pattern_0(): empty_memory_format = CallFunction(aten.empty.memory_format, Ignored(), dtype=Ignored(), layout=torch.strided, device=Ignored(), pin_memory=False) permute_default = CallFunction(aten.permute.default, empty_memory_format, Ignored()) split_with_sizes_default = CallFunction(aten.split_with_sizes.default, KeywordArg('qkv'), Ignored(), Ignored(), _users=3) operator_getitem = CallFunction(operator.getitem, split_with_sizes_default, 0) reshape_default =...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: mat = CallFunction(aten.empty.memory_format, Ignored(), dtype=Ignored(), layout=torch.strided, device=Ignored(), pin_memory=False) permute_default = CallFunction(aten.permute.default, empty_memory_format, Ignored()) spl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: alls as seen when RoPE is a custom op. This unusual nesting may cause mismatches in metadata such as _users. If the traced graph structure deviates significantly from the actual forward computation order, the pattern ma...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: calls as seen when RoPE is a custom op. This unusual nesting may cause mismatches in metadata such as _users. If the traced graph structure deviates significantly from the actual forward computation order, the pattern m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: empty_memory_format = CallFunction(aten.empty.memory_format, Ignored(), dtype=Ignored(), layout=torch.strided, device=Ignored(), pin_memory=False) permute_default = CallFunction(aten.permute.default, empty_memory_format...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _0) ``` # rms_norm custom, rope custom def pattern_0(): empty_memory_format = CallFunction(aten.empty.memory_format, Ignored(), dtype=Ignored(), layout=torch.strided, device=Ignored(), pin_memory=False) permute_default...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
