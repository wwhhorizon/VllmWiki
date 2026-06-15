# vllm-project/vllm#16886: [Usage]: Deciding max-num-seqs and max-num-batched-tokens for desired throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#16886](https://github.com/vllm-project/vllm/issues/16886) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Deciding max-num-seqs and max-num-batched-tokens for desired throughput

### Issue 正文摘录

### Your current environment output of python collect_env.py ```text INFO 04-20 11:27:48 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /workspace/vllm/inference/lib/python3.10/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml warnings.warn( PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.10.12 (main, Feb 4 2025, 14:57:36) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-44-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 Nvidia driver version: 560.35.03 cuDNN version: Probably one of the follow...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Usage]: Deciding max-num-seqs and max-num-batched-tokens for desired throughput usage;stale ### Your current environment output of python collect_env.py ```text INFO 04-20 11:27:48 [__init__.py:239] Automatically detec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: xt INFO 04-20 11:27:48 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /workspace/vllm/inference/lib/python3.10/site-packages/_distutils_hack/__init__.py:30: UserWarning: Se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: _.py:239] Automatically detected platform cuda. Collecting environment information... /workspace/vllm/inference/lib/python3.10/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: x async abort: Not affected Versions of relevant libraries: [pip3] flashinfer-python==0.2.5+cu124torch2.6 [pip3] numpy==2.2.5 [pip3] nvidia-cublas-cu12==12.4.5.8 [pip3] nvidia-cuda-cupti-cu12==12.4.127 [pip3] nvidia-cud...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: tches we can process at once on 24G with 6G model and 18G free space for kv-cache When I run the same on H100 (80G vRAM): My calculations suggest it should work for ``` max-num-batched-tokens : 65536*4 max-num-seqs : 64...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
