# vllm-project/vllm#19607: [Usage]: Full cuda graph for vllm v1

| 字段 | 值 |
| --- | --- |
| Issue | [#19607](https://github.com/vllm-project/vllm/issues/19607) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Full cuda graph for vllm v1

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` INFO 06-13 17:46:31 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : CentOS Linux 7 (Core) (x86_64) GCC version : (GCC) 9.3.1 20200408 (Red Hat 9.3.1-2) Clang version : Could not collect CMake version : version 3.25.0-rc2 Libc version : glibc-2.17 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (main, Oct 10 2024, 21:53:07) [GCC 10.2.1 20210130 (Red Hat 10.2.1-11)] (64-bit runtime) Python platform : Linux-4.18.0-147.mt20200626.413.el8_1.x86_64-x86_64-with-glibc2.17 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.99 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver versio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ====== OS : CentOS Linux 7 (Core) (x86_64) GCC version : (GCC) 9.3.1 20200408 (Red Hat 9.3.1-2) Clang version : Could not collect CMake version : version 3.25.0-rc2 Libc version : glibc-2.17 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Usage]: Full cuda graph for vllm v1 usage;stale ### Your current environment ```text The output of `python collect_env.py` INFO 06-13 17:46:31 [__init__.py:239] Automatically detected platform cuda. Collecting environm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: _.py:239] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : CentOS Linux 7 (Core) (x86_64) GCC version : (GCC) 9.3...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: Versions of relevant libraries ============================== [pip3] mt-tritonclient==1.0.4 [pip3] mypy==1.15.0 [pip3] mypy_extensions==1.1.0 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Full cuda graph for vllm v1 usage;stale ### Your current environment ```text The output of `python collect_env.py` INFO 06-13 17:46:31 [__init__.py:239] Automatically detected platform cuda. Collecting environm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
