# vllm-project/vllm#43009: [Bug]: Triton kernel JIT compilation during inference

| 字段 | 值 |
| --- | --- |
| Issue | [#43009](https://github.com/vllm-project/vllm/issues/43009) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton kernel JIT compilation during inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I started getting multiple warnings on the topic of `Triton kernel JIT compilation during inference` with the latest nightly builds - `version 0.21.1rc1.dev46+gb50646e5e` specifically and a few days prior. I did not receive these warnings a week or two ago. Is this a warning that was just not exposed before, or a new issue? Here is the startup log: ``` (APIServer) INFO 05-18 17:24:44 [utils.py:306] █ █ █▄ ▄█ (APIServer) INFO 05-18 17:24:44 [utils.py:306] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.21.1rc1.dev46+gb50646e5e (APIServer) INFO 05-18 17:24:44 [utils.py:306] █▄█▀ █ █ █ █ model Qwen/Qwen3.6-27B-FP8 (APIServer) INFO 05-18 17:24:44 [utils.py:306] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer) INFO 05-18 17:24:44 [utils.py:306] (APIServer) INFO 05-18 17:24:44 [utils.py:240] non-default args: {'model_tag': 'Qwen/Qwen3.6-27B-FP8', 'default_chat_template_kwargs': {'preserve_thinking': False}, 'enable_auto_tool_choice': True, 'tool_call_parser': 'qwen3_coder', 'host': '0.0.0.0', 'disable_access_log_for_endpoints': '/health,/metrics,/ping,/v1/models', 'model': 'Qwen/Qwen3.6-27B-FP8', 'max_model_len': 147456, 'served_model_name': ['Q36_27B_FP8'], 'override_gene...

## 现有链接修复摘要

#43879 [Bugfix] precompile Triton KV-zero and slot-mapping kernels (#43009)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: PIServer) INFO 05-18 17:24:44 [utils.py:306] █▄█▀ █ █ █ █ model Qwen/Qwen3.6-27B-FP8 (APIServer) INFO 05-18 17:24:44 [utils.py:306] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer) INFO 05-18 17:24:44 [utils.py:306] (APIServer) INFO 05-1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: 4m3', 'enable_prefix_caching': True, 'max_num_seqs': 32, 'enable_chunked_prefill': True, 'speculative_config': {'method': 'mtp', 'num_speculative_tokens': 1}} (APIServer) WARNING 05-18 17:24:44 [envs.py:1895] Unknown vL...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: the topic of `Triton kernel JIT compilation during inference` with the latest nightly builds - `version 0.21.1rc1.dev46+gb50646e5e` specifically and a few days prior. I did not receive these warnings a week or two ago....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: 4:44 [utils.py:306] █▄█▀ █ █ █ █ model Qwen/Qwen3.6-27B-FP8 (APIServer) INFO 05-18 17:24:44 [utils.py:306] ▀▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀ ▀ (APIServer) INFO 05-18 17:24:44 [utils.py:306] (APIServer) INFO 05-18 17:24:44 [utils.py:240]...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 6: wen3.6-27B-FP8', 'default_chat_template_kwargs': {'preserve_thinking': False}, 'enable_auto_tool_choice': True, 'tool_call_parser': 'qwen3_coder', 'host': '0.0.0.0', 'disable_access_log_for_endpoints': '/health,/metrics...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43879](https://github.com/vllm-project/vllm/pull/43879) | closes_keyword | 0.95 | [Bugfix] precompile Triton KV-zero and slot-mapping kernels (#43009) | Closes #43009 ## Test Plan todo ## Test Result todo --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [x] The pur |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
