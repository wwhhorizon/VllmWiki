# vllm-project/vllm#42619: [Bug]: Structured-output scheduler can keep advancing a terminated xgrammar matcher

| 字段 | 值 |
| --- | --- |
| Issue | [#42619](https://github.com/vllm-project/vllm/issues/42619) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Structured-output scheduler can keep advancing a terminated xgrammar matcher

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen3-0.6B-GPTQ-Int8` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a structured-output lifecycle bug in the xgrammar path. In a frontend-legal structured-output workload, a structured-output request can already reach a terminated xgrammar matcher state, but later scheduler iterations still try to advance that same matcher with more generated tokens. On the re-verified Qwen3 AsyncLLM runs from May 14, 2026, this reproduces 2/2 times and leaves a stable internal error surface in the engine logs: ```text Failed to advance FSM Unexpected: grammar rejected tokens The matcher has terminated ... but is trying to accept new token ``` This is not a malformed-input bug. The request shape is legal. The problem is that the terminated grammar state is not consistently honored across the structured-output scheduling path. ## Trigger chain 1. Start a legal structured-output request with xgrammar enabled. 2. Keep a live mixed batch running so speculative decoding and multi-step scheduling remain active around that structured-output request. 3. The structur...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Structured-output scheduler can keep advancing a terminated xgrammar matcher bug ### Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen3-0.6B-GPTQ-Int8` Ha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: l: `Qwen/Qwen3-0.6B-GPTQ-Int8` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a structured-output lifecycle bug in the xgrammar path. In a frontend-legal structured-output workload, a s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen3-0.6B-GPTQ-Int8` Hardware reproduced on: `NVIDIA GeForce RTX 4090`, single GPU ## Summary I found a structured-output lifecycle bug in t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Structured-output scheduler can keep advancing a terminated xgrammar matcher bug ### Your current environment ### 🐛 Describe the bug # Describe the bug Version: vLLM `0.17.1` Model: `Qwen/Qwen3-0.6B-GPTQ-Int8` Ha...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rnal failures. ## Details ### Trigger path in code 1. In the xgrammar backend, `accept_tokens()` returns `False` once the matcher is already terminated or if `accept_token()` fails for a new token. ```python # vllm/v1/s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
