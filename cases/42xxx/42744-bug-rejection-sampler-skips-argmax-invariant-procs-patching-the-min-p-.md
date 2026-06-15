# vllm-project/vllm#42744: [Bug]: rejection sampler skips argmax-invariant procs — patching the min_p/logit_bias 400 alone is insufficient

| 字段 | 值 |
| --- | --- |
| Issue | [#42744](https://github.com/vllm-project/vllm/issues/42744) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: rejection sampler skips argmax-invariant procs — patching the min_p/logit_bias 400 alone is insufficient

### Issue 正文摘录

The guard at `vllm/sampling_params.py:_validate_spec_decode` 400s any spec-decode request with `min_p > _SAMPLING_EPS` or `logit_bias` set (added in #31982). Patching the raise out locally to let the params through reveals the underlying gap: the rejection sampler at `vllm/v1/sample/rejection_sampler.py:apply_logits_processors` only iterates `sampling_metadata.logitsprocs.non_argmax_invariant`. Both `MinPLogitsProcessor.is_argmax_invariant()` and `LogitBiasLogitsProcessor.is_argmax_invariant()` return `True` — the comment in `vllm/v1/sample/logits_processor/builtin.py` even says "Min-p never impacts greedy sampling". Net: even with the guard removed, min_p / logit_bias are NOT applied to verified target-logit tokens during rejection. They'd only land on bonus tokens via the regular Sampler path. Inconsistent honoring across a single response, arguably worse than the current 400 if a caller assumed they'd taken effect. Two ways to close this properly: 1. Mirror the regular Sampler in `apply_logits_processors` and include argmax-invariant procs (preserves determinism for greedy callers via the existing sampling_metadata check). 2. Route requests with `min_p`/`logit_bias` set to a no...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: one is insufficient The guard at `vllm/sampling_params.py:_validate_spec_decode` 400s any spec-decode request with `min_p > _SAMPLING_EPS` or `logit_bias` set (added in #31982). Patching the raise out locally to let the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: the guard as a hard fallback. ## Repro ``` vllm serve --speculative-config '{"method":"ngram","num_speculative_tokens":5}' curl /v1/chat/completions -d '{"messages":[...], "min_p":0.05}' # 400 BadRequest: "The min_p and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: oding." ``` ## Context Hitting this running `RedHatAI/Qwen3-Coder-Next-NVFP4` with ngram speculative decoding on a DGX Spark (GB10 / sm_121a) via the Avarok-Cybersecurity/dgx-vllm fork. Qwen-family AWQ/NVFP4 leans on `m...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t to a non-spec target when they're present, leaving the guard as a hard fallback. ## Repro ``` vllm serve --speculative-config '{"method":"ngram","num_speculative_tokens":5}' curl /v1/chat/completions -d '{"messages":[...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: gmax-invariant procs — patching the min_p/logit_bias 400 alone is insufficient The guard at `vllm/sampling_params.py:_validate_spec_decode` 400s any spec-decode request with `min_p > _SAMPLING_EPS` or `logit_bias` set (...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
