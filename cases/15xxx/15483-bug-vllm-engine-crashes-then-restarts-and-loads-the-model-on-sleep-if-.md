# vllm-project/vllm#15483: [Bug]: vLLM engine crashes then restarts and loads the model on sleep if a chat request is made

| 字段 | 值 |
| --- | --- |
| Issue | [#15483](https://github.com/vllm-project/vllm/issues/15483) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM engine crashes then restarts and loads the model on sleep if a chat request is made

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # 🐛 Bug: Server crashes when making completion requests to a sleeping model When using vLLM's sleep mode functionality through the `/sleep`, `/wake_up`, and `/is_sleeping` endpoints, the server crashes with a CUDA error if a completion request is made while the model is in sleep mode. ## Steps to Reproduce 1. Start a vLLM server 2. Put the model to sleep with a POST request to `/sleep` 3. Attempt to make a completion request with endpoints like `/v1/chat/completions` or `/v1/completions` The server immediately crashes with a CUDA memory access error, requiring a restart. ## Expected Behavior When making a completion request to a sleeping model, the server should either: - Automatically and gracefully wake up the model first - Return a proper error response indicating the model is sleeping and needs to be woken up ## Actual Behavior The server crashes with an error like: ``` CUDA error: an illegal memory access was encountered RuntimeError: CUDA error: an illegal memory access was encountered ``` Full crash log ``` vllm | INFO 03-25 16:01:40 [engine.py:310] Added request cmpl-0750d012ef7140d1b80c8768ae5ef193-0. vllm | CRITICAL 03-...

## 现有链接修复摘要

#16536 Fix #15483 : Add error handling for model-dependent endpoints during sleep mode | #30186 Fix #15483 : Add error handling for model-dependent endpoints during …

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ht be incorrect.\nFor debugging consider passing CUDA_LAUNCH_BLOCKING=1\nCompile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.\n') vllm | ERROR 03-25 16:01:40 [engine.py:160] Traceback (most recent call la...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: vLLM engine crashes then restarts and loads the model on sleep if a chat request is made bug;stale ### Your current environment ### 🐛 Describe the bug # 🐛 Bug: Server crashes when making completion requests to a sleepin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ep`, `/wake_up`, and `/is_sleeping` endpoints, the server crashes with a CUDA error if a completion request is made while the model is in sleep mode. ## Steps to Reproduce 1. Start a vLLM server 2. Put the model to slee...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ne.py:160] File "/opt/venv/lib/python3.12/site-packages/vllm/attention/backends/flash_attn.py", line 756, in forward vllm | ERROR 03-25 16:01:40 [engine.py:160] flash_attn_varlen_func( vllm | ERROR 03-25 16:01:40 [engin...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ompletion request is made while the model is in sleep mode. ## Steps to Reproduce 1. Start a vLLM server 2. Put the model to sleep with a POST request to `/sleep` 3. Attempt to make a completion request with endpoints l...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#16536](https://github.com/vllm-project/vllm/pull/16536) | closes_keyword | 0.95 | Fix #15483 : Add error handling for model-dependent endpoints during sleep mode | FIX #15483 ## Solution Added a middleware that checks if the model is sleeping before processing requests to endpoints that require model access. When the model is sleeping, these |
| [#30186](https://github.com/vllm-project/vllm/pull/30186) | closes_keyword | 0.95 | Fix #15483 : Add error handling for model-dependent endpoints during … | FIX for existing issue #15483) We initially created the PR https://github.com/vllm-project/vllm/pull/16536 which was closed due to time and I'm creating a new one from the suggest |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
