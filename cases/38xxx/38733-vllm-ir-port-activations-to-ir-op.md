# vllm-project/vllm#38733: [vLLM IR] Port activations to IR op

| 字段 | 值 |
| --- | --- |
| Issue | [#38733](https://github.com/vllm-project/vllm/issues/38733) |
| 状态 | open |
| 标签 | vllm-ir |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [vLLM IR] Port activations to IR op

### Issue 正文摘录

`SiluAndMul` and other activation function `CustomOp` subclasses should be ported over to vLLM IR. This should be done in three steps: 1. Replace forward_* methods in `SiluAndMul` with a call to new `vllm.ir.ops.silu_and_mul`. 2. The same for other activation functions 3. Convert `CustomOp` objects to `PluggableLayer` An additional challenge is the `compile_native=True` behavior: inside the `fused_moe` torch custom op, `SiluAndMul.forward_native` is not visible to model-level compilation, so we apply another `torch.compile` decorator. To work with vLLM IR, we'll have to locally disable torch wrapping (`vllm.ir.enable_torch_wrap(False)`), and only in the MoE case. So we should default `compile_native=False` and only set it to True for MoE. Moving forward, we will enable automatic compilation of all IR native implementations by default, but that requires more design & discussion: #38744 1 is high priority, 2 is slightly less so. 3 requires the above compilation fix. Also, once all OOT platforms migrate these ops to vLLM IR, we can remove the PluggableLayer system completely.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: `CustomOp` objects to `PluggableLayer` An additional challenge is the `compile_native=True` behavior: inside the `fused_moe` torch custom op, `SiluAndMul.forward_native` is not visible to model-level compilation, so we...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 'll have to locally disable torch wrapping (`vllm.ir.enable_torch_wrap(False)`), and only in the MoE case. So we should default `compile_native=False` and only set it to True for MoE. Moving forward, we will enable auto...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: used_moe` torch custom op, `SiluAndMul.forward_native` is not visible to model-level compilation, so we apply another `torch.compile` decorator. To work with vLLM IR, we'll have to locally disable torch wrapping (`vllm....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ional challenge is the `compile_native=True` behavior: inside the `fused_moe` torch custom op, `SiluAndMul.forward_native` is not visible to model-level compilation, so we apply another `torch.compile` decorator. To wor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
