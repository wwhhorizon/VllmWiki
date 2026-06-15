# vllm-project/vllm#24917: [Performance]: Fuse padding onto GEMM by making the GEMM out-of-place

| 字段 | 值 |
| --- | --- |
| Issue | [#24917](https://github.com/vllm-project/vllm/issues/24917) |
| 状态 | open |
| 标签 | performance;unstale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Fuse padding onto GEMM by making the GEMM out-of-place

### Issue 正文摘录

### Proposal to improve performance Currently, at the start of fused_moe, we pad the hidden dim of the activations to comply with fused moe kernel requirements. This results in a copy following the router GEMM (GPT-OSS, Deepseek). In the captured fx.Graph, it looks something like: ``` ... mul_22: "bf16[s72, 2880]" = torch.ops.aten.mul.Tensor(convert_element_type_6, arg4_1); convert_element_type_6 = arg4_1 = None constant_pad_nd: "bf16[s72, 3072]" = torch.ops.aten.constant_pad_nd.default(mul_22, [0, 192], 0.0) ... ``` Instead, we should write the output of `mul_22` into a pre-padded tensor by replacing the sequence of these two operations with an out-of-place mm call (that takes a pre-allocated output tensor as an arg). ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked quest...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Performance]: Fuse padding onto GEMM by making the GEMM out-of-place performance;unstale ### Proposal to improve performance Currently, at the start of fused_moe, we pad the hidden dim of the activations to comply with...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: kes a pre-allocated output tensor as an arg). ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: we should write the output of `mul_22` into a pre-padded tensor by replacing the sequence of these two operations with an out-of-place mm call (that takes a pre-allocated output tensor as an arg). ### Report of performa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: red fx.Graph, it looks something like: ``` ... mul_22: "bf16[s72, 2880]" = torch.ops.aten.mul.Tensor(convert_element_type_6, arg4_1); convert_element_type_6 = arg4_1 = None constant_pad_nd: "bf16[s72, 3072]" = torch.ops...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
