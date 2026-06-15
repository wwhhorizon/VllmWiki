# vllm-project/vllm#37753: [Feature]: Unify MoE "Oracles" with Class Structure

| 字段 | 值 |
| --- | --- |
| Issue | [#37753](https://github.com/vllm-project/vllm/issues/37753) |
| 状态 | open |
| 标签 | help wanted;good first issue;feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Unify MoE "Oracles" with Class Structure

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We currently have the following MoE "oracles", which select the right MoE kernel for each model - `model_executor/layers/fused_moe/oracle` We have: - fp8 - nvfp4 - mxfp8 - unquantized and will soon have mxfp4 Each of these has the following functions: - `select_XX_moe_backend` - called by the quantization integration to get the backend - `convert_to_XX_moe_kernel_format` - called by the quantization integration to shuffle the weights - `make_XX_moe_quant_config` - called by the quantization integration to make the quant config - `make_fp8_moe_kernel` - called by the quantization integration to construct the kernel Now that we have the structure standardized, we need to create a generic class that implements this logic. Then, each oracle can inherit from this. So, we would have the following: ``` class MoEKernelOracle(ABC) ... class Fp8MoEKernelOracle(MoEOracle): ... ``` and so on and so forth ### Alternatives just use conventions. this is a bad idea due to drift and duplicated code ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living a...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: el for each model - `model_executor/layers/fused_moe/oracle` We have: - fp8 - nvfp4 - mxfp8 - unquantized and will soon have mxfp4 Each of these has the following functions: - `select_XX_moe_backend` - called by the qua...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: the following MoE "oracles", which select the right MoE kernel for each model - `model_executor/layers/fused_moe/oracle` We have: - fp8 - nvfp4 - mxfp8 - unquantized and will soon have mxfp4 Each of these has the follow...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: have mxfp4 Each of these has the following functions: - `select_XX_moe_backend` - called by the quantization integration to get the backend - `convert_to_XX_moe_kernel_format` - called by the quantization integration to...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: forth ### Alternatives just use conventions. this is a bad idea due to drift and duplicated code ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
