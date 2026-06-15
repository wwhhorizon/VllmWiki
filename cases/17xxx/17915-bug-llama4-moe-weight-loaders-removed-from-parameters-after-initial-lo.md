# vllm-project/vllm#17915: [Bug]: Llama4 MoE weight_loaders Removed from Parameters After Initial Load, Causing Errors During Refitting

| 字段 | 值 |
| --- | --- |
| Issue | [#17915](https://github.com/vllm-project/vllm/issues/17915) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama4 MoE weight_loaders Removed from Parameters After Initial Load, Causing Errors During Refitting

### Issue 正文摘录

### Your current environment **Environment:** * vLLM version: [0.8.4] * ray version: [2.43.0] ### 🐛 Describe the bug **Description:** We are integrating Llama4 (with Mixture of Experts) support into a reinforcement learning framework. While the initial model loading and weight initialization from Hugging Face checkpoints work correctly with vLLM, we encounter an issue when attempting to refit or update the model weights via worker extensions. The process fails with an error indicating that an MoE parameter (specifically observed with `w2_weight`) is missing its `weight_loader`. Dense parameters do not exhibit this issue. Through debugging, we've observed that the `weight_loader` attribute for MoE parameters (e.g., `w2_weight`) appears to be removed or unset *after* the initial model loading and processing steps, specifically during the `_process_weights_after_loading` call which subsequently involves `Llama4Model.setattr`. This removal prevents subsequent operations like weight updates that might rely on these loaders. **Steps to Reproduce:** 1. Initialize a Llama4 model with MoE layers using vLLM. 2. Load Hugging Face pretrained weights. (This step completes successfully). 3. Att...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama4 MoE weight_loaders Removed from Parameters After Initial Load, Causing Errors During Refitting bug ### Your current environment **Environment:** * vLLM version: [0.8.4] * ray version: [2.43.0] ### 🐛 Descri...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ations like weight updates that might rely on these loaders. **Steps to Reproduce:** 1. Initialize a Llama4 model with MoE layers using vLLM. 2. Load Hugging Face pretrained weights. (This step completes successfully)....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ring Refitting bug ### Your current environment **Environment:** * vLLM version: [0.8.4] * ray version: [2.43.0] ### 🐛 Describe the bug **Description:** We are integrating Llama4 (with Mixture of Experts) support into a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cessfully). 3. Attempt to update or refit the MoE weights using a mechanism that might rely on the `weight_loader` attribute (e.g., through worker extensions or a custom refitting loop). 4. Observe an error related to a...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Llama4 MoE weight_loaders Removed from Parameters After Initial Load, Causing Errors During Refitting bug ### Your current environment **Environment:** * vLLM version: [0.8.4] * ray version: [2.43.0] ### 🐛 Descri...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
