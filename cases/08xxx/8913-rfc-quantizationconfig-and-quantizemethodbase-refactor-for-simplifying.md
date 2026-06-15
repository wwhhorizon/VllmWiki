# vllm-project/vllm#8913: [RFC]: QuantizationConfig and QuantizeMethodBase Refactor for Simplifying Kernel Integrations

| 字段 | 值 |
| --- | --- |
| Issue | [#8913](https://github.com/vllm-project/vllm/issues/8913) |
| 状态 | open |
| 标签 | RFC;keep-open;unstale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: QuantizationConfig and QuantizeMethodBase Refactor for Simplifying Kernel Integrations

### Issue 正文摘录

### Motivation. Currently vLLM generally has a tight coupling between the checkpoint format and the kernel used during model execution. This model causes issues as the diversity of hardware and kernels increases. This is particularly challenging for quantized kernels (mixed-precision with subbyte weights in particular). For performance, quantized kernels will frequently want to run hardware specialized kernels and for mixed-input commonly pre-pack the weights into a bespoke layout that closely matches the hardware it's running on. The goal is to separate the kernel implementation from checkpoint format; this will require a more sophisticated way of describing the linear layer operation in addition to a more sophisticated way of describing packed layouts within vLLM. The result will hopefully make it easier to register a kernel as a backend for multiple checkpoint formats. It will also require standardizing the calling structure of quantized linear layers in vLLM. ### Proposed Change. The high level proposal is to separate out the `create_weights` logic, moving it into `QuantizationConfig` from `QuantizeMethodBase`, as `QuantizationConfig` is more closely tied to the serialization...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: QuantizationConfig and QuantizeMethodBase Refactor for Simplifying Kernel Integrations RFC;keep-open;unstale ### Motivation. Currently vLLM generally has a tight coupling between the checkpoint format and the ker...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: vLLM. The result will hopefully make it easier to register a kernel as a backend for multiple checkpoint formats. It will also require standardizing the calling structure of quantized linear layers in vLLM. ### Proposed...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: @robertgshaw2-neuralmagic @comaniac @alexm-neuralmagic @HanGuo97 @tlrmchlsmth @bnellnm ### Any Other Things. _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, a...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: increases. This is particularly challenging for quantized kernels (mixed-precision with subbyte weights in particular). For performance, quantized kernels will frequently want to run hardware specialized kernels and for...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: reases. This is particularly challenging for quantized kernels (mixed-precision with subbyte weights in particular). For performance, quantized kernels will frequently want to run hardware specialized kernels and for mi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
