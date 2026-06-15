# vllm-project/vllm#42655: [Bug]: Async double streaming_update can break the request ID -> previous batch row mapping and crash the engine

| 字段 | 值 |
| --- | --- |
| Issue | [#42655](https://github.com/vllm-project/vllm/issues/42655) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;nondeterministic |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Async double streaming_update can break the request ID -> previous batch row mapping and crash the engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen2-0.5B` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a double-`streaming_update` bug in the `AsyncLLM` path that can break the worker's request ID -> previous batch row mapping for a resumed request and then kill the engine. The reproducer submits one resumable request and then applies two legal `streaming_update` operations to that same live request while async scheduling and speculative decoding are both active. Under that combination, the scheduler can continue issuing speculative decode positions for the resumed request, but the worker-side request ID -> previous batch row mapping no longer matches the live request state. The verified `AsyncLLM` runs then reach a worker update step where the request id is missing from `prev_req_id_to_index`, and the engine dies with: - `scheduled_spec_decode_tokens={...: [-1, ...]}` - `KeyError: 'req2-...'` - `EngineDeadError` This is not the same bug as: - the async same-request-id reuse underflow bug - the resumed prompt-width overflow bug ## Trigger chain 1. Submit a live mixed batch so async sch...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen2-0.5B` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a double-`streaming_upd...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Async double streaming_update can break the request ID -> previous batch row mapping and crash the engine bug ### Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: be the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen2-0.5B` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a double-`streaming_update` bug in the `AsyncLLM` path that can break the worke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: .1` Model: `Qwen/Qwen2-0.5B` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a double-`streaming_update` bug in the `AsyncLLM` path that can break the worker's request ID -> previous bat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen2-0.5B` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a double-`streaming_update` bug in the `AsyncLLM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
