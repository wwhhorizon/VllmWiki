# vllm-project/vllm#6261: [Bug]: ModuleNotFoundError: No module named 'outlines.caching'

| 字段 | 值 |
| --- | --- |
| Issue | [#6261](https://github.com/vllm-project/vllm/issues/6261) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ModuleNotFoundError: No module named 'outlines.caching'

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 07-09 19:49:30 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.3.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.11.9 | packaged by conda-forge | (main, Apr 19 2024, 18:36:13) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-6.5.0-35-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 24 On-line CPU(s) list: 0-23 Vendor ID: GenuineIntel Model name: 13th Gen Intel(R) Core(TM) i7-13700 CPU family: 6 Model: 183 Thread(s) per c...

## 现有链接修复摘要

#6262 [BugFix]: set outlines pkg version

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: nment information... WARNING 07-09 19:49:30 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.3.0+cpu Is debug build: False CUDA used to build PyTo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: odule named 'vllm._C'") PyTorch version: 2.3.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: hing' bug ### Your current environment ```text Collecting environment information... WARNING 07-09 19:49:30 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mitigation; Sp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: onnx==1.16.1 [pip3] torch==2.3.0+cpu [pip3] transformers==4.41.2 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.1 vLLM Build Flags: CUDA Archs: N...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6262](https://github.com/vllm-project/vllm/pull/6262) | closes_keyword | 0.95 | [BugFix]: set outlines pkg version | FIX #6261 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering d |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
