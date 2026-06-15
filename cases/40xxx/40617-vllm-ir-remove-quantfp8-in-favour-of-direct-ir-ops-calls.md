# vllm-project/vllm#40617: [vllm IR]: Remove `QuantFP8` in favour of direct `ir.ops` calls

| 字段 | 值 |
| --- | --- |
| Issue | [#40617](https://github.com/vllm-project/vllm/issues/40617) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [vllm IR]: Remove `QuantFP8` in favour of direct `ir.ops` calls

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description `QuantFP8` is a `CustomOp` whose `forward_native` already delegates, almost, entirely to IR ops (`ir.ops.dynamic_group_quant_fp81, `ir.ops.dynamic_quant_fp8`, `ir.ops.static_quant_fp8`, `ir.ops.static_group_quant_fp8`). The IR ops handle platform dispatch internally, making the `CustomOp` abstraction redundant. ### Proposed change Replace call sites that instantiate QuantFP8 with direct calls to the appropriate IR op, and remove the class. ### Blocker `forward_cuda` contains a special path for the DeepGemm packed scale format that calls `per_token_group_quant_fp8_packed_for_deepgemm`. This path has no equivalent in the IR ops and must be handled by retaining it as a separate call before QuantFP8 can be removed. ### Alternatives Retain `QuantFP8` and accept the indirection. This leaves an unnecessary abstraction layer between call sites and the IR ops. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of freq...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [vllm IR]: Remove `QuantFP8` in favour of direct `ir.ops` calls feature request ### 🚀 The feature, motivation and pitch ### Description `QuantFP8` is a `CustomOp` whose `forward_native` already delegates, almost, entire...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Blocker `forward_cuda` contains a special path for the DeepGemm packed scale format that calls `per_token_group_quant_fp8_packed_for_deepgemm`. This path has no equivalent in the IR ops and must be handled by retain...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: quant_fp8`, `ir.ops.static_group_quant_fp8`). The IR ops handle platform dispatch internally, making the `CustomOp` abstraction redundant. ### Proposed change Replace call sites that instantiate QuantFP8 with direct cal...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### Blocker `forward_cuda` contains a special path for the DeepGemm packed scale format that calls `per_token_group_quant_fp8_packed_for_deepgemm`. This path has no equivalent in the IR ops and must be handled by retain...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ### Blocker `forward_cuda` contains a special path for the DeepGemm packed scale format that calls `per_token_group_quant_fp8_packed_for_deepgemm`. This path has no equivalent in the IR ops and must be handled by re

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
