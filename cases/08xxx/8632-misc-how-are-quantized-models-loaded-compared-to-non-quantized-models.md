# vllm-project/vllm#8632: [Misc]: How are quantized models loaded compared to non-quantized models?

| 字段 | 值 |
| --- | --- |
| Issue | [#8632](https://github.com/vllm-project/vllm/issues/8632) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: How are quantized models loaded compared to non-quantized models?

### Issue 正文摘录

Hi, I am trying to research MoE layer memory optimizations and I am using vLLM to do so. I have some custom logging code in the initializers/model code of the Mixtral model. When I load a quantized model, no logging code is executed. Simple print statements in the `MixtralModel.__init__` are not printed to screen. Is this on purpose? Where are the MoE kernels getting executed? Thanks for any help, I have been stuck on this for a while. For reference, I have tried to use the https://huggingface.co/TheBloke/mixtral-8x7b-v0.1-AWQ and I have quantized my own models with autoAWQ and bitsandbytes and the same behavior occurs.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Misc]: How are quantized models loaded compared to non-quantized models? Hi, I am trying to research MoE layer memory optimizations and I am using vLLM to do so. I have some custom logging code in the initializers/mode...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Misc]: How are quantized models loaded compared to non-quantized models? Hi, I am trying to research MoE layer memory optimizations and I am using vLLM to do so. I have some custom logging code in the initializers/mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: models loaded compared to non-quantized models? Hi, I am trying to research MoE layer memory optimizations and I am using vLLM to do so. I have some custom logging code in the initializers/model code of the Mixtral mode...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ls loaded compared to non-quantized models? Hi, I am trying to research MoE layer memory optimizations and I am using vLLM to do so. I have some custom logging code in the initializers/model code of the Mixtral model. W...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
