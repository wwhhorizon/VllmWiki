# vllm-project/vllm#6213: [Bug]: Using vllm as the inference engine, there is an incorrect recognition of GPU computing capabilities for different types.

| 字段 | 值 |
| --- | --- |
| Issue | [#6213](https://github.com/vllm-project/vllm/issues/6213) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using vllm as the inference engine, there is an incorrect recognition of GPU computing capabilities for different types.

### Issue 正文摘录

### Your current environment ```text (py311) (base) lianjh@cloud88:/storage/lianjh/dev$ python collect_env.py Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-102-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.7.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM3-32GB GPU 1: NVIDIA GeForce RTX 3090 GPU 2: Tesla V100-PCIE-32GB GPU 3: Tesla V100-PCIE-32GB GPU 4: NVIDIA A800 80GB PCIe GPU 5: NVIDIA A800 80GB PCIe GPU 6: NVIDIA A800 80GB PCIe GPU 7: NVIDIA A800 80GB PCIe Nvidia driver version: 550.54.15 cuDNN version: Probably one of the following: /usr/local/cuda-10.2/targets/x86_64-linux/lib/libcudnn.so.7 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn.so.8.8.1 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.8....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: dev$ python collect_env.py Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ud88:/storage/lianjh/dev$ python collect_env.py Collecting environment information... PyTorch version: 2.3.0 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ite-packages/vllm/worker/worker.py", line 337, in _check_if_gpu_supports_dtype raise ValueError( ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your NVIDIA A800 80GB PCIe GPU has...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Mitigation; Enhanced IBRS Vulnerability Spec rstack overflow: Not affected V...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
