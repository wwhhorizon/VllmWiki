# vllm-project/vllm#37714: [Installation]: Blackwell SM120 + CUDA 13 pip install: 5 sequential failures before Qwen3.5 27B+ runs

| 字段 | 值 |
| --- | --- |
| Issue | [#37714](https://github.com/vllm-project/vllm/issues/37714) |
| 状态 | open |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;triton |
| 症状 | build_error;crash;import_error;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Installation]: Blackwell SM120 + CUDA 13 pip install: 5 sequential failures before Qwen3.5 27B+ runs

### Issue 正文摘录

### Your current environment Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Mar 3 2026, 12:15:18) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.6.87.2-microsoft-standard-WSL2-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX PRO 5000 Blackwell Nvidia driver version : 595.79 cuDNN version : Could not collect ============================== CPU Info ============================== Architecture: x86_64 Model name: Intel(R) Core(TM)...

## 现有链接修复摘要

#14221 [V1][Bugfix] Standardize quantized kv cache rejection for attention backends | #37757 [UX] Logging - Improve Startup Error Logs

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 12: [Installation]: Blackwell SM120 + CUDA 13 pip install: 5 sequential failures before Qwen3.5 27B+ runs installation ### Your current environment Collecting environment information...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Installation]: Blackwell SM120 + CUDA 13 pip install: 5 sequential failures before Qwen3.5 27B+ runs installation ### Your current environment Collecting environment information...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: --- ### Problem 4: `--attention-backend FLASH_ATTN` + `--kv-cache-dtype fp8` = silent crash **Error** (again, buried in EngineCore subprocess): ``` ValueError: Selected backend AttentionBackendEnum.FLASH_ATTN is not val...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.4 [pip3] numpy==2.2.6 [pip3] nvidia-cuda-runtime==13.0.96 [pip3] nvidia-cuda-runtime-cu12==12.9.79
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: h version : 2.10.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#14221](https://github.com/vllm-project/vllm/pull/14221) | mentioned | 0.45 | [V1][Bugfix] Standardize quantized kv cache rejection for attention backends | d or remove --kv-cache-dtype fp8." **related:** #12543, #35577, pr #14221 --- ### problem 5: "engine core initialization failed" provides no useful information ``` runtimee |
| [#37757](https://github.com/vllm-project/vllm/pull/37757) | closes_keyword | 0.95 | [UX] Logging - Improve Startup Error Logs | Fixes #31683. Also addresses #37714. ## Summary This PR scopes #31683 to startup failures only, matching the guidance in the issue thread. - propagate structured startup fai |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
