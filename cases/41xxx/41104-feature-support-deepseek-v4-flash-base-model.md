# vllm-project/vllm#41104: [Feature]: Support DeepSeek-V4-Flash-Base model

| 字段 | 值 |
| --- | --- |
| Issue | [#41104](https://github.com/vllm-project/vllm/issues/41104) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support DeepSeek-V4-Flash-Base model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently vLLM can only run with the DSV4 instruct models. Base models are not supported. Supporting base model is important for RL which normally runs with the Base. When trying to run with the Base model, the `RuntimeError` will occur in `fused_moe/layer.py`: ```python expert_data.copy_(loaded_weight) # RuntimeError: The size of tensor a (2048) must match the size of tensor b (16) ``` **Why this happens:** 1. The vLLM `deepseek_v4.py` loader are built for the **Instruct** format, where the MoE experts are quantized to **FP4** (highly packed/compressed). 2. The **Base** model uses **pure FP8** weights. The tensor shapes, packing, and quantization scales are completely different. 3. When the weight loader tries to copy FP8-shaped data into an FP4-expecting buffer (or applies an FP4 dequantization view to an FP8 tensor), the dimensions don't align, producing the 2048 vs. 16 mismatch. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vll...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: loader are built for the **Instruct** format, where the MoE experts are quantized to **FP4** (highly packed/compressed). 2. The **Base** model uses **pure FP8** weights. The tensor shapes, packing, and quantization scal...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nstruct models. Base models are not supported. Supporting base model is important for RL which normally runs with the Base. When trying to run with the Base model, the `RuntimeError` will occur in `fused_moe/layer.py`:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: an FP8 tensor), the dimensions don't align, producing the 2048 vs. 16 mismatch. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already search...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support DeepSeek-V4-Flash-Base model feature request ### 🚀 The feature, motivation and pitch Currently vLLM can only run with the DSV4 instruct models. Base models are not supported. Supporting base model is...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ying to run with the Base model, the `RuntimeError` will occur in `fused_moe/layer.py`: ```python expert_data.copy_(loaded_weight) # RuntimeError: The size of tensor a (2048) must match the size of tensor b (16) ``` **W...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
