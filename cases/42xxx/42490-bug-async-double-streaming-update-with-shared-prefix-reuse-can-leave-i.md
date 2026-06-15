# vllm-project/vllm#42490: [Bug]: Async double streaming_update with shared-prefix reuse can leave invalid -1 token ids in the worker input row

| 字段 | 值 |
| --- | --- |
| Issue | [#42490](https://github.com/vllm-project/vllm/issues/42490) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Async double streaming_update with shared-prefix reuse can leave invalid -1 token ids in the worker input row

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen3-0.6B-GPTQ-Int8` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a frontend-legal request-lifecycle bug in the resumable `streaming_update` path. The reproducer sends one live request (`req2`) and then legally updates the same request twice with `streaming_update`. While those two updates are being processed, async queue lag and shared-prefix reuse are both still active. Under that combination, vLLM rebuilds the renewed `req2` state, schedules speculative placeholder tokens for it, but the worker-side input row is no longer fully backed by real token ids. As a result, the prepared host-side input row for `req2` contains `-1` values before model execution starts. On the re-verified Qwen3 standalone run, the visible non-blocking failure is a CUDA `device-side assert` in the FlashAttention execution path. The important point is that the bad row already exists before the GPU failure. This is not a random backend crash, and it is not the same issue as the same-id placeholder-underflow bug or the older prompt-width overflow bug. ## Trigger chai...

## 现有链接修复摘要

#42519 [Bugfix] Fix async double streaming_update placeholder bug (#42490)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: IDIA GeForce RTX 4090`, single GPU ## Summary I found a frontend-legal request-lifecycle bug in the resumable `streaming_update` path. The reproducer sends one live request (`req2`) and then legally updates the same req...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen3-0.6B-GPTQ-Int8` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a frontend-le...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: l: `Qwen/Qwen3-0.6B-GPTQ-Int8` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a frontend-legal request-lifecycle bug in the resumable `streaming_update` path. The reproducer sends one l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen3-0.6B-GPTQ-Int8` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a frontend-legal request-lifecycle bug...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: , the visible non-blocking failure is a CUDA `device-side assert` in the FlashAttention execution path. The important point is that the bad row already exists before the GPU failure. This is not a random backend crash,...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42519](https://github.com/vllm-project/vllm/pull/42519) | closes_keyword | 0.95 | [Bugfix] Fix async double streaming_update placeholder bug (#42490) | Fixes #42490. This PR resolves a scheduler/worker state mismatch in the v1 engine that can cause `CUDA error: device-side assert triggered` under a specific combination of fea |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
