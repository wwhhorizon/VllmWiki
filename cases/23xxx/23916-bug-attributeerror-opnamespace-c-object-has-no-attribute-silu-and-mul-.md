# vllm-project/vllm#23916: [Bug]: 'AttributeError: '_OpNamespace' '_C' object has no attribute 'silu_and_mul_nvfp4_quant'

| 字段 | 值 |
| --- | --- |
| Issue | [#23916](https://github.com/vllm-project/vllm/issues/23916) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'AttributeError: '_OpNamespace' '_C' object has no attribute 'silu_and_mul_nvfp4_quant'

### Issue 正文摘录

### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : 19.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.4.1 25184 c87081df219c42dc27c5b6d86c0525bc7d01f727) CMake version : version 3.31.6 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+gitf717b2a Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.4.43483-a187df25c ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-6.15.7-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : Radeon RX 7900 XTX (gfx1100) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP runtime version : 6.4.43483 MI...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : 19.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.4.1 25184 c87081df219c42dc27c5b6d86c0525b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: OpNamespace' '_C' object has no attribute 'silu_and_mul_nvfp4_quant' bug;rocm ### Your current environment Collecting environment information... ============================== System Info ==============================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 4_quant' bug;rocm ### Your current environment Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Mitigation; Clear Register File Vulnerability Retbleed: Not affected Vulnerability Spec rstack overf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ttributeError: '_OpNamespace' '_C' object has no attribute 'silu_and_mul_nvfp4_quant' bug;rocm ### Your current environment Collecting environment information... ============================== System Info ==============...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23921: Should have ROCm label: NO (0 matches) #23916: Should have ROCm label: YES (8 matches) • ROCm System Management Interface (keyword) in body: 1 matches |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
