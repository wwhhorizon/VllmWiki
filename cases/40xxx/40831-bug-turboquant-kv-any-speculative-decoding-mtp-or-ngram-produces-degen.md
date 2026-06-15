# vllm-project/vllm#40831: [Bug]: TurboQuant KV × any speculative decoding (MTP or ngram) produces degenerate token loops — confirmed across dense and hybrid attention

| 字段 | 值 |
| --- | --- |
| Issue | [#40831](https://github.com/vllm-project/vllm/issues/40831) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: TurboQuant KV × any speculative decoding (MTP or ngram) produces degenerate token loops — confirmed across dense and hybrid attention

### Issue 正文摘录

### Summary When MTP speculative decoding is combined with any TurboQuant KV preset (`turboquant_3bit_nc`, `turboquant_4bit_nc`, `turboquant_k8v4`) on a Qwen3-Next hybrid model (DeltaNet + attention — here Qwen3.6-27B Lorbus int4-AutoRound), the model emits degenerate token loops on any workload that requires structured or exact output: - **Tool-call prompts** loop: ` ...` emitted as plain text; `tool_calls[]` never populated. - **Long-context recall** loops: needle-in-haystack retrieves the first token of the secret then loops (e.g. `"amber amber amber..."`, `"turqururur..."` at 10K–90K depths). - **Streaming** occasionally loops: `"Wait, I I I I I..."` on open-ended generation. Short narrative / code completions look fine, which is why initial benchmarks passed. **Isolation:** MTP alone is fine (fp8_e5m2 KV + MTP → all tests pass). TurboQuant alone is fine (turboquant_3bit_nc, no spec-decode → all tests pass). Only the combination fails. Tested all three TurboQuant presets; all fail with MTP. MTP `num_speculative_tokens` 1 and 3 both fail. This is distinct from the CUDA-graph capture crash in #40807 (which is a prerequisite just to reach inference — the output-quality bug is obs...

## 现有链接修复摘要

#38479 [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity | #43747 [Bugfix][TurboQuant] Fix CUDA graph capture crash with spec-decode + chunked-prefill (#40807)

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: TP `num_speculative_tokens` 1 and 3 both fail. This is distinct from the CUDA-graph capture crash in #40807 (which is a prerequisite just to reach inference — the output-quality bug is observed on top of the CUDA-graph...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: TurboQuant KV × any speculative decoding (MTP or ngram) produces degenerate token loops — confirmed across dense and hybrid attention ### Summary When MTP speculative decoding is combined with any TurboQuant KV p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: : https://github.com/noonghunna/qwen36-27b-single-3090/blob/main/compose/docker-compose.longctx-experimental.yml Run `scripts/verify-full.sh` against it — tool-call (step 4) and long-ctx-recall (step 7) fail with degene...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: TurboQuant KV × any speculative decoding (MTP or ngram) produces degenerate token loops — confirmed across dense and hybrid attention ### Summary When MTP speculative decoding is combined with any TurboQuant KV p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ion. Short narrative / code completions look fine, which is why initial benchmarks passed. **Isolation:** MTP alone is fine (fp8_e5m2 KV + MTP → all tests pass). TurboQuant alone is fine (turboquant_3bit_nc, no spec-dec...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38479](https://github.com/vllm-project/vllm/pull/38479) | mentioned | 0.45 | [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity | ause the distribution doesn't collapse there — consistent with the pr #38479 benchmarks (which measured throughput + gsm8k + niah on `qwen3-4b`, a non-hybrid non-spec-dec model) s… |
| [#43747](https://github.com/vllm-project/vllm/pull/43747) | closes_keyword | 0.95 | [Bugfix][TurboQuant] Fix CUDA graph capture crash with spec-decode + chunked-prefill (#40807) | closed, workaround via Genesis P65) - #40831 — TurboQuant × any spec-decode produces degenerate loops (closed) - #42544 — workspace allocation assertion (open, addressed by #42551) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
