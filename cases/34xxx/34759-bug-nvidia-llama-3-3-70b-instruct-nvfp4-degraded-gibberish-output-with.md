# vllm-project/vllm#34759: [Bug]: nvidia/Llama-3.3-70B-Instruct-NVFP4 Degraded / Gibberish Output with TRITON_ATTN

| 字段 | 值 |
| --- | --- |
| Issue | [#34759](https://github.com/vllm-project/vllm/issues/34759) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: nvidia/Llama-3.3-70B-Instruct-NVFP4 Degraded / Gibberish Output with TRITON_ATTN

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On a B200 at vLLM 0.16.0rc3, nvidia/Llama-3.3-70B-Instruct-NVFP4 seems to have degraded output when using TRITON_ATTN backend: `curl --location 'localhost:8000/v1/chat/completions' --header 'Content-Type: application/json' --data '{"model": "nvidia/Llama-3.3-70B-Instruct-NVFP4", "max_tokens": 64, "temperature": 0.7, "seed": 42, "messages": [{"role": "user", "content": "Hey, how are you doing?"}]}'` ``` { "id":"chatcmpl-cf9d34913711cc5a60d4648892044dfd", "object":"chat.completion", "created":1771369061, "model":"nvidia/Llama-3.3-70B-Instruct-NVFP4", "choices":[ { "index":0, "message":{ "role":"assistant", "content":"201 ,\n\n\nHowever.com no to, a bachelor\nI to a century\",\n\nI a vital\nassistant\n\nThe or less\n\nIfYou K (Chinese may be to a baby\nassistant\n\nI only\n\nThe I to over L\\\\\\\\\nThe the world of in A , ,. THE\nassistant\n\n", "refusal":null, "annotations":null, "audio":null, "function_call":null, "tool_calls":[ ], "reasoning":null }, "logprobs":null, "finish_reason":"length", "stop_reason":null, "token_ids":null } ], "service_tier":null, "system_fingerprint":null, "usage":{ "prompt_tokens":42, "total_tokens":106...

## 现有链接修复摘要

#36908 Fix/triton quant query input | #36913 Fix/triton quant query input | #36914 Fix/triton quant query input

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: nvidia/Llama-3.3-70B-Instruct-NVFP4 Degraded / Gibberish Output with TRITON_ATTN bug ### Your current environment ### 🐛 Describe the bug On a B200 at vLLM 0.16.0rc3, nvidia/Llama-3.3-70B-Instruct-NVFP4 seems to h...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: g]: nvidia/Llama-3.3-70B-Instruct-NVFP4 Degraded / Gibberish Output with TRITON_ATTN bug ### Your current environment ### 🐛 Describe the bug On a B200 at vLLM 0.16.0rc3, nvidia/Llama-3.3-70B-Instruct-NVFP4 seems to have...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cache;cuda...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: N_ATTN bug ### Your current environment ### 🐛 Describe the bug On a B200 at vLLM 0.16.0rc3, nvidia/Llama-3.3-70B-Instruct-NVFP4 seems to have degraded output when using TRITON_ATTN backend: `curl --location 'localhost:8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: nvidia/Llama-3.3-70B-Instruct-NVFP4 Degraded / Gibberish Output with TRITON_ATTN bug ### Your current environment ### 🐛 Describe the bug On a B200 at vLLM 0.16.0rc3, nvidia/Llama-3.3-70B-Instruct-NVFP4 seems to h...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36908](https://github.com/vllm-project/vllm/pull/36908) | closes_keyword | 0.95 | Fix/triton quant query input | Fixes #34759 Two changes: 1. **Added `q_descale` support in the Triton unified attention kernel** : the Triton backend now properly supports pre-quantized Q input via a new `USE_Q |
| [#36913](https://github.com/vllm-project/vllm/pull/36913) | closes_keyword | 0.95 | Fix/triton quant query input | Fixes #34759 Two changes: 1. **Added `q_descale` support in the Triton unified attention kernel** : the Triton backend now properly supports pre-quantized Q input via a new `USE_Q |
| [#36914](https://github.com/vllm-project/vllm/pull/36914) | closes_keyword | 0.95 | Fix/triton quant query input | Fixes #34759 Two changes: 1. **Added `q_descale` support in the Triton unified attention kernel** : the Triton backend now properly supports pre-quantized Q input via a new `USE_Q |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
