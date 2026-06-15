# vllm-project/vllm#34252: [Bug]: Multi-GPU NCCL initialization fails with Cuda failure 700 'an illegal memory access was encountered' on NVIDIA B200 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#34252](https://github.com/vllm-project/vllm/issues/34252) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-GPU NCCL initialization fails with Cuda failure 700 'an illegal memory access was encountered' on NVIDIA B200 GPUs

### Issue 正文摘录

# Environment GPUs: NVIDIA B200 (8 GPUs) vLLM: latest (pip-installed) Python: 3.12 CUDA Toolkit: 13.1 NVIDIA Driver: 590 Guest OS: Ubuntu 24.04 Host OS: Ubuntu 25.10 Environment: Running inside a VM following the NVIDIA TDX Deployment Guide https://docs.nvidia.com/cc-deployment-guide-tdx.pdf ### 🐛 Describe the bug vLLM fails to start in multi-GPU mode on NVIDIA B200 GPUs with an NCCL error: ``Cuda failure 700 'an illegal memory access was encountered'`` Single-GPU runs work correctly. Any configuration with tensor-parallel-size > 1 fails immediately during NCCL initialization. ## Reproduction (vLLM) Command ``` vllm serve \ --model deepseek-ai/DeepSeek-Coder-V2-Lite-Base \ --host 0.0.0.0 \ --port 8000 \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.8 ``` ## Observed Behavior ``` ERROR 02-10 03:17:41 [multiproc_executor.py:772] WorkerProc failed to start. ERROR 02-10 03:17:41 [multiproc_executor.py:772] Traceback (most recent call last): ERROR 02-10 03:17:41 [multiproc_executor.py:772] File "/root/.env/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 743, in worker_main ERROR 02-10 03:17:41 [multiproc_executor.py:772] worker = WorkerProc(*args, **k...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: B200 GPUs bug # Environment GPUs: NVIDIA B200 (8 GPUs) vLLM: latest (pip-installed) Python: 3.12 CUDA Toolkit: 13.1 NVIDIA Driver: 590 Guest OS: Ubuntu 24.04 Host OS: Ubuntu 25.10 Environment: Running inside a VM follow...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Multi-GPU NCCL initialization fails with Cuda failure 700 'an illegal memory access was encountered' on NVIDIA B200 GPUs bug # Environment GPUs: NVIDIA B200 (8 GPUs) vLLM: latest (pip-installed) Python: 3.12 CUDA...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: gal memory access was encountered'`` Single-GPU runs work correctly. Any configuration with tensor-parallel-size > 1 fails immediately during NCCL initialization. ## Reproduction (vLLM) Command ``` vllm serve \ --model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: use ring PXN 0 GDR 1 [2026-02-10 03:17:41] tdx-guest:13723:13723 [0] enqueue.cc:1626 NCCL WARN Cuda failure 700 'an illegal memory access was encountered' tdx-guest:13723:13723 [0] NCCL INFO group.cc:299 -> 1 tdx-guest:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: on NVIDIA B200 GPUs bug # Environment GPUs: NVIDIA B200 (8 GPUs) vLLM: latest (pip-installed) Python: 3.12 CUDA Toolkit: 13.1 NVIDIA Driver: 590 Guest OS: Ubuntu 24.04 Host OS: Ubuntu 25.10 Environment: Running inside a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
