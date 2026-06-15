# vllm-project/vllm#7166: [Bug]: vLLM latest version on Inf2 fails

| 字段 | 值 |
| --- | --- |
| Issue | [#7166](https://github.com/vllm-project/vllm/issues/7166) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;import_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM latest version on Inf2 fails

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNING 08-05 17:30:24 _custom_ops.py:15] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-1031-aws-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Vendor ID: AuthenticAMD Model name: AMD EPYC 7R13 Processor CPU family: 25 Model: 1 Thread(s) per co...

## 现有链接修复摘要

#9257 [Doc][Neuron] add note to neuron documentation about resolving triton issue

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: vLLM latest version on Inf2 fails bug ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNING 08-05 17:30:24 _custom_ops.py:15] Failed to import fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ule named 'vllm._C'") PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ```text The output of `python collect_env.py` Collecting environment information... WARNING 08-05 17:30:24 _custom_ops.py:15] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: module named 'vllm._C'") PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9257](https://github.com/vllm-project/vllm/pull/9257) | closes_keyword | 0.95 | [Doc][Neuron] add note to neuron documentation about resolving triton issue | FIX #7166 (*link existing issues this PR will resolve*) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
