# vllm-project/vllm#20015: [Usage]: Why does the Prefix cache hit rate reach 60% for random data during benchmark?

| 字段 | 值 |
| --- | --- |
| Issue | [#20015](https://github.com/vllm-project/vllm/issues/20015) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Why does the Prefix cache hit rate reach 60% for random data during benchmark?

### Issue 正文摘录

### Your current environment ```text root@llm206:/workspace/vllm# python3 ./vllm/collect_env.py INFO 06-24 09:50:15 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /usr/local/lib/python3.10/dist-packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is replacing distutils. warnings.warn("Setuptools is replacing distutils.") ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.12 (main, Nov 6 2024, 20:22:13) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.2.140 CUD...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is replacing distutils. warnings.warn("Setuptools is replacing distutils.") ============================== System Info ============================== OS :...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: py INFO 06-24 09:50:15 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /usr/local/lib/python3.10/dist-packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is rep...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:239] Automatically detected platform cuda. Collecting environment information... /usr/local/lib/python3.10/dist-packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is replacing distutils. warnings.warn...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Prefix cache hit rate reach 60% for random data during benchmark? usage;stale ### Your current environment ```text root@llm206:/workspace/vllm# python3 ./vllm/collect_env.py INFO 06-24 09:50:15 [__init__.py:239] Automat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.2.1.post2+cu124torch2.6 [pip3] numpy==1.26.3 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
