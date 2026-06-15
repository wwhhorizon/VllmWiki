# vllm-project/vllm#41390: [Performance]: Llama-Nemotron embedding is slower than Transformers for offline batch-32 pooling after compile-cache warmup

| 字段 | 值 |
| --- | --- |
| Issue | [#41390](https://github.com/vllm-project/vllm/issues/41390) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;nondeterministic;slowdown |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Llama-Nemotron embedding is slower than Transformers for offline batch-32 pooling after compile-cache warmup

### Issue 正文摘录

## Proposal to improve performance I do not have a specific implementation proposal yet. I am filing this with a standalone MRE because vLLM appears slower than a direct Hugging Face Transformers embedding path for a small/medium offline embedding workload, even after separating startup time and rerunning vLLM after the torch.compile cache is populated. This may be related to the existing embedding optimization RFC: - https://github.com/vllm-project/vllm/issues/21796 ## Report of performance regression I am comparing offline embedding throughput for `nvidia/llama-nemotron-embed-1b-v2`, a supported `LlamaBidirectionalModel` pooling/embedding model. The workload is intended to mimic a recall/query embedding path: - deterministic short natural-language queries - `query: ` prefix - batch size 32 - input length around 32 words per query - no OpenAI server, no HTTP serialization, no external dataset - model already present in the Hugging Face cache for the measured startup numbers - no explicit vLLM pooler override - explicit vLLM pooling runner, matching NeMo Retriever's local vLLM helper - explicit vLLM `FLASH_ATTN` attention backend, matching NeMo Retriever's local vLLM helper - vLLM...

## 现有链接修复摘要

#41678 Improve offline embedding throughput for pooling models

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: embedding is slower than Transformers for offline batch-32 pooling after compile-cache warmup ## Proposal to improve performance I do not have a specific implementation proposal yet. I am filing this with a standalone M...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: Llama-Nemotron embedding is slower than Transformers for offline batch-32 pooling after compile-cache warmup ## Proposal to improve performance I do not have a specific implementation proposal yet. I am f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ps://github.com/vllm-project/vllm/issues/21796 ## Report of performance regression I am comparing offline embedding throughput for `nvidia/llama-nemotron-embed-1b-v2`, a supported `LlamaBidirectionalModel` pooling/embed...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ears slower than a direct Hugging Face Transformers embedding path for a small/medium offline embedding workload, even after separating startup time and rerunning vLLM after the torch.compile cache is populated. This ma...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: eMo Retriever's local vLLM helper - explicit vLLM `FLASH_ATTN` attention backend, matching NeMo Retriever's local vLLM helper - vLLM progress bars disabled during timed embedding calls - vLLM run with `max_model_len=819...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41678](https://github.com/vllm-project/vllm/pull/41678) | closes_keyword | 0.95 | Improve offline embedding throughput for pooling models | fix for #41390. ## Review Follow-up Required Before this PR is marked ready, address the review-flagged safety items: check `tokenizer is None` before accessing tokenizer attribu |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
