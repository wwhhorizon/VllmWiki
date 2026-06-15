# vllm-project/vllm#16676: [Bug]: Enabling LoRA not working with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#16676](https://github.com/vllm-project/vllm/issues/16676) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Enabling LoRA not working with vLLM

### Issue 正文摘录

### Your current environment The output of `python collect_env.py` ``INFO 04-15 18:22:30 [__init__.py:239] Automatically detected platform rocm. Collecting environment information... PyTorch version: 2.7.0a0+git28b68b4 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42134-a9a80e791 OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 18.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.3.4 25012 e5bf7e55c91490b07c49d8960fa7983d864936c4) CMake version: version 3.31.6 Libc version: glibc-2.35 Python version: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb 6 2025, 18:56:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.5.0-21-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Instinct MI300X (gfx942:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.3.42134 MIOpen runtime version: 3.3.0 Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits...

## 现有链接修复摘要

#17492 [Bugfix] Adding maxnreg to lora expand/shrink kernel definition | #17677 [Bugfix] LoRA - Retire unused maxnreg LoRA kernel argument

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ly detected platform rocm. Collecting environment information... PyTorch version: 2.7.0a0+git28b68b4 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42134-a9a80e791 OS: Ubuntu 22.04...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: ``INFO 04-15 18:22:30 [__init__.py:239] Automatically detected platform rocm. Collecting environment information... PyTorch version: 2.7.0a0+git28b68b4 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mitigation; Sp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:239] Automatically detected platform rocm. Collecting environment information... PyTorch version: 2.7.0a0+git28b68b4 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42134-a9a80...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17492](https://github.com/vllm-project/vllm/pull/17492) | closes_keyword | 0.95 | [Bugfix] Adding maxnreg to lora expand/shrink kernel definition | FIX #16676 <!--- pyml disable-next-line no-emphasis-as-heading --> |
| [#17677](https://github.com/vllm-project/vllm/pull/17677) | closes_keyword | 0.95 | [Bugfix] LoRA - Retire unused maxnreg LoRA kernel argument | FIX #16676 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
