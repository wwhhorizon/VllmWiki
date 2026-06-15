# vllm-project/vllm#11248: [Bug]: Using lm_format_enforcer, or using certain schemas, with Llama-3.2-90B-Vision-Instruct causes a crash

| 字段 | 值 |
| --- | --- |
| Issue | [#11248](https://github.com/vllm-project/vllm/issues/11248) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Using lm_format_enforcer, or using certain schemas, with Llama-3.2-90B-Vision-Instruct causes a crash

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This seems to be a near-replica of #8952. Running the server using Docker with latest image `698668586297dd30428a9f3bbcadb8a2034732ed13fdcd49218c8c3c9eb1cbd6`. Arguments: `--disable-log-requests -tp 8 --max-num-seqs 64 --enforce-eager` Reproducer: ```python import openai client = openai.OpenAI(base_url='http:// /v1', api_key='.') client.chat.completions.create(model='meta-llama/Llama-3.2-90B-Vision-Instruct', messages=[{'role': 'user', 'content': "Return a JSON object with key a value 1"}], response_format={'type': 'json_object'}) # Works, returns: ChatCompletion(id='chatcmpl-cc5772c27f4d40ea91cafd5eeb8d14f1', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='{ \n "a" \n \n \n \n\n\n\n\n\n \n\n\n\n\n\n: 1 \n}', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[]), stop_reason=None)], created=1734398547, model='meta-llama/Llama-3.2-90B-Vision-Instruct', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=20, prompt_tokens=45, total_tokens=65, completion_tokens_de...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: bug This seems to be a near-replica of #8952. Running the server using Docker with latest image `698668586297dd30428a9f3bbcadb8a2034732ed13fdcd49218c8c3c9eb1cbd6`. Arguments: `--disable-log-requests -tp 8 --max-num-seqs...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: g certain schemas, with Llama-3.2-90B-Vision-Instruct causes a crash bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This seems to be a near-replica of #8952. Running th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ccurred'], 'title': 'Event', 'type': 'object', 'additionalProperties': False}, 'LooseDate': {'properties': {'verbal_date': {'title': 'Verbal Date', 'type': 'string'}, 'is_precise': {'title': 'Is Precise', 'type': 'boole...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Using lm_format_enforcer, or using certain schemas, with Llama-3.2-90B-Vision-Instruct causes a crash bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug This seems t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ], response_format={'type': 'json_object'}, extra_body={"guided_decoding_backend": "lm-format-enforcer"}) # Crashes client.chat.completions.create(model='meta-llama/Llama-3.2-90B-Vision-Instruct', messages=[{'role': 'us...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | x94ac3 (0x7f5bb24b9ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #4: clone + 0x44 (0x7f5bb254aa04 in /usr/lib/x86_64-linux-gnu/libc.so.6) info: shutting down info: w |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7f5b6762c61d in /usr/local/lib/python3.12/dist-packa… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0x145c0 (0x7f5bb1c675c0 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorch… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
