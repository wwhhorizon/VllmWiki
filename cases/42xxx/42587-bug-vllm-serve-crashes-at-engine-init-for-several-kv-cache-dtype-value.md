# vllm-project/vllm#42587: [Bug]: vllm serve crashes at engine init for several --kv-cache-dtype values accepted by CLI (fp8_ds_mla, fp8_e5m2, fp8_inc, bfloat16)

| 字段 | 值 |
| --- | --- |
| Issue | [#42587](https://github.com/vllm-project/vllm/issues/42587) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve crashes at engine init for several --kv-cache-dtype values accepted by CLI (fp8_ds_mla, fp8_e5m2, fp8_inc, bfloat16)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Several `--kv-cache-dtype` values that are accepted by the CLI crash during engine initialization because the attention layer's internal dtype check only recognizes a subset of the advertised values. The affected values are `fp8_ds_mla`, `fp8_e5m2`, and `fp8_inc`. In each case the server loads the model successfully but then fails during the profiling run with an internal assertion or `ValueError`, well after significant initialization work has already been done. Additionally, `--kv-cache-dtype bfloat16` is also accepted by the CLI but crashes even earlier — at attention backend selection — because no available backend supports it as a KV cache dtype. All four values share the same root problem: they are accepted at the CLI boundary but rejected much later by internal runtime checks, with no early validation to catch the incompatibility upfront. ## Steps to Reproduce **Case 1: `--kv-cache-dtype fp8_ds_mla`** ```bash vllm serve \ --host 127.0.0.1 \ --port 19411 \ --kv-cache-dtype fp8_ds_mla ``` **Case 2: `--kv-cache-dtype fp8_e5m2`** ```bash vllm serve \ --host 127.0.0.1 \ --port 19412 \ --kv-cache-dtype fp8_e5m2 ``` **Case 3: `--...

## 现有链接修复摘要

#42685 [FlashAttn] Fix supports_kv_cache_dtype() accepting unhandled fp8 kv-cache dtype variants

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: vllm serve crashes at engine init for several --kv-cache-dtype values accepted by CLI (fp8_ds_mla, fp8_e5m2, fp8_inc, bfloat16) bug ### Your current environment ### 🐛 Describe the bug Several `--kv-cache-dtype` v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: t16` is also accepted by the CLI but crashes even earlier — at attention backend selection — because no available backend supports it as a KV cache dtype. All four values share the same root problem: they are accepted a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: er pid=1017428) INFO 05-14 09:09:58 [api_server.py:1272] vLLM API server version 0.14.1 (APIServer pid=1017428) INFO 05-14 09:09:58 [utils.py:263] non-default args: {'model_tag': '/root/.cache/modelscope/hub/models/LLM-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Using max model len 131072 (APIServer pid=1017428) INFO 05-14 09:09:58 [scheduler.py:229] Chunked prefill is enabled with max_num_batched_tokens=8192. (APIServer pid=1017428) INFO 05-14 09:09:58 [vllm.py:630] Asynchrono...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: vllm serve crashes at engine init for several --kv-cache-dtype values accepted by CLI (fp8_ds_mla, fp8_e5m2, fp8_inc, bfloat16) bug ### Your current environment ### 🐛 Describe the bug Several `--kv-cache-dtype` v...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42685](https://github.com/vllm-project/vllm/pull/42685) | closes_keyword | 0.95 | [FlashAttn] Fix supports_kv_cache_dtype() accepting unhandled fp8 kv-cache dtype variants | Fixes #42587. ## Test Plan New regression tests added to `tests/kernels/attention/test_attention_selector.py`: - `test_flash_attn_rejects_unhandled_kv_cache_dtypes` — para |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
