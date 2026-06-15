# vllm-project/vllm#35755: [Bug]: AsyncScheduler crashes with AssertionError during Realtime ASR streaming (num_output_placeholders underflow)

| 字段 | 值 |
| --- | --- |
| Issue | [#35755](https://github.com/vllm-project/vllm/issues/35755) |
| 状态 | open |
| 标签 | stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;multimodal_vlm;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm |
| 症状 | crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AsyncScheduler crashes with AssertionError during Realtime ASR streaming (num_output_placeholders underflow)

### Issue 正文摘录

## Bug Description The vLLM engine crashes with a fatal `AssertionError` in `AsyncScheduler._update_request_with_output` when using the Realtime WebSocket API (`/v1/realtime`) with Qwen3-ASR. The crash is caused by `request.num_output_placeholders` going negative, which kills the entire `EngineCore` process. The bug is an interaction between two features that were never tested together: - **PR #33652** (Feb 4) refactored `AsyncScheduler._update_after_schedule` to skip placeholder increment when `is_prefill_chunk=True` - **PR #34613** (Feb 20) added Qwen3-ASR realtime streaming, which sends multiple audio segments as streaming input chunks There are currently **no tests** that combine streaming input with `AsyncScheduler`. ## Root Cause The Realtime ASR buffer splits audio into 5-second segments plus a short tail flush (e.g. 0.9 seconds). Each segment is submitted to the engine as a `StreamingInput` via `_update_request_as_session`. When the short tail segment arrives: 1. `_update_request_as_session` extends `num_tokens` (new prompt tokens), but `num_computed_tokens` stays at its previous value. 2. `_update_after_schedule` in `scheduler.py` computes: ```python request.is_prefill_ch...

## 现有链接修复摘要

#39642 [Realtime][Video] Add streaming video input for real-time video understanding

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: AsyncScheduler crashes with AssertionError during Realtime ASR streaming (num_output_placeholders underflow) stale ## Bug Description The vLLM engine crashes with a fatal `AssertionError` in `AsyncScheduler._upda...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: with_output` when using the Realtime WebSocket API (`/v1/realtime`) with Qwen3-ASR. The crash is caused by `request.num_output_placeholders` going negative, which kills the entire `EngineCore` process. The bug is an int...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ltime mode: ```bash vllm serve Qwen/Qwen3-ASR-1.7B \ --hf-overrides '{"architectures": ["Qwen3ASRRealtimeGeneration"]}' \ --max-model-len 4096 \ --limit-mm-per-prompt '{"audio": 1}' \ --enforce-eager ``` 2. Send audio (...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ack to prefill via `_update_request_as_session`. ## Environment - vLLM version: `0.1.dev14351+gbbf81f9a9.d20260302` (main branch HEAD) - Model: `Qwen/Qwen3-ASR-1.7B` with `Qwen3ASRRealtimeGeneration` architecture - GPU:...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: rectness frontend_api;model_support;multimodal_vlm;scheduler_memory cuda;gemm crash;nan_inf env_dependency #39642 [Realtime][Video] Add streaming video input for real-time video understanding Bug Description

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39642](https://github.com/vllm-project/vllm/pull/39642) | closes_keyword | 0.95 | [Realtime][Video] Add streaming video input for real-time video understanding | fixes #35755) \| \| `vllm/model_executor/models/interfaces.py` \| `supports_realtime_video()` → opt-in interface for future models \| \| `vllm/model_executor/models/qwen3_vl.py` \| `su |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
