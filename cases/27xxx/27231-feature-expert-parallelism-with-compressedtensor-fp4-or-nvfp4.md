# vllm-project/vllm#27231: [Feature]: Expert Parallelism with CompressedTensor FP4 or NVFP4

| 字段 | 值 |
| --- | --- |
| Issue | [#27231](https://github.com/vllm-project/vllm/issues/27231) |
| 状态 | closed |
| 标签 | feature request;nvidia |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;moe;quantization |
| 子分类 |  |
| Operator 关键词 | moe;quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Expert Parallelism with CompressedTensor FP4 or NVFP4

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In order to further improve the performance of large models like Qwen3-VL-235B, fp4 plus expert parallel is a necessary feature. ### Alternatives _No response_ ### Additional context The current fp4 checkpoint is quantized through llm-compressor. The current quantization method class has assertion that blocks using --enable-expert-parallel. `AssertionError: Expert Parallelism / expert_map is currently not supported for CompressedTensorsW4A4MoeMethod.` Similar warning has been seen on NVFP4 method through modelopt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature]: Expert Parallelism with CompressedTensor FP4 or NVFP4 feature request;nvidia ### 🚀 The feature, motivation and pitch In order to further improve the performance of large models like Qwen3-VL-235B, fp4 plus ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Expert Parallelism with CompressedTensor FP4 or NVFP4 feature request;nvidia ### 🚀 The feature, motivation and pitch In order to further improve the performance of large models like Qwen3-VL-235B, fp4 plus ex...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tivation and pitch In order to further improve the performance of large models like Qwen3-VL-235B, fp4 plus expert parallel is a necessary feature. ### Alternatives _No response_ ### Additional context The current fp4 c...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: Expert Parallelism with CompressedTensor FP4 or NVFP4 feature request;nvidia ### 🚀 The feature, motivation and pitch In order to further improve the performance of large models like Qwen3-VL-235B, fp4 plus ex...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: m-compressor. The current quantization method class has assertion that blocks using --enable-expert-parallel. `AssertionError: Expert Parallelism / expert_map is currently not supported for CompressedTensorsW4A4MoeMetho...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
