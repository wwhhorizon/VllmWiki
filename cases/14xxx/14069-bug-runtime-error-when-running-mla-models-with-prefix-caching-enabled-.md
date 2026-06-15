# vllm-project/vllm#14069: [Bug]: Runtime error when running MLA models with "prefix caching enabled" and "chunked prefill disabled"

| 字段 | 值 |
| --- | --- |
| Issue | [#14069](https://github.com/vllm-project/vllm/issues/14069) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Runtime error when running MLA models with "prefix caching enabled" and "chunked prefill disabled"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **TL;DR:** This bug will happen when running MLA models (i.e., deepseek R1) with - enable prefixing caching - disable chunked prefill ### Detailed explanation: In #12639 , a few new variables related to chunked prefill and a new function called `_compute_prefill_context` are introduced in class `MLACommonBackend`. The `_compute_prefill_context` function will be called when prefix caching is enabled. It uses the new variables related to chunked prefill (e.g., `context_chunk_cu_seq_lens`, `context_chunk_starts`, `context_chunk_seq_tot`, and `context_chunk_max_seq_lens`). However, if chunked prefill is **not** enabled, those variables will be None and cause the above assertion error. ### Example script: ```bash vllm serve cognitivecomputations/DeepSeek-R1-AWQ \ --trust-remote-code \ --tensor-parallel-size 8 \ --gpu-memory-utilization 0.9 \ --dtype float16 \ --max-model-len 32768 \ --max-num-batched-tokens 32768 \ --enforce-eager \ --disable-log-requests \ --enable-chunked-prefill false \ --enable-prefix-caching ``` To reproduce the bug, send two requests to the serving engine with the same prefix. ### Error logs: **Key part:** ```pl...

## 现有链接修复摘要

#12639 [Attention] MLA with chunked prefill

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: error when running MLA models with "prefix caching enabled" and "chunked prefill disabled" bug;stale ### Your current environment ### 🐛 Describe the bug **TL;DR:** This bug will happen when running MLA models (i.e., dee...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding attention;cuda;operato...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --tensor-parallel-size 8 \ --gpu-memory-utilization 0.9 \ --dtype float16 \ --max-model-len 32768 \ --max-num-batched-tokens 32768 \ --enforce-eager \ --disable-log-requests \ --enable-chunked-prefill false \ --enable-p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: y:141] AssertionError ``` @LucasWilkinson @pathorn @simon-mo @tlrmchlsmth PTAL 🙏 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tion called `_compute_prefill_context` are introduced in class `MLACommonBackend`. The `_compute_prefill_context` function will be called when prefix caching is enabled. It uses the new variables related to chunked pref...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#12639](https://github.com/vllm-project/vllm/pull/12639) | mentioned | 0.45 | [Attention] MLA with chunked prefill | ing caching - disable chunked prefill ### detailed explanation: in #12639 , a few new variables related to chunked prefill and a new function called `_compute_prefill_context` are… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
