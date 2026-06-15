# vllm-project/vllm#26984: [Bug]: qwen2.5-vl vit fp8 scaled_mm_kernel kernel bug,

| 字段 | 值 |
| --- | --- |
| Issue | [#26984](https://github.com/vllm-project/vllm/issues/26984) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen2.5-vl vit fp8 scaled_mm_kernel kernel bug,

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug > When deploying the Qwen2.5-VL-7B model with FP8 quantization on vLLM, I encountered the following issue: when I attempted to enable FP8 quantization for the ViT (Vision Transformer), severe performance degradation occurred in the ViT's GEMM (General Matrix Multiplication) operations. Specifically, the latency of an FP8 scaled_mm_kernel degraded from 737 microseconds (in the FP8-wo-ViT scenario) to 40 milliseconds. Here, "FP8-w-ViT" denotes enabling FP8 quantization for the ViT, and "FP8-wo-ViT" denotes not enabling FP8 quantization for the ViT. Could you tell us if this is a problem that has already been encountered, and how to resolve it? for fp8 without vit we use following command [fp8 quantization](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/qwen_2_5_vl_example.py) for fp8 with vit we also use following command [fp8 quantization](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/qwen_2_5_vl_example.py) but ignore is `ignore=["re:.*lm_head"]` the following pdf is out detailed result [1.vllm qwen2.5-vl-7b vit-fp8 gemm issue.pdf](https://github.c...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: qwen2.5-vl vit fp8 scaled_mm_kernel kernel bug, bug;stale ### Your current environment ### 🐛 Describe the bug > When deploying the Qwen2.5-VL-7B model with FP8 quantization on vLLM, I encountered the following is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: qwen2.5-vl vit fp8 scaled_mm_kernel kernel bug, bug;stale ### Your current environment ### 🐛 Describe the bug > When deploying the Qwen2.5-VL-7B model with FP8 quantization on vLLM, I encountered the following is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ccurred in the ViT's GEMM (General Matrix Multiplication) operations. Specifically, the latency of an FP8 scaled_mm_kernel degraded from 737 microseconds (in the FP8-wo-ViT scenario) to 40 milliseconds. Here, "FP8-w-ViT...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: df) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: qwen2.5-vl vit fp8 scaled_mm_kernel kernel bug, bug;stale ### Your current environment ### 🐛 Describe the bug > When deploying the Qwen2.5-VL-7B model with FP8 quantization on vLLM, I encountered the following is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
