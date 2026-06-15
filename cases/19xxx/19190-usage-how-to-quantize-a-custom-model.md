# vllm-project/vllm#19190: [Usage]: How to quantize a custom model

| 字段 | 值 |
| --- | --- |
| Issue | [#19190](https://github.com/vllm-project/vllm/issues/19190) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to quantize a custom model

### Issue 正文摘录

### Your current environment ```text --2025-06-05 08:50:21-- https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8001::154, 2606:50c0:8000::154, 2606:50c0:8002::154, ... Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8001::154|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 28292 (28K) [text/plain] Saving to: ‘collect_env.py.3’ collect_env.py.3 100%[===================>] 27.63K --.-KB/s in 0.06s 2025-06-05 08:50:21 (489 KB/s) - ‘collect_env.py.3’ saved [28292/28292] INFO 06-05 08:50:25 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.7.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 21.0.0 (++20250204042402+749372ba2423-1~exp1~20250204042535.2211) CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-60-gene...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ly detected platform cuda. Collecting environment information... PyTorch version: 2.7.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ] INFO 06-05 08:50:25 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.7.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: How to quantize a custom model usage;stale ### Your current environment ```text --2025-06-05 08:50:21-- https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py Resolving raw.githubuserconte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: How to quantize a custom model usage;stale ### Your current environment ```text --2025-06-05 08:50:21-- https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py Resolving raw.githubuserconte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.7.0 [pip3] torchvision==0.22.0 [pip3] transformers==4.52.4 [pip3] triton==3.3.0 [conda] numpy 2.2.6 pypi_0 pypi [conda] nvidia-cublas-cu12 12.6.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.6.80

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
