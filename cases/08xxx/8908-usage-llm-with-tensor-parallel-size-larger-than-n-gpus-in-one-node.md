# vllm-project/vllm#8908: [Usage]: LLM with tensor_parallel_size larger than n. gpus in one node

| 字段 | 值 |
| --- | --- |
| Issue | [#8908](https://github.com/vllm-project/vllm/issues/8908) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: LLM with tensor_parallel_size larger than n. gpus in one node

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` on a single node: Register this system with Red Hat Insights: insights-client --register Create an account or view all your systems at https://red.ht/insights-dashboard Last login: Fri Sep 27 16:49:32 2024 from 10.99.0.2 [gpuccett@lrdn0487 ~]$ cd /leonardo_scratch/large/userexternal/gpuccett/Repos/MGT2025-private/ [gpuccett@lrdn0487 MGT2025-private]$ conda activate conda_venv/ (/leonardo_scratch/large/userexternal/gpuccett/Repos/MGT2025-private/conda_venv) [gpuccett@lrdn0487 MGT2025-private]$ python collect_env.py Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8.7 (Ootpa) (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-16) Clang version: Could not collect CMake version: version 3.20.2 Libc version: glibc-2.28 Python version: 3.12.6 | packaged by conda-forge | (main, Sep 22 2024, 14:16:49) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-4.18.0-425.19.2.el8_7.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: Could not collect CU...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: e]$ python collect_env.py Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux release 8.7 (Ootpa) (x86_64) GCC version: (GCC) 8.5....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: dn0487 MGT2025-private]$ python collect_env.py Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: caler +21m12s)ESC[0m Error: No available node types can fulfill resource request {'node:10.2.0.127': 0.001, 'GPU': 1.0}. Add suitable node types to this cluster to resolve this issue. INFO 09-27 16:47:50 ray_utils.py:18...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.45.1 [pip3] triton==3.0.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
