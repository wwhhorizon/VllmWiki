# vllm-project/vllm#29883: [Bug]: Qwen3-Next-80B-A3B-Instruct-FP8 crashes with CUDA illegal memory access on vLLM 0.11.2 (even with cudagraph_mode=PIECEWISE)

| 字段 | 值 |
| --- | --- |
| Issue | [#29883](https://github.com/vllm-project/vllm/issues/29883) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next-80B-A3B-Instruct-FP8 crashes with CUDA illegal memory access on vLLM 0.11.2 (even with cudagraph_mode=PIECEWISE)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Summary When running Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 on vLLM v0.11.2, the engine crashes with: torch.AcceleratorError: CUDA error: an illegal memory access was encountered deep_gemm::DGException: Assertion error: error == CUDA_SUCCESS or error == CUDA_ERROR_DEINITIALIZED This happens even when using the recommended workaround: --compilation-config {"cudagraph_mode": "PIECEWISE"} The crash occurs during generation (sample_tokens) with long sequences (~5400 tokens total). The process dies, and the API server returns EngineDeadError. This appears related but not identical to issue #28835, as the problem persists with PIECEWISE and with the FP8 variant of Qwen3-Next-80B. Environment vLLM version: v0.11.2 (vllm/vllm-openai:v0.11.2 Docker image) Model: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 GPU: NVIDIA H200 (CUDA 12.8 / 12.9) Driver: NVIDIA-SMI 580.95.05 Setup: single GPU (tensor_parallel_size=1) Docker Compose command: command: - --model - Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 - --served-model-name - Qwen3-Next-80B-A3B - --gpu-memory-utilization - "0.9" - --enable-auto-tool-choice - --tool-call-parser - hermes - --compilation-config...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: PIECEWISE and with the FP8 variant of Qwen3-Next-80B. Environment vLLM version: v0.11.2 (vllm/vllm-openai:v0.11.2 Docker image) Model: Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 GPU: NVIDIA H200 (CUDA 12.8 / 12.9) Driver: NVI...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Qwen3-Next-80B-A3B-Instruct-FP8 crashes with CUDA illegal memory access on vLLM 0.11.2 (even with cudagraph_mode=PIECEWISE) bug;unstale ### Your current environment ### 🐛 Describe the bug Summary When running Qwe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3-Next-80B-A3B-Instruct-FP8 crashes with CUDA illegal memory access on vLLM 0.11.2 (even with cudagraph_mode=PIECEWISE) bug;unstale ### Your current environment ### 🐛 Describe the bug Summary When running Qwe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Next-80B-A3B-Instruct-FP8 crashes with CUDA illegal memory access on vLLM 0.11.2 (even with cudagraph_mode=PIECEWISE) bug;unstale ### Your current environment ### 🐛 Describe the bug Summary When running Qwe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: memory access on vLLM 0.11.2 (even with cudagraph_mode=PIECEWISE) bug;unstale ### Your current environment ### 🐛 Describe the bug Summary When running Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 on vLLM v0.11.2, the engine cra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
