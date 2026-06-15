# vllm-project/vllm#16632: [Usage]: [swift with vllm and only using vllm serve]  leads to different result（10% diff）

| 字段 | 值 |
| --- | --- |
| Issue | [#16632](https://github.com/vllm-project/vllm/issues/16632) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: [swift with vllm and only using vllm serve]  leads to different result（10% diff）

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` **~ $ python collect_env.py** INFO 04-15 11:43:18 __init__.py:190] Automatically detected platform cuda. Collecting environment information... /home/work/py39/lib/python3.9/site-packages/_distutils_hack/__init__.py:26: UserWarning: Setuptools is replacing distutils. warnings.warn("Setuptools is replacing distutils.") PyTorch version: 2.5.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 12.1.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.17 Python version: 3.9.2 (default, Mar 3 2021, 20:02:32) [GCC 7.3.0] (64-bit runtime) Python platform: Linux-5.10.0-1.0.0.34-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 10.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10 GPU 1: NVIDIA A10 Nvidia driver version: 535.154.05 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: packages/_distutils_hack/__init__.py:26: UserWarning: Setuptools is replacing distutils. warnings.warn("Setuptools is replacing distutils.") PyTorch version: 2.5.1+cu118 Is debug build: False CUDA used to build PyTorch:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: y** INFO 04-15 11:43:18 __init__.py:190] Automatically detected platform cuda. Collecting environment information... /home/work/py39/lib/python3.9/site-packages/_distutils_hack/__init__.py:26: UserWarning: Setuptools is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:190] Automatically detected platform cuda. Collecting environment information... /home/work/py39/lib/python3.9/site-packages/_distutils_hack/__init__.py:26: UserWarning: Setuptools is replacing distutils. warnings....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lm and only using vllm serve] leads to different result（10% diff） usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` **~ $ python collect_env.py** INFO 04-15 11:43:18 __init__.py:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: sformers==4.49.0.dev0 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.7.2 vLLM Build Flags: CUDA Archs:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
