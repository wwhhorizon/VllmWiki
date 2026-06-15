# vllm-project/vllm#8484: [Usage]: Model Qwen2VLForConditionalGeneration does not support LoRA, but LoRA is enabled.

| 字段 | 值 |
| --- | --- |
| Issue | [#8484](https://github.com/vllm-project/vllm/issues/8484) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Model Qwen2VLForConditionalGeneration does not support LoRA, but LoRA is enabled.

### Issue 正文摘录

### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.15.0-113-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-16GB Nvidia driver version: 550.90.07 cuDNN version: Probably one of the following: /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn_adv.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn_cnn.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn_engines_precompiled.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn_engines_runtime_compiled.so.9.2.0 /usr/local/cuda-12.4/targets/x86_64-linux/lib/libcudnn_graph.so.9.2.0 /usr/local/cuda-12.4/target...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: t LoRA, but LoRA is enabled. usage ### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Model Qwen2VLForConditionalGeneration does not support LoRA, but LoRA is enabled. usage ### Your current environment PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 19.0 [pip3] transformers==4.45.0.dev0 [pip3] triton==3.0.0 [pip3] vector-quantize-pytorch==1.17.1 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Mitigation; IBRS Vulnerability Spec rstack o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
