# vllm-project/vllm#3520: [Bug]: vllm slows down after a long run

| 字段 | 值 |
| --- | --- |
| Issue | [#3520](https://github.com/vllm-project/vllm/issues/3520) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm slows down after a long run

### Issue 正文摘录

### Your current environment ```text Collecting environment information... /data/miniconda3_new/envs/vllm/lib/python3.10/site-packages/transformers/utils/hub.py:124: FutureWarning: Using `TRANSFORMERS_CACHE` is deprecated and will be removed in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.28.0 Libc version: glibc-2.35 Python version: 3.10.0 | packaged by conda-forge | (default, Nov 20 2021, 02:24:10) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-6.5.0-21-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 Nvidia driver version: 525.147.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: 架构： x86_64 CPU 运行模式： 32-bit, 64...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: d in v5 of Transformers. Use `HF_HOME` instead. warnings.warn( PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC vers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ead. warnings.warn( PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: bug;stale ### Your current environment ```text Collecting environment information... /data/miniconda3_new/envs/vllm/lib/python3.10/site-packages/transformers/utils/hub.py:124: FutureWarning: Using `TRANSFORMERS_CACHE` i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm slows down after a long run bug;stale ### Your current environment ```text Collecting environment information... /data/miniconda3_new/envs/vllm/lib/python3.10/site-packages/transformers/utils/hub.py:124: Fut...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: torch==2.1.2 [pip3] torchaudio==2.1.2 [pip3] torchvision==0.16.2 [pip3] triton==2.1.0 [conda] numpy 1.24.4 pypi_0 pypi [conda] torch 2.1.2 pypi_0 pypi [conda] torchaudio 2.1.2

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
