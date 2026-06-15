# vllm-project/vllm#12411: [Usage]: Is it possible to use `meta-llama/Llama-3.2-1B-Instruct-SpinQuant_INT4_EO8` with vLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#12411](https://github.com/vllm-project/vllm/issues/12411) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Is it possible to use `meta-llama/Llama-3.2-1B-Instruct-SpinQuant_INT4_EO8` with vLLM?

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-125-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.6.77 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version: 560.35.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.5.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.5.0 /usr/lib/x86_64-linux-g...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: O8` with vLLM? usage;stale ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC ver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Usage]: Is it possible to use `meta-llama/Llama-3.2-1B-Instruct-SpinQuant_INT4_EO8` with vLLM? usage;stale ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Usage]: Is it possible to use `meta-llama/Llama-3.2-1B-Instruct-SpinQuant_INT4_EO8` with vLLM? usage;stale ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: e `meta-llama/Llama-3.2-1B-Instruct-SpinQuant_INT4_EO8` with vLLM? usage;stale ### Your current environment ```text PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
