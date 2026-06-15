# vllm-project/vllm#42492: [Bug]: Async cancel/resubmit with reused runtime request id can drive num_output_placeholders below zero

| 字段 | 值 |
| --- | --- |
| Issue | [#42492](https://github.com/vllm-project/vllm/issues/42492) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Async cancel/resubmit with reused runtime request id can drive num_output_placeholders below zero

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen3-0.6B-GPTQ-Int8` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a frontend-legal async request-identity bug. The reproducer first queues work for one live request (`req2a`), then cancels that request, and finally submits a new request (`req2b`) that reuses the same runtime request id (`late_req2`). Because the old async batch is still queued, draining that old batch later can apply its output to the new live request object instead of the cancelled one. When that happens, vLLM decrements `request.num_output_placeholders` on the wrong request object and the async scheduler invariant below fails: ```text assert request.num_output_placeholders >= 0 ``` This is not a malformed-input bug. The workload is frontend-legal. The failure comes from stale queued output being rebound to the wrong live request after runtime request id reuse. This issue is different from the double-`streaming_update` row-mapping issue. This one specifically depends on `cancel -> resubmit with the same runtime request id -> drain old queued batch`. ## Trigger chain 1. Su...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Async cancel/resubmit with reused runtime request id can drive num_output_placeholders below zero bug ### Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen3-0.6B-GPTQ-Int8` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a frontend-le...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: l: `Qwen/Qwen3-0.6B-GPTQ-Int8` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a frontend-legal async request-identity bug. The reproducer first queues work for one live request (`req2a`...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen3-0.6B-GPTQ-Int8` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a frontend-legal async request-identit...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding cuda;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf dty...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
