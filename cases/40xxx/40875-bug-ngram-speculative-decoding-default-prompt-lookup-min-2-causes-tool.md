# vllm-project/vllm#40875: [Bug]: ngram speculative decoding default prompt_lookup_min=2 causes tool-call output corruption on Qwen3-class models with structured output (config-only fix: prompt_lookup_min=8)

| 字段 | 值 |
| --- | --- |
| Issue | [#40875](https://github.com/vllm-project/vllm/issues/40875) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;fp8;kernel;moe;sampling |
| 症状 | nondeterministic;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: ngram speculative decoding default prompt_lookup_min=2 causes tool-call output corruption on Qwen3-class models with structured output (config-only fix: prompt_lookup_min=8)

### Issue 正文摘录

### Summary When using `--speculative-config '{"method":"ngram","prompt_lookup_min":2,...}'` (the default `prompt_lookup_min`) with a Qwen3-class model AND `tool_choice=auto` requests AND a tools array in the system prompt, **tool-call output is corrupted in ~50% of requests** even on a stack with all known related fixes applied (#40738 Phase 1+2, #36138, #40783, #39055). The corruption manifests as wrong-token cascades like ` \n \nprint(...)`, `parameter=parameter=name`, ` ... ` instead of the correct chat-template format ` \n \n \nVALUE\n ...`. **Config-only workaround (no code changes): set `prompt_lookup_min=8`. Achieves 100% clean tool-call rate (n=30 single-query, 96% n=25 multi-query) on the same hardware/model where default `prompt_lookup_min=2` gave ~50%.** This is a separate bug class from PR #40738 (GDN state corruption, which we backported and confirmed gives +30-40% improvement). The remaining ~50% residual that the four upstream PRs don't close is the rejection-sampling artifact described here. ### Environment - vLLM: `0.19.2rc1.dev205+g07351e088` (latest nightly tested) - Model: `Qwen3.6-35B-A3B-FP8` (hybrid linear-attention + MoE + full-attention layers) - Hardware...

## 现有链接修复摘要

#40738 [Bugfix] Fix GDN conv + SSM state corruption with ngram spec decode | #40768 [Bugfix][Scheduler] Fix CUDA crash caused by stale async placeholder tokens in speculative decoding

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: ngram speculative decoding default prompt_lookup_min=2 causes tool-call output corruption on Qwen3-class models with structured output (config-only fix: prompt_lookup_min=8) ### Summary When using `--speculative-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: id linear-attention + MoE + full-attention layers) - Hardware: 2× NVIDIA RTX A5000 (Ampere SM 8.6), TP=2 - KV cache: `turboquant_k8v4` - Speculative config: `{"method":"ngram","num_speculative_tokens":3,"prompt_lookup_m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: coding default prompt_lookup_min=2 causes tool-call output corruption on Qwen3-class models with structured output (config-only fix: prompt_lookup_min=8) ### Summary When using `--speculative-config '{"method":"ngram","...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: g`: `false` - `--enable-chunked-prefill`, `--enable-prefix-caching` ### Reproducer ```python import json import requests PROMPT = { "model": "Qwen/Qwen3.6-35B-A3B-FP8", "messages": [{"role": "user", "content": "Get weat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e-chunked-prefill`, `--enable-prefix-caching` ### Reproducer ```python import json import requests PROMPT = { "model": "Qwen/Qwen3.6-35B-A3B-FP8", "messages": [{"role": "user", "content": "Get weather for Tokyo"}], "too...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40738](https://github.com/vllm-project/vllm/pull/40738) | mentioned | 0.45 | [Bugfix] Fix GDN conv + SSM state corruption with ngram spec decode | whose work narrowed our search: - @tdoublep + @bhaktatejas922 — [vllm#40738](https://github.com/vllm-project/vllm/pull/40738) / [vllm#39273](https://github.com/vllm-project/vllm/i… |
| [#40768](https://github.com/vllm-project/vllm/pull/40768) | mentioned | 0.45 | [Bugfix][Scheduler] Fix CUDA crash caused by stale async placeholder tokens in speculative decoding | soning embedded tool_call xml extraction) - @z1ying + @sweihub — [vllm#40768](https://github.com/vllm-project/vllm/pull/40768) / [vllm#37159](https://github.com/vllm-project/vllm/… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
