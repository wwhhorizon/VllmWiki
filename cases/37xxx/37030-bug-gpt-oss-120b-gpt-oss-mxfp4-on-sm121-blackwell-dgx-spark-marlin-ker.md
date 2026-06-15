# vllm-project/vllm#37030: [Bug]: GPT-OSS-120B gpt-oss MXFP4 on SM121 (Blackwell DGX Spark): Marlin kernel generates wrong first Harmony token, producing null content/reasoning

| 字段 | 值 |
| --- | --- |
| Issue | [#37030](https://github.com/vllm-project/vllm/issues/37030) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;quantization |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS-120B gpt-oss MXFP4 on SM121 (Blackwell DGX Spark): Marlin kernel generates wrong first Harmony token, producing null content/reasoning

### Issue 正文摘录

### Environment - **vLLM Version**: 0.16.0rc2.dev559+g4bf19f9bf - **CUDA**: 13.0 - **GPU**: NVIDIA B200 / DGX Spark (SM121) - **Model**: openai/gpt-oss-120b **Server command:** ```bash vllm serve openai/gpt-oss-120b \ --quantization mxfp4 \ --dtype bfloat16 \ --kv-cache-dtype fp8 \ --max-model-len 2048 \ --gpu-memory-utilization 0.70 \ --max-num-seqs 2 \ --enable-chunked-prefill \ --enable-prefix-caching \ --load-format fastsafetensors ``` --- ### 🐛 Bug Description When serving `openai/gpt-oss-120b` with MXFP4 quantization on a **single SM121 GPU** (NVIDIA B200 / DGX Spark), all chat completions return `content: null` and `reasoning: null` despite `completion_tokens` showing that tokens were generated. **Request:** ```python client.chat.completions.create( model="gpt-oss-120b", messages=[{"role": "user", "content": "What is 2+2?"}], max_tokens=512, ) ``` **Response:** ```json { "choices": [{ "message": { "role": "assistant", "content": null, "reasoning": null, "tool_calls": [] }, "finish_reason": "length" }], "usage": { "prompt_tokens": 74, "completion_tokens": 512, "total_tokens": 586 } } ``` 512 tokens were generated but none surfaced as content or reasoning. --- ### Root Cause...

## 现有链接修复摘要

#31607 [Bugfix] Add SM 12.1 support + Fix GPT-OSS Harmony garbled reasoning and HarmonyError crashes

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: GPT-OSS-120B gpt-oss MXFP4 on SM121 (Blackwell DGX Spark): Marlin kernel generates wrong first Harmony token, producing null content/reasoning ### Environment - **vLLM Version**: 0.16.0rc2.dev559+g4bf19f9bf - **C...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: GPT-OSS-120B gpt-oss MXFP4 on SM121 (Blackwell DGX Spark): Marlin kernel generates wrong first Harmony token, producing null content/reasoning ### Environment - **vLLM Version**: 0.16.0rc2.dev559+g4bf19f9bf - **C...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: well DGX Spark): Marlin kernel generates wrong first Harmony token, producing null content/reasoning ### Environment - **vLLM Version**: 0.16.0rc2.dev559+g4bf19f9bf - **CUDA**: 13.0 - **GPU**: NVIDIA B200 / DGX Spark (S...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GPT-OSS-120B gpt-oss MXFP4 on SM121 (Blackwell DGX Spark): Marlin kernel generates wrong first Harmony token, producing null content/reasoning ### Environment - **vLLM Version**: 0.16.0rc2.dev559+g4bf19f9bf - **C...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: --gpu-memory-utilization 0.70 \ --max-num-seqs 2 \ --enable-chunked-prefill \ --enable-prefix-caching \ --load-format fastsafetensors ``` --- ### 🐛 Bug Description When serving `openai/gpt-oss-120b` with MXFP4 quantizat...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31607](https://github.com/vllm-project/vllm/pull/31607) | closes_keyword | 0.95 | [Bugfix] Add SM 12.1 support + Fix GPT-OSS Harmony garbled reasoning and HarmonyError crashes | fixes (new) Partially addresses #37030 Fixes two bugs causing `openai/gpt-oss-120b` to produce garbled, hallucinated, or null reasoning output. Not a duplicate of #34951, #30247, |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
