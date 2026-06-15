# vllm-project/vllm#40081: [Bug]: vLLM fails to start on RDNA 4 (gfx1201) inside containers — amdsmi, circular import, and torch.cuda.device_count() all broken

| 字段 | 值 |
| --- | --- |
| Issue | [#40081](https://github.com/vllm-project/vllm/issues/40081) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe |
| 症状 | crash;import_error;oom |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vLLM fails to start on RDNA 4 (gfx1201) inside containers — amdsmi, circular import, and torch.cuda.device_count() all broken

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running vLLM inside a container on an RDNA 4 GPU (RX 9070 XT, gfx1201) hits **three sequential failures** that prevent the engine from starting. The GPU is fully functional via HIP — `hipGetDeviceCount()` returns 1, inference works once you get past these bugs. The issues are all in vLLM's platform detection and initialization path, not in the GPU or ROCm stack. I've published workaround patches and a full writeup at [sleeepss/vllm-rdna4-container-patches](https://github.com/sleeepss/vllm-rdna4-container-patches). Filing this to get the issues on upstream's radar. **Note:** I tested on v0.16.0rc0 via bluefalcon13/vllm-rocm. I've confirmed that `rocm_platform_plugin()` in `platforms/__init__.py` is still amdsmi-only on current main (no HIP fallback). Open issues #24576, #34573, and #39378 report the same detection failure on other hardware — this issue adds the RDNA 4 container-specific angle with root cause analysis and working patches. --- ### Bug 1: `amdsmi` fails to initialize → platform detection fails `vllm/platforms/__init__.py` → `rocm_platform_plugin()` calls `amdsmi` to detect ROCm. Inside a container, `amdsmi` fails wit...

## 现有链接修复摘要

#31062 [ROCm][Docker] Add gfx1103 support to Docker builds | #38086 [ROCm] Enable VLLM triton FP8 moe for gfx1201, tuned for Qwen3-30B-A3B-FP8 tp=2 and Qwen/Qwen3.5-35B-A3B-FP8 tp=2 | #41585 [ROCm] Fix platform detection failures in unprivileged containers

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ug]: vLLM fails to start on RDNA 4 (gfx1201) inside containers — amdsmi, circular import, and torch.cuda.device_count() all broken rocm ### Your current environment ### 🐛 Describe the bug Running vLLM inside a container...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: vLLM fails to start on RDNA 4 (gfx1201) inside containers — amdsmi, circular import, and torch.cuda.device_count() all broken rocm ### Your current environment ### 🐛 Describe the bug Running vLLM inside a contain...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: in `platforms/__init__.py` is still amdsmi-only on current main (no HIP fallback). Open issues #24576, #34573, and #39378 report the same detection failure on other hardware — this issue adds the RDNA 4 container-specif...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 0XTX + ROCm 7.2 + v0.19.0 (open) **vLLM — RDNA 4 specific:** - #28649 — FP8 WMMA feature request for gfx1201 (open) - #28052 — Flash attention error on gfx1201 in Docker (closed, fixed by PR #31062) - PR #38086 — FP8 Mo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: r or upstream in PyTorch's ROCm backend. ### Bonus: GGUF weight-loading OOM on 16 GB cards Not a code bug, but a sharp edge worth documenting. Once vLLM starts and begins loading a 14B Q4_K_M GGUF (~9 GB on disk), `_cre...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31062](https://github.com/vllm-project/vllm/pull/31062) | mentioned | 0.45 | [ROCm][Docker] Add gfx1103 support to Docker builds | 052 — flash attention error on gfx1201 in docker (closed, fixed by pr #31062) - pr #38086 — fp8 moe enabled for gfx1201 on main (merged apr 2, 2026) - pr #38455 — gfx1201 device i… |
| [#38086](https://github.com/vllm-project/vllm/pull/38086) | mentioned | 0.45 | [ROCm] Enable VLLM triton FP8 moe for gfx1201, tuned for Qwen3-30B-A3B-FP8 tp=2 and Qwen/Qwen3.5-35B-A3B-FP8 tp=2 | ttention error on gfx1201 in docker (closed, fixed by pr #31062) - pr #38086 — fp8 moe enabled for gfx1201 on main (merged apr 2, 2026) - pr #38455 — gfx1201 device id mapping add… |
| [#41585](https://github.com/vllm-project/vllm/pull/41585) | closes_keyword | 0.95 | [ROCm] Fix platform detection failures in unprivileged containers | Closes #40081 (Bug 1 + Bug 2) ### Root cause `rocm_platform_plugin()` relies solely on `amdsmi` to detect ROCm. `amdsmi` requires `/sys/bus/pci/drivers/amdgpu`, hwmon, and DRM sy |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
