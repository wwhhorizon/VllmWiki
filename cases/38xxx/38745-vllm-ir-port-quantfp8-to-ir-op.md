# vllm-project/vllm#38745: [vLLM IR] Port QuantFP8 to IR op

| 字段 | 值 |
| --- | --- |
| Issue | [#38745](https://github.com/vllm-project/vllm/issues/38745) |
| 状态 | open |
| 标签 | vllm-ir |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [vLLM IR] Port QuantFP8 to IR op

### Issue 正文摘录

Port the various ops inside the `QuantFP8` class. I think we should separate the different types of quantization instead of trying to jam them all into the same op. Quantization types and corresponding ops: - static per-tensor: `static_quant_fp8(x: Tensor, scale: Tensor) -> Tensor` - static per-group: `static_group_quant_fp8(x: Tensor, scale: Tensor) -> Tensor` - dynamic per-token/per-tensor: `dynamic_quant_fp8(x: Tensor, per_token: bool, scale_ub: Tensor | None = None) -> tuple[Tensor, Tensor]` - these could be separate ops as well but I think together is better to consolidate a bit, also dynamic per-tensor is very uncommon these days. - dynamic per-group: `dynamic_group_quant_fp8(x: Tensor, group_shape: list[int], column_major: bool, use_ue8m0: bool, scale_alignment: int = 1) -> tuple[Tensor, Tensor]` Just like activation ops, we will need to compile the native impl for use inside MoE and MLA: #38744

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [vLLM IR] Port QuantFP8 to IR op vllm-ir Port the various ops inside the `QuantFP8` class. I think we should separate the different types of quantization instead of trying to jam them all into the same op. Quantization...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 1) -> tuple[Tensor, Tensor]` Just like activation ops, we will need to compile the native impl for use inside MoE and MLA: #38744
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e activation ops, we will need to compile the native impl for use inside MoE and MLA: #38744

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
