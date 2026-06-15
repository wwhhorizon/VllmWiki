# vllm-project/vllm#32358: [RFC]: vLLM IR: A Functional Intermediate Representation for vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#32358](https://github.com/vllm-project/vllm/issues/32358) |
| 状态 | open |
| 标签 | RFC;torch.compile;vllm-ir |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: vLLM IR: A Functional Intermediate Representation for vLLM

### Issue 正文摘录

### Summary This RFC proposes vLLM IR, a functional intermediate representation (IR) based on torch for custom operations like `rms_norm`, `quant`, activations, etc. It addresses issues with compilation and `CustomOp`\-based kernel dispatching. More details are available in the [detailed proposal](https://docs.google.com/document/d/1zyPdGVX7TnVtvqD9NsaTO4E02u7PY7uudreLrdWp2GM/edit?tab=t.xerdhb9i406r). Also take a look at the [slides](https://docs.google.com/presentation/u/0/d/1k0Zo33KubK7pmhYXg-7G1PjgcEbOhBkSbwiEwUpUyH0/edit). ### Motivation and proposal Fusion/transformation `torch.compile` passes struggle with custom operators like `RMSNorm`, `Quant`, etc. because they decompose to either a fragile sequence of `torch` ops or a variety of custom kernels, requiring separate handling for each of them. All of those operators are instances of `CustomOp`, which has many of its own issues, mostly stemming from complicated and clunky dispatching logic with low visibility. vLLM IR is a **functional intermediate representation (IR)** that fills the gap between low-level `torch` ops and vLLM layers like `RMSNorm`, separating the ***semantics*** from the ***implementation*** and ***dispatch...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 1PjgcEbOhBkSbwiEwUpUyH0/edit). ### Motivation and proposal Fusion/transformation `torch.compile` passes struggle with custom operators like `RMSNorm`, `Quant`, etc. because they decompose to either a fragile sequence of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: C]: vLLM IR: A Functional Intermediate Representation for vLLM RFC;torch.compile;vllm-ir ### Summary This RFC proposes vLLM IR, a functional intermediate representation (IR) based on torch for custom operations like `rm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: , etc. It addresses issues with compilation and `CustomOp`\-based kernel dispatching. More details are available in the [detailed proposal](https://docs.google.com/document/d/1zyPdGVX7TnVtvqD9NsaTO4E02u7PY7uudreLrdWp2GM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: presentation (IR) based on torch for custom operations like `rms_norm`, `quant`, activations, etc. It addresses issues with compilation and `CustomOp`\-based kernel dispatching. More details are available in the [detail...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 519 @youkaichao @tjtanaa @BoyuanFeng @mgoin @robertgshaw2-redhat @tlrmchlsmth @LucasWilkinson @Yikun @whx-sjtu @xuechendi ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you alre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
