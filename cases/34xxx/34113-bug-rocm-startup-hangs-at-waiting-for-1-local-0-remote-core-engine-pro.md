# vllm-project/vllm#34113: [Bug][ROCm] Startup hangs at 'Waiting for 1 local, 0 remote core engine proc(s) to start' on AI MAX+ 395

| 字段 | 值 |
| --- | --- |
| Issue | [#34113](https://github.com/vllm-project/vllm/issues/34113) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm] Startup hangs at 'Waiting for 1 local, 0 remote core engine proc(s) to start' on AI MAX+ 395

### Issue 正文摘录

## Bug Report: vLLM hangs at startup on ROCm (AI MAX+ 395) ### Summary On Ubuntu 24.04, vLLM hangs during startup and keeps printing: `Waiting for 1 local, 0 remote core engine proc(s) to start.` I tested both: - vLLM `0.15.1` official wheel - self-built `0.15.2rc1.dev93+g11a4c9d30` (ROCm) In both cases, startup does not complete even after 2-3 hours. During the hang, one CPU thread stays at 100% usage. ### Environment - OS: Ubuntu 24.04 - Python env: Conda - GPU backend: ROCm - ROCm version: `7.2` - GPU: AMD AI MAX+ 395 (debug allocation currently ~32 GB on 8060S) - System and ROCm stack were installed by following AMD's official Ubuntu installation documentation. - vLLM versions tested: - `0.15.1` (official wheel) - `0.15.2rc1.dev93+g11a4c9d30` (self-built with ROCm 7.2) ### Environment Variables ```bash export VLLM_LOGGING_LEVEL=DEBUG export NCCL_DEBUG=INFO export FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" export PYTORCH_ROCM_ARCH="gfx1151" export NCCL_P2P_DISABLE=1 ``` ### Launch Command ```bash python3 -m vllm.entrypoints.openai.api_server \ --model /home/ragnarokchan/models/HY-MT1.5-7B \ --served-model-name HY-MT1.5-7B \ --trust-remote-code \ --gpu-memory-utilization 0.90 \ --...

## 现有链接修复摘要

#35304 [Bugfix][Hardware][AMD] Fix startup hang on ROCm gfx1151 in MinTokensLogitsProcessor

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: emote core engine proc(s) to start.` I tested both: - vLLM `0.15.1` official wheel - self-built `0.15.2rc1.dev93+g11a4c9d30` (ROCm) In both cases, startup does not complete even after 2-3 hours. During the hang, one CPU...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug][ROCm] Startup hangs at 'Waiting for 1 local, 0 remote core engine proc(s) to start' on AI MAX+ 395 rocm ## Bug Report: vLLM hangs at startup on ROCm (AI MAX+ 395) ### Summary On Ubuntu 24.04, vLLM hangs during sta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug][ROCm] Startup hangs at 'Waiting for 1 local, 0 remote core engine proc(s) to start' on AI MAX+ 395 rocm ## Bug Report: vLLM hangs at startup on ROCm (AI MAX+ 395) ### Summary On Ubuntu 24.04, vLLM hangs during sta...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 00% usage. ### Environment - OS: Ubuntu 24.04 - Python env: Conda - GPU backend: ROCm - ROCm version: `7.2` - GPU: AMD AI MAX+ 395 (debug allocation currently ~32 GB on 8060S) - System and ROCm stack were installed by f...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ngineCore_DP0 pid=14341) DEBUG ... Received init message: EngineHandshakeMetadata(...) (EngineCore_DP0 pid=14341) INFO ... Initializing a V1 LLM engine (...) ... (APIServer pid=14228) DEBUG ... Waiting for 1 local, 0 re...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35304](https://github.com/vllm-project/vllm/pull/35304) | closes_keyword | 0.95 | [Bugfix][Hardware][AMD] Fix startup hang on ROCm gfx1151 in MinTokensLogitsProcessor | Fixes #34113 ## Test plan - Verified the fix matches the existing `_device_tensor()` and `AllowedTokenIdsLogitsProcessor` patterns in the same file - No behavioral change for exi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
