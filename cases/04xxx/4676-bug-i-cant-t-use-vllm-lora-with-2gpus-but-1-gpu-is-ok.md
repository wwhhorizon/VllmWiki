# vllm-project/vllm#4676: [Bug]: i cant't use vllm lora with 2gpus, but 1 gpu is ok

| 字段 | 值 |
| --- | --- |
| Issue | [#4676](https://github.com/vllm-project/vllm/issues/4676) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: i cant't use vllm lora with 2gpus, but 1 gpu is ok

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.11.9 (main, Apr 6 2024, 17:59:24) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-28-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.3.52 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 ``` ### 🐛 Describe the bug if i set" tensor_parallel_size=1, " the program running fine , but if i set "tensor_parallel_size=2", the program will report the error: ''' (RayWorkerWrapper pid=131231) ERROR 05-08 15:54:03 worker_base.py:145] File "/home/e5/xxwriter/llm_program/vllm-kynow-2/venv-vllm-kynow2/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context (RayWorkerWrapper pid=131231) ERROR 05-08 15:54:03 worker_base.py:145] return func(*args, **kwargs) (RayWorkerWrapper pid=131231) ERROR 05-08 15:54:03 worker_b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: but 1 gpu is ok bug;stale ### Your current environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.3.52 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 GPU 1: NVIDIA GeForce RTX 4090 ``` ### 🐛 Describe the bug if i set" tensor_parallel_size=1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ion = 0.8, tensor_parallel_size=2,# gpu num dtype="float16", ) while True: prompt = input('write the request：') get_lora_reqonse(prompt, llm)` development ci_build;frontend_api;hardware_porting;sampling_logits cuda;samp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rent environment ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
