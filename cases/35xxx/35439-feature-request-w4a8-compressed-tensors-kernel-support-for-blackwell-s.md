# vllm-project/vllm#35439: [Feature Request]: W4A8 (compressed-tensors) Kernel support for Blackwell SM100+

| 字段 | 值 |
| --- | --- |
| Issue | [#35439](https://github.com/vllm-project/vllm/issues/35439) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;moe;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature Request]: W4A8 (compressed-tensors) Kernel support for Blackwell SM100+

### Issue 正文摘录

### Your current environment vLLM version: 0.15.1 PyTorch: 2.9.1+cu129 CUDA: 12.9 GPU: NVIDIA B200 (SM100, Blackwell) OS: Linux (Docker, vllm/vllm-openai:latest) Python: 3.12 ### Model Qwen/Qwen3-30B-A3B (MoE), quantized to W4A8 (int4 weights + fp8 activations) using llm-compressor `oneshot()` with `scheme="W4A8"` via compressed-tensors format. ### 🐛 Describe the bug Loading a W4A8 compressed-tensors checkpoint into vLLM on a Blackwell B200 GPU (SM100) fails during model initialization. vLLM cannot find any mixed-precision linear kernel that supports SM100 for the W4A8 scheme. All six registered kernel implementations reject SM100: | Kernel | Rejection reason | |--------|-----------------| | CutlassW4A8LinearKernel | Requires compute capability of 90 (Hopper) | | MacheteLinearKernel | Requires compute capability of 90 (Hopper) | | AllSparkLinearKernel | Does not support device_capability = 100 | | MarlinLinearKernel | Quant type (int4) not supported | | ConchLinearKernel | Weight type (int4) not supported | | ExllamaLinearKernel | Only supports float16 activations | The same checkpoint works correctly on Hopper (SM90) GPUs. Quantization (export) succeeds on all architectures — onl...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: m/vllm-openai:latest) Python: 3.12 ### Model Qwen/Qwen3-30B-A3B (MoE), quantized to W4A8 (int4 weights + fp8 activations) using llm-compressor `oneshot()` with `scheme="W4A8"` via compressed-tensors format. ### 🐛 Descri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Feature Request]: W4A8 (compressed-tensors) Kernel support for Blackwell SM100+ bug;stale ### Your current environment vLLM version: 0.15.1 PyTorch: 2.9.1+cu129 CUDA: 12.9 GPU: NVIDIA B200 (SM100, Blackwell) OS: Linux...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: upport for Blackwell SM100+ bug;stale ### Your current environment vLLM version: 0.15.1 PyTorch: 2.9.1+cu129 CUDA: 12.9 GPU: NVIDIA B200 (SM100, Blackwell) OS: Linux (Docker, vllm/vllm-openai:latest) Python: 3.12 ### Mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Blackwell) OS: Linux (Docker, vllm/vllm-openai:latest) Python: 3.12 ### Model Qwen/Qwen3-30B-A3B (MoE), quantized to W4A8 (int4 weights + fp8 activations) using llm-compressor `oneshot()` with `scheme="W4A8"` via compre...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: PU (SM100) fails during model initialization. vLLM cannot find any mixed-precision linear kernel that supports SM100 for the W4A8 scheme. All six registered kernel implementations reject SM100: | Kernel | Rejection reas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
