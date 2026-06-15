# vllm-project/vllm#21873: [Usage]: Qwen 2.5 VL 7B throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#21873](https://github.com/vllm-project/vllm/issues/21873) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | throughput |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Qwen 2.5 VL 7B throughput

### Issue 正文摘录

### Your current environment ```text INFO 07-29 22:25:18 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.31.4 Libc version : glibc-2.31 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.13 | packaged by conda-forge | (main, Dec 23 2023, 15:36:39) [GCC 12.3.0] (64-bit runtime) Python platform : Linux-6.6.72+-x86_64-with-glibc2.31 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.6.85 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB Nvidia driver version : 535.129.03 =====...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 20.04.6 LTS (x86_64) GCC version : (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version : Could not collect CMake version : version 3.31.4 Libc version : glibc-2.31 =================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: xt INFO 07-29 22:25:18 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 20.04.6 LTS (x86...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Qwen 2.5 VL 7B throughput usage;stale ### Your current environment ```text INFO 07-29 22:25:18 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... =====================...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Usage]: Qwen 2.5 VL 7B throughput usage;stale ### Your current environment ```text INFO 07-29 22:25:18 [__init__.py:244] Automatically detected platform cuda. Collecting environment information... =====================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: .1 [pip3] torchvision==0.22.0+default [pip3] transformers==4.52.4 [pip3] triton==3.3.0 [conda] _anaconda_depends 2025.02 py310_mkl_0 [conda] blas 1.0 mkl [conda] curated-transformers 2.0.1 pypi_0 pypi

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
