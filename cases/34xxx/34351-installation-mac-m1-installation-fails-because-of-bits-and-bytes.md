# vllm-project/vllm#34351: [Installation]: MAC M1 installation fails because of bits-and-bytes

| 字段 | 值 |
| --- | --- |
| Issue | [#34351](https://github.com/vllm-project/vllm/issues/34351) |
| 状态 | open |
| 标签 | installation;unstale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: MAC M1 installation fails because of bits-and-bytes

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : macOS 15.6.1 (arm64) GCC version : Could not collect Clang version : 17.0.0 (clang-1700.0.13.5) CMake version : version 4.0.2 Libc version : N/A ============================== PyTorch Info ============================== PyTorch version : 2.10.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)] (64-bit runtime) Python platform : macOS-15.6.1-arm64-arm-64bit ============================== CUDA / GPU Info ============================== Is CUDA available : False CUDA runtime version : No CUDA CUDA_MODULE_LOADING set to : N/A GPU models and configuration : No CUDA Nvidia driver version : No CUDA cuDNN version : No CUDA HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ============================== CPU Info ============================== Apple M1 Pro ============================== Versions of rel...

## 现有链接修复摘要

#41345 [Installation] Make bitsandbytes, runai-model-streamer, and mamba-ssm optional for macOS | #41347 [Installation] Make bitsandbytes and runai-model-streamer optional for macOS

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: MAC M1 installation fails because of bits-and-bytes installation;unstale ### Your current environment ```text Collecting environment information... ============================== System Info =====
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Torch version : 2.10.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: n;unstale ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : macOS 15.6.1 (arm64) GCC version : Could not collect Cl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: = PyTorch version : 2.10.0 Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ion]: MAC M1 installation fails because of bits-and-bytes installation;unstale ### Your current environment ```text Collecting environment information... ============================== System Info ======================...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41345](https://github.com/vllm-project/vllm/pull/41345) | closes_keyword | 0.95 | [Installation] Make bitsandbytes, runai-model-streamer, and mamba-ssm optional for macOS | Fixes #34351 ## Additional Notes - `bitsandbytes` is only used for quantization features - `runai-model-streamer` is only available for Linux x86_64 - `mamba-ssm` requires CUDA ( |
| [#41347](https://github.com/vllm-project/vllm/pull/41347) | closes_keyword | 0.95 | [Installation] Make bitsandbytes and runai-model-streamer optional for macOS | Fixes #34351 ## Additional Notes - Uses precise platform conditions as suggested by Gemini Code Review - `bitsandbytes` is only used for quantization features - `runai-model-stre |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
