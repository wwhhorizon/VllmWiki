# vllm-project/vllm#36865: [Bug]: SM120 / RTX 5090 source build still registers unsupported FlashMLA / FA targets and uses non-SM120 Marlin defaults.

| 字段 | 值 |
| --- | --- |
| Issue | [#36865](https://github.com/vllm-project/vllm/issues/36865) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;hardware_porting;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;kernel;moe;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SM120 / RTX 5090 source build still registers unsupported FlashMLA / FA targets and uses non-SM120 Marlin defaults.

### Issue 正文摘录

## System Info * GPU: **NVIDIA GeForce RTX 5090** (Blackwell **SM120 / compute capability 12.0**) * Driver 595.45.04 - CUDA 13.2 * OS: Ubuntu 24.04.x LTS x86_64 * Python: 3.11.14 (venv) - Python 3.12.12 (system) * vLLM: `0.17.2.dev0+g95c0f928c.d20260312.cu132` * PyTorch: `2.10.0+cu130` * Flashinfer: `0.6.6+sm120` ### ✔️ SM120 (OK) * CUTLASS SM120 kernels * NVFP4 SM120 * MLA SM120 * moe_data SM120 * general SM120 codegen (`compute_120f`, `sm_120f`) ### ❌ Not SM120 * Marlin → need SM120 forcing / 8.0+PTX * Marlin‑MOE → need SM120 forcing / 8.0+PTX * FlashMLA → should be skipped/disabled on SM120, FlashMLA kernels only work on Hopper and require CUDA 12.3+, so on SM120 the correct action is to guard it out and disable its targets? * FA2_ARCHS → pip/setuptools still asks Ninja for_vllm_fa2_C / _vllm_fa3_C /_vllm_fa4_cutedsl_C

## 现有链接修复摘要

#36873 [ROCm] Fix build issues with cub:: namespace and missing headers

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 8: [Bug]: SM120 / RTX 5090 source build still registers unsupported FlashMLA / FA targets and uses non-SM120 Marlin defaults. bug ## System Info * GPU: **NVIDIA GeForce RTX 5090** (Blackwell **SM120 / compute capability 12...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: LM: `0.17.2.dev0+g95c0f928c.d20260312.cu132` * PyTorch: `2.10.0+cu130` * Flashinfer: `0.6.6+sm120` ### ✔️ SM120 (OK) * CUTLASS SM120 kernels * NVFP4 SM120 * MLA SM120 * moe_data SM120 * general SM120 codegen (`compute_1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: SM120 / RTX 5090 source build still registers unsupported FlashMLA / FA targets and uses non-SM120 Marlin defaults. bug ## System Info * GPU: **NVIDIA GeForce RTX 5090** (Blackwell **SM120 / compute capability 12...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Flashinfer: `0.6.6+sm120` ### ✔️ SM120 (OK) * CUTLASS SM120 kernels * NVFP4 SM120 * MLA SM120 * moe_data SM120 * general SM120 codegen (`compute_120f`, `sm_120f`) ### ❌ Not SM120 * Marlin → need SM120 forcing / 8.0+PTX...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ### ✔️ SM120 (OK) * CUTLASS SM120 kernels * NVFP4 SM120 * MLA SM120 * moe_data SM120 * general SM120 codegen (`compute_120f`, `sm_120f`) ### ❌ Not SM120 * Marlin → need SM120 forcing / 8.0+PTX * Marlin‑MOE → need SM120...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36873](https://github.com/vllm-project/vllm/pull/36873) | closes_keyword | 0.95 | [ROCm] Fix build issues with cub:: namespace and missing headers | Fixes #36865 <!-- markdownlint-disable --> ## Purpose ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
