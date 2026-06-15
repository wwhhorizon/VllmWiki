# vllm-project/vllm#38230: Hybrid KV offload: MultiConnector + planner for mamba+attention models

| 字段 | 值 |
| --- | --- |
| Issue | [#38230](https://github.com/vllm-project/vllm/issues/38230) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | attention;cache;fp8 |
| 症状 | crash |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Hybrid KV offload: MultiConnector + planner for mamba+attention models

### Issue 正文摘录

## Problem Hybrid models like Qwen3.5 (mamba + attention layers) can't use external KV cache offloading out of the box. The stock offload path requires LCM of all group block sizes, which is impractical for hybrid models where mamba groups have very different block sizes than attention groups. ## What we built A working hybrid offload stack for Qwen3.5-4B-FP8 (24 mamba + 8 attention layers), validated on RTX 4080 Super with `max_model_len=98304`: 1. **HybridOffloadPlanner** (`vllm/v1/kv_offload/planner.py`): configurable `hybrid_chunk_size` splits groups where `gpu_block_size % chunk_size == 0`, with per-group coverage tracking and binary search for efficient chunk counting. 2. **MultiConnector** (`multi_connector.py`): wraps multiple KV connectors (e.g., LMCache CPU + llm-d disk) with weighted load selection, HMA support (`SupportsHMA`), and preemption compatibility with stock vLLM's `set[str]` signature. 3. **Metrics safety**: clamp negative `prompt_tokens_by_source` values in `loggers.py` that crash Prometheus counters under high concurrency with external cache hits. ## Results - 79% cross-restart cache hit rate (llm-d disk, `PYTHONHASHSEED=0`) - 97% same-session hit rate (vLLM...

## 现有链接修复摘要

#2845 Fix docker python version | #38261 Hybrid KV offload: planner, MultiConnector, and mamba alignment for hybrid models

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: k_size == 0`, with per-group coverage tracking and binary search for efficient chunk counting. 2. **MultiConnector** (`multi_connector.py`): wraps multiple KV connectors (e.g., LMCache CPU + llm-d disk) with weighted lo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: groups. ## What we built A working hybrid offload stack for Qwen3.5-4B-FP8 (24 mamba + 8 attention layers), validated on RTX 4080 Super with `max_model_len=98304`: 1. **HybridOffloadPlanner** (`vllm/v1/kv_offload/planne...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Hybrid KV offload: MultiConnector + planner for mamba+attention models ## Problem Hybrid models like Qwen3.5 (mamba + attention layers) can't use external KV cache offloading out of the box. The stock offload path requi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d stack for Qwen3.5-4B-FP8 (24 mamba + 8 attention layers), validated on RTX 4080 Super with `max_model_len=98304`: 1. **HybridOffloadPlanner** (`vllm/v1/kv_offload/planner.py`): configurable `hybrid_chunk_size` splits...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: Hybrid KV offload: MultiConnector + planner for mamba+attention models ## Problem Hybrid models like Qwen3.5 (mamba + attention layers) can't use external KV cache offloading out of the box. The stock offload path requi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#2845](https://github.com/vllm-project/vllm/pull/2845) | mentioned | 0.45 | Fix docker python version | ibuted/kv_transfer/kv_connector/v1/`. related: lmcache/lmcache#2879, lmcache/lmcache#2845 > ai-assisted: developed with claude. all changes reviewed and tested by a human. |
| [#38261](https://github.com/vllm-project/vllm/pull/38261) | closes_keyword | 0.95 | Hybrid KV offload: planner, MultiConnector, and mamba alignment for hybrid models | Closes #38230 > AI-assisted: developed with Claude. All changes reviewed and tested by a human. 🤖 Generated with [Claude Code](https://claude.com/claude-code) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
