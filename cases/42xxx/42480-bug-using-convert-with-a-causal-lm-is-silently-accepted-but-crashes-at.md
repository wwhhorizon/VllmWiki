# vllm-project/vllm#42480: [Bug]: Using --convert with a causal LM is silently accepted but crashes at engine startup

| 字段 | 值 |
| --- | --- |
| Issue | [#42480](https://github.com/vllm-project/vllm/issues/42480) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using --convert with a causal LM is silently accepted but crashes at engine startup

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving a causal LM (e.g. `Meta-Llama-3.1-8B-Instruct`) with `--convert classify`, `--convert embed`, or `--convert reward`, vLLM's CLI and `validate_parsed_serve_args` both accept the configuration without complaint, but the server then crashes during engine initialization with an internal `AssertionError: pooler_config is not None` in `adapters.py`. The configuration is presented to users as a supported adaptation path (vLLM's own docs and config code reference `--convert` for pooling tasks), so this crash is unexpected and misleading. Notable: `--convert reward` is explicitly rewritten to `embed` internally with a deprecation warning, yet still crashes for the same reason — confirming this is a validation gap, not a model-specific edge case. ## Steps to Reproduce **Case 1: `--convert classify`** ```bash vllm serve \ --host 127.0.0.1 \ --port 19088 \ --convert classify ``` **Case 2: `--convert embed`** ```bash vllm serve \ --host 127.0.0.1 \ --port 19089 \ --convert embed ``` **Case 3: `--convert reward`** ```bash vllm serve \ --host 127.0.0.1 \ --port 19092 \ --convert reward ``` All three commands are accepted by the CLI...

## 现有链接修复摘要

#42672 [Bugfix] Align runner_type with explicit --convert to avoid pooler_config crash

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: crash is unexpected and misleading. Notable: `--convert reward` is explicitly rewritten to `embed` internally with a deprecation warning, yet still crashes for the same reason — confirming this is a validation gap, not...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ronment ### 🐛 Describe the bug When serving a causal LM (e.g. `Meta-Llama-3.1-8B-Instruct`) with `--convert classify`, `--convert embed`, or `--convert reward`, vLLM's CLI and `validate_parsed_serve_args` both accept th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ne of the following should happen: 1. vLLM successfully starts with the requested `--convert` mode, or 2. vLLM rejects the configuration early with a clear, user-facing error explaining that the specified `--convert` mo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42672](https://github.com/vllm-project/vllm/pull/42672) | closes_keyword | 0.95 | [Bugfix] Align runner_type with explicit --convert to avoid pooler_config crash | Fixes #42480. When `--convert embed\|classify` is passed on a causal LM (e.g. `Llama-3.1-8B-Instruct`) with `--runner` left on its `auto` default, `_get_runner_type` resolves to `" |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
