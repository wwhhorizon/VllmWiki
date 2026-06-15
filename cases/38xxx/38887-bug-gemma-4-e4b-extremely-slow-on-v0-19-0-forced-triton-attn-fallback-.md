# vllm-project/vllm#38887: [Bug]: Gemma 4 E4B extremely slow on v0.19.0  forced TRITON_ATTN fallback yields ~9 tok/s on RTX 4090 (vs ~100+ tok/s for comparable Llama 3B)

| 字段 | 值 |
| --- | --- |
| Issue | [#38887](https://github.com/vllm-project/vllm/issues/38887) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;triton |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 E4B extremely slow on v0.19.0  forced TRITON_ATTN fallback yields ~9 tok/s on RTX 4090 (vs ~100+ tok/s for comparable Llama 3B)

### Issue 正文摘录

### Your current environment PyTorch version : 2.10.0+cu129 Python version : 3.12.13 (64-bit runtime) CUDA runtime version : 12.9.86 vLLM Version : 0.19.0 [pip3] torch==2.10.0+cu129 [pip3] transformers==5.5.0 [pip3] triton==3.6.0 [pip3] flashinfer-python==0.6.6 ### 🐛 Describe the bug Gemma 4 E4B (`google/gemma-4-e4b-it`, 4.5B effective parameters) generates at only **~9 tokens/s** on an RTX 4090 with vLLM v0.19.0. For comparison, a similarly-sized Llama 3.2 3B model on the same hardware with the same vLLM version generates at **100+ tokens/s**. The root cause is that Gemma 4's heterogeneous attention head dimensions force vLLM to disable FlashAttention and fall back to a much slower Triton attention kernel. Additionally, `custom_ops` is set to `['none']`, meaning no vLLM-native CUDA kernels are used. From vLLM server logs during inference: ``` INFO [config.py:104] Gemma4 model has heterogeneous head dimensions (head_dim=256, global_head_dim=512). Forcing TRITON_ATTN backend to prevent mixed-backend numerical divergence. INFO [cuda.py:274] Using AttentionBackendEnum.TRITON_ATTN backend. INFO [loggers.py:259] Engine 000: Avg prompt throughput: 1.6 tokens/s, Avg generation throughput...

## 现有链接修复摘要

#38891 [Gemma4] Allow per-layer attention backend selection for heterogeneou… | #42069 [Spec Decode] Allow DFlash drafter to autoselect non-causal-capable backend on Gemma 4

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: Gemma 4 E4B extremely slow on v0.19.0 forced TRITON_ATTN fallback yields ~9 tok/s on RTX 4090 (vs ~100+ tok/s for comparable Llama 3B) bug ### Your current environment PyTorch version : 2.10.0+cu129 Python versio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: .6 tokens/s, Avg generation throughput: 9.2 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 1.9%, Prefix cache hit rate: 94.9% ``` Expected behavior A 4.5B parameter model on an RTX 4090 (24GB VRAM, BF16...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: al_head_dim=512). Forcing TRITON_ATTN backend to prevent mixed-backend numerical divergence. INFO [cuda.py:274] Using AttentionBackendEnum.TRITON_ATTN backend. INFO [loggers.py:259] Engine 000: Avg prompt throughput: 1....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma 4 E4B extremely slow on v0.19.0 forced TRITON_ATTN fallback yields ~9 tok/s on RTX 4090 (vs ~100+ tok/s for comparable Llama 3B) bug ### Your current environment PyTorch version : 2.10.0+cu129 Python
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tok/s for comparable Llama 3B) bug ### Your current environment PyTorch version : 2.10.0+cu129 Python version : 3.12.13 (64-bit runtime) CUDA runtime version : 12.9.86 vLLM Version : 0.19.0 [pip3] torch==2.10.0+cu129 [p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38891](https://github.com/vllm-project/vllm/pull/38891) | closes_keyword | 0.95 | [Gemma4] Allow per-layer attention backend selection for heterogeneou… | Fix #38887: Gemma 4 models are extremely slow on vLLM v0.19.0 (~9 tok/s on RTX 4090 for E4B) because `Gemma4Config` forces **all** layers to use `TRITON_ATTN`, even though |
| [#42069](https://github.com/vllm-project/vllm/pull/42069) | mentioned | 0.6 | [Spec Decode] Allow DFlash drafter to autoselect non-causal-capable backend on Gemma 4 | on the same prompt set - [ ] CI ## Related - Filed issue: #42068 - #38887 — Gemma 4 E4B slow on TRITON_ATTN (open since v0.19.0) - #41789 — Gemma 4 31B MTP draft acceptance 0.2% (… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
