# vllm-project/vllm#34303: [RFC]: CUDA Checkpoint/Restore for Near-Zero Cold Starts

| 字段 | 值 |
| --- | --- |
| Issue | [#34303](https://github.com/vllm-project/vllm/issues/34303) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;kernel |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: CUDA Checkpoint/Restore for Near-Zero Cold Starts

### Issue 正文摘录

### Motivation. > **Issue:** [vllm-project/vllm#33930](https://github.com/vllm-project/vllm/issues/33930) > **Scope:** v1 engine only > **Status:** Draft ## Motivation Cold start latency is a major barrier for several important use cases: - **Multi-model serving:** Swapping between models on shared GPUs requires full teardown and re-initialization, taking 30–120s depending on model size. - **Scale-to-zero serverless:** Platforms that scale GPU workloads to zero pay the full cold start penalty on every scale-up, making sub-minute response SLAs impossible for large models. - **Cost-efficient hosting:** Providers cannot amortize GPU costs across many models if each model swap requires a lengthy restart, making per-request billing impractical. Modal has demonstrated [10x cold start improvements](https://modal.com/blog/gpu-mem-snapshots) using the CUDA checkpoint API with vLLM, and InferX has reportedly built similar functionality on top of vLLM. While [AI Dynamo's chrek](https://github.com/ai-dynamo/dynamo/tree/main/deploy/chrek) provides an open-source CRIU + CUDA checkpoint orchestrator, no inference engine currently offers this as a native, built-in capability. ### What cold start...

## 现有链接修复摘要

#35934 feat: add suspend()/resume() for CRIU-safe snapshots | #37921 [Core] CUDA Checkpoint/Restore — Phase 1: C Extension, Python Wrapper, Worker Methods | #42874 Release stale CUDA primary contexts inherited by forked workers | #44074 [Core] Pluggable sleep-mode backend abstraction (RFC #34303)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Draft ## Motivation Cold start latency is a major barrier for several important use cases: - **Multi-model serving:** Swapping between models on shared GPUs requires full teardown and re-initialization, taking 30–120s d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: t latency is a major barrier for several important use cases: - **Multi-model serving:** Swapping between models on shared GPUs requires full teardown and re-initialization, taking 30–120s depending on model size. - **S...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [RFC]: CUDA Checkpoint/Restore for Near-Zero Cold Starts RFC ### Motivation. > **Issue:** [vllm-project/vllm#33930](https://github.com/vllm-project/vllm/issues/33930) > **Scope:** v1 engine only > **Status:** Draft ## M...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: apture (~2-10s) 6. NCCL initialization for tensor parallelism (~1-3s) 7. KV cache allocation and profiling (~1-2s) Steps 3–5 are the most expensive and are precisely what CUDA checkpoint/restore eliminates entirely. ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: llm-project/vllm/issues/33930) > **Scope:** v1 engine only > **Status:** Draft ## Motivation Cold start latency is a major barrier for several important use cases: - **Multi-model serving:** Swapping between models on s...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35934](https://github.com/vllm-project/vllm/pull/35934) | mentioned | 0.6 | feat: add suspend()/resume() for CRIU-safe snapshots | ing engine as unhealthy during suspend (raised by @aerialhedgehog in [#34303 comment](https://github.com/vllm-project/vllm/issues/34303#issuecomment-2958756773)) cc @elizabetht @n… |
| [#37921](https://github.com/vllm-project/vllm/pull/37921) | mentioned | 0.6 | [Core] CUDA Checkpoint/Restore — Phase 1: C Extension, Python Wrapper, Worker Methods | - Not duplicating any existing PR — this is new functionality per RFC #34303. |
| [#42874](https://github.com/vllm-project/vllm/pull/42874) | closes_keyword | 0.95 | Release stale CUDA primary contexts inherited by forked workers | Fixes #42873 ## Context Discovered while integrating NVIDIA cuda-checkpoint with vLLM for multi-GPU cold start optimization (related to RFC #34303). The stale inherited contexts |
| [#44074](https://github.com/vllm-project/vllm/pull/44074) | mentioned | 0.6 | [Core] Pluggable sleep-mode backend abstraction (RFC #34303) | es - `cuda_checkpoint` stays the canonical built-in either way. Refs #34303 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
