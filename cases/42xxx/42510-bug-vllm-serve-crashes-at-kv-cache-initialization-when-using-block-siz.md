# vllm-project/vllm#42510: [Bug]: vllm serve crashes at KV cache initialization when using --block-size 1 or 8 despite being listed as valid choices

| 字段 | 值 |
| --- | --- |
| Issue | [#42510](https://github.com/vllm-project/vllm/issues/42510) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve crashes at KV cache initialization when using --block-size 1 or 8 despite being listed as valid choices

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When passing `--block-size 1` or `--block-size 8` to `vllm serve`, the CLI explicitly lists both values as valid choices (`choose from 1, 8, 16, 32, 64, 128, 256`), but the server crashes during KV cache initialization with `ValueError: No common block size for 1.` The same model and configuration starts successfully with `--block-size 16`. This is a contract violation: the CLI advertises these values as supported, but the engine rejects them at runtime after significant initialization work (model loading, torch.compile, etc.) has already completed. ## Steps to Reproduce ```bash vllm serve \ --host 127.0.0.1 \ --port 19399 \ --block-size 1 ``` The same crash is expected with `--block-size 8`. Using `--block-size 16` starts successfully. ``` (vllm) root@lizhiyuan-ubuntu-01:~# /root/anaconda3/envs/vllm/bin/vllm serve /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct --host 127.0.0.1 --port 19399 --block-size 1 (APIServer pid=928798) INFO 05-13 16:41:24 [api_server.py:1272] vLLM API server version 0.14.1 (APIServer pid=928798) INFO 05-13 16:41:24 [utils.py:263] non-default args: {'model_tag': '/root/.cache...

## 现有链接修复摘要

#42682 fix: validate backend block size earlier | #43514 [Bugfix] Reject non-positive block_size in CacheConfig

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ssing `--block-size 1` or `--block-size 8` to `vllm serve`, the CLI explicitly lists both values as valid choices (`choose from 1, 8, 16, 32, 64, 128, 256`), but the server crashes during KV cache initialization with `V...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e initialization with `ValueError: No common block size for 1.` The same model and configuration starts successfully with `--block-size 16`. This is a contract violation: the CLI advertises these values as supported, bu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ] Using max model len 131072 (APIServer pid=928798) INFO 05-13 16:41:24 [scheduler.py:229] Chunked prefill is enabled with max_num_batched_tokens=8192. (APIServer pid=928798) INFO 05-13 16:41:24 [vllm.py:630] Asynchrono...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42682](https://github.com/vllm-project/vllm/pull/42682) | closes_keyword | 0.95 | fix: validate backend block size earlier | Fixes #42510. ## Summary - validate user-specified block sizes against the selected attention backend before KV cache setup - report the backend-supported kernel block sizes in th |
| [#43514](https://github.com/vllm-project/vllm/pull/43514) | mentioned | 0.6 | [Bugfix] Reject non-positive block_size in CacheConfig | latform.update_block_size_for_backend`. It addresses a different bug (#42510 — backend compatibility) and does not catch `block_size <= 0` because (a) backend `supports_block_size… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
