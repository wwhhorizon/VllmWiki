# vllm-project/vllm#37801: [Bug]: CUDA 13 LMCache KV connector install path still resolves CUDA 12 artifacts

| 字段 | 值 |
| --- | --- |
| Issue | [#37801](https://github.com/vllm-project/vllm/issues/37801) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA 13 LMCache KV connector install path still resolves CUDA 12 artifacts

### Issue 正文摘录

## Summary The current LMCache KV-connector installation path in `vllm/vllm-openai:latest-cu130` is not compatible with the latest LMCache integration stack. In a CUDA 13 container derived from `vllm/vllm-openai:latest-cu130`, enabling the LMCache connector can fail before serving starts because the install path still pulls CUDA 12-oriented artifacts. ## Reproduction Environment used for validation: - Podman - NVIDIA RTX 4080 SUPER - driver `595.45.04` - host CUDA `13.2` - base image `vllm/vllm-openai:latest-cu130` Minimal reproduction shape: 1. Start from `vllm/vllm-openai:latest-cu130`. 2. Install LMCache through the current KV-connector path. 3. Import `lmcache.integration.vllm.vllm_v1_adapter` or start `vllm serve` with `LMCacheConnectorV1`. Observed failure: ```text ImportError: libcudart.so.12: cannot open shared object file ``` ## Expected behavior The CUDA 13 image path should install CUDA 13-compatible KV-connector dependencies so that LMCache can be imported and used without falling back to CUDA 12 artifacts. ## Root cause hypothesis The CUDA 13 image path still assumes the generic / CUDA 12-oriented LMCache packaging path. In practice, the working CUDA 13 combination re...

## 现有链接修复摘要

#37802 [CI/Build] Fix LMCache KV connector install path for CUDA 13 images | #42771 [CI/Build] Resolve LMCache wheels by CUDA major

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: CUDA 13 LMCache KV connector install path still resolves CUDA 12 artifacts ## Summary The current LMCache KV-connector installation path in `vllm/vllm-openai:latest-cu130` is not compatible with the latest LMCach...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: CUDA 13 LMCache KV connector install path still resolves CUDA 12 artifacts ## Summary The current LMCache KV-connector installation path in `vllm/vllm-openai:latest-cu130` is not compatible with the latest LMCach...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: uilt a CUDA 13 image on top of `vllm/vllm-openai:latest-cu130` - served `Qwen/Qwen3-0.6B` - enabled `LMCacheConnectorV1` - confirmed `LocalCPUBackend` and `LocalDiskBackend` creation - confirmed disk offload writes - co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ed `Qwen/Qwen3-0.6B` - enabled `LMCacheConnectorV1` - confirmed `LocalCPUBackend` and `LocalDiskBackend` creation - confirmed disk offload writes - confirmed replay cache hits - confirmed OpenAI-compatible responses exp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: DiskBackend` creation - confirmed disk offload writes - confirmed replay cache hits - confirmed OpenAI-compatible responses expose `usage.prompt_tokens_details.cached_tokens` when both: - `--enable-prompt-tokens-details...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37802](https://github.com/vllm-project/vllm/pull/37802) | closes_keyword | 0.95 | [CI/Build] Fix LMCache KV connector install path for CUDA 13 images | Fixes #37801. This updates the CUDA 13 KV-connector install path so `vllm/vllm-openai:latest-cu130` can be layered with LMCache without pulling CUDA 12-oriented artifacts. Relate |
| [#42771](https://github.com/vllm-project/vllm/pull/42771) | closes_keyword | 0.95 | [CI/Build] Resolve LMCache wheels by CUDA major | Fixes #37801. The CUDA 13 optional KV connector Docker install currently lets the generic `lmcache >= 0.3.9` requirement resolve to whatever the latest LMCache wheel is. That was |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
