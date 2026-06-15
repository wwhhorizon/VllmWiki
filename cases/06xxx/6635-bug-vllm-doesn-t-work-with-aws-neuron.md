# vllm-project/vllm#6635: [Bug]: vllm doesn't work with AWS neuron

| 字段 | 值 |
| --- | --- |
| Issue | [#6635](https://github.com/vllm-project/vllm/issues/6635) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm doesn't work with AWS neuron

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNING 07-22 07:34:58 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/ubuntu/vllm/vllm/usage/usage_lib.py:19: RuntimeWarning: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-1022-aws-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: nment information... WARNING 07-22 07:34:58 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/ubuntu/vllm/vllm/usage/usage_lib.py:19: RuntimeWarning: Failed to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ion__ as VLLM_VERSION PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ```text The output of `python collect_env.py` Collecting environment information... WARNING 07-22 07:34:58 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/ubu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm doesn't work with AWS neuron bug;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNING 07-22 07:34:58 _custom_ops.py:14] Failed to imp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ] transformers==4.42.4 [pip3] transformers-neuronx==0.10.20240710 [pip3] triton==2.1.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: (0, 'instance-type: inf2.24xlarge\ninstance-id: i-0113...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
