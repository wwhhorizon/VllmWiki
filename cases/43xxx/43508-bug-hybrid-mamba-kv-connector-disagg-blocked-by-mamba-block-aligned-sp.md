# vllm-project/vllm#43508: [Bug]: Hybrid Mamba + KV connector disagg blocked by _mamba_block_aligned_split assertion (NemotronH-550B repro)

| 字段 | 值 |
| --- | --- |
| Issue | [#43508](https://github.com/vllm-project/vllm/issues/43508) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | cache |
| 症状 | crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Hybrid Mamba + KV connector disagg blocked by _mamba_block_aligned_split assertion (NemotronH-550B repro)

### Issue 正文摘录

## Your current environment - **vLLM**: `0.19.0` (running inside the `nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.0.1` overlay image — `dynamo-vllm-efa`) - **Hardware**: 2× `p5en.48xlarge` (16× H200 total), EFA, NIXL + LIBFABRIC transport - **Model**: `nvidia/Nemotron-3-Ultra-550B-A55B-RL` (NemotronH SSM-Hybrid) - **Topology**: Disaggregated serving via LeaderWorkerSet, `--disaggregation-mode prefill` and `--disaggregation-mode decode`, NixlConnector - **Flags**: `--no-disable-hybrid-kv-cache-manager` (i.e. hybrid KV cache manager enabled), `mamba_cache_mode == "align"` ## Describe the bug The unconditional assertion in `vllm/v1/core/sched/scheduler.py::_mamba_block_aligned_split`: ```python assert num_external_computed_tokens == 0, \ "External KV connector is not verified yet" ``` fires on the **first inference request** whenever a Mamba-Hybrid model is run with `mamba_cache_mode == \"align\"` **and** a `NixlConnector` (or any external KV connector) is attached. This makes disaggregated serving impossible for any Mamba-Hybrid family on stock vLLM — the EngineCore subprocess crashes the moment a request reaches the scheduler. This is the same assertion @NickLucche tried to remove in #...

## 现有链接修复摘要

#36687 [PD][Nixl] Add support for hybrid SSM-FA models | #42522 [BugFix] Set mamba_block_size to max_model_len for KV consumers in align mode

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ogy**: Disaggregated serving via LeaderWorkerSet, `--disaggregation-mode prefill` and `--disaggregation-mode decode`, NixlConnector - **Flags**: `--no-disable-hybrid-kv-cache-manager` (i.e. hybrid KV cache manager enabl...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: ggregation-mode decode`, NixlConnector - **Flags**: `--no-disable-hybrid-kv-cache-manager` (i.e. hybrid KV cache manager enabled), `mamba_cache_mode == "align"` ## Describe the bug The unconditional assertion in `vllm/v...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Hybrid Mamba + KV connector disagg blocked by _mamba_block_aligned_split assertion (NemotronH-550B repro) ## Your current environment - **vLLM**: `0.19.0` (running inside the `nvcr.io/nvidia/ai-dynamo/vllm-runtim...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nt (Karpenter node consolidation), so the end-to-end path is not yet exercised. However, the **engine-init-time assertion that previously blocked startup is bypassed**, which validates the patch concept on a non-Jamba S...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ransport - **Model**: `nvidia/Nemotron-3-Ultra-550B-A55B-RL` (NemotronH SSM-Hybrid) - **Topology**: Disaggregated serving via LeaderWorkerSet, `--disaggregation-mode prefill` and `--disaggregation-mode decode`, NixlConn...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36687](https://github.com/vllm-project/vllm/pull/36687) | mentioned | 0.45 | [PD][Nixl] Add support for hybrid SSM-FA models | ect-fix attempt; we have now validated its concept on nemotronh. - pr #36687 — the merged connector-side support that this scheduler bug now blocks for mamba-hybrid. ## before sub… |
| [#42522](https://github.com/vllm-project/vllm/pull/42522) | mentioned | 0.45 | [BugFix] Set mamba_block_size to max_model_len for KV consumers in align mode | mitting a new issue... - [x] searched existing issues; #41515 and pr #42522 are the closest matches. filing a fresh issue because (a) #41515 is filed against a different surface (… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
