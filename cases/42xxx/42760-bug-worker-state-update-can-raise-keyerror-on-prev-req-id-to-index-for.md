# vllm-project/vllm#42760: [Bug]: Worker state update can raise KeyError on prev_req_id_to_index for a resumed AsyncLLM request

| 字段 | 值 |
| --- | --- |
| Issue | [#42760](https://github.com/vllm-project/vllm/issues/42760) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Worker state update can raise KeyError on prev_req_id_to_index for a resumed AsyncLLM request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: local GraniteMoE checkpoint used for repro Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found an async `streaming_update` bug in the `AsyncLLM` path that can crash the engine with a worker-side `KeyError`. The reproducer keeps one other live request active so speculative decoding stays enabled, then starts one resumable live request (`req0`) and sends two legal `streaming_update`s to that same live request. Under that combination, the scheduler still emits speculative decode tokens for `req0`, for example: ```text scheduled_spec_decode_tokens={req0-...: [-1, -1, -1, -1]} ``` But by the time the worker updates the cached request state for the next async iteration, that same `req0` is no longer present in `prev_req_id_to_index`. On the re-verified standalone `AsyncLLM` run from `2026-05-16`, the reproducer then crashes in `gpu_model_runner.py:1104` with: ```text KeyError: 'req0-...' ``` This is not the same issue as: - the Qwen double-`streaming_update` row-mapping issue that was already filed - the shared-prefix `-1` placeholder leak issue In this repro...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: local GraniteMoE checkpoint used for repro Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I foun...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: update can raise KeyError on prev_req_id_to_index for a resumed AsyncLLM request bug ### Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: local GraniteMoE checkpoint used...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: eMoE checkpoint used for repro Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found an async `streaming_update` bug in the `AsyncLLM` path that can crash the engine with a worker-side `KeyErr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: local GraniteMoE checkpoint used for repro Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found an async `streaming_upd...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: This is not the same issue as: - the Qwen double-`streaming_update` row-mapping issue that was already filed - the shared-prefix `-1` placeholder leak issue In this reproduction, the visible sink is: `scheduled_spec_dec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
