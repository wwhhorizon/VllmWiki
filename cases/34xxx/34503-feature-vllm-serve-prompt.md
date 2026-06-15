# vllm-project/vllm#34503: [Feature]: vllm serve日志不显示请求Prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#34503](https://github.com/vllm-project/vllm/issues/34503) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vllm serve日志不显示请求Prompt

### Issue 正文摘录

### 🚀 The feature, motivation and pitch 升级vllm版本后，发现vllm serve日志中只显示： ```bash [0;36m(APIServer pid=90458)[0;0m INFO: Started server process [90458] [0;36m(APIServer pid=90458)[0;0m INFO: Waiting for application startup. [0;36m(APIServer pid=90458)[0;0m INFO: Application startup complete. [0;36m(APIServer pid=90458)[0;0m INFO 02-13 11:33:33 [logger.py:49] Received request chatcmpl-a269fdcb7c6ce890: params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=0.95, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=100, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, structured_outputs=None, extra_args=None), lora_request: None. [0;36m(APIServer pid=90458)[0;0m INFO 02-13 11:33:33 [async_llm.py:382] Added request chatcmpl-a269fdcb7c6ce890-a8a65d16. [0;36m(APIServer pid=90458)[0;0m INFO: 10.80.23.18:51408 - "POST /v1/chat/completions HTTP/1.1" 200 OK [0;36m(APIServer pid=90458)[0;0m INFO 02-13 11:33:39 [loggers.py:257] Engine 000: Avg p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: x_tokens=100, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, structured_outputs=None, extra_args=None), lora_request: None....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 4.6 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% [0;36m(APIServer pid=90458)[0;0m INFO 02-13 11:33:49 [loggers.py:257] Engine 000: Avg prompt t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: , stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=100, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: vllm serve日志不显示请求Prompt feature request ### 🚀 The feature, motivation and pitch 升级vllm版本后，发现vllm serve日志中只显示： ```bash [0;36m(APIServer pid=90458)[0;0m INFO: Started server process [90458] [0;36m(APIServer...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 90458)[0;0m INFO 02-13 11:33:39 [loggers.py:257] Engine 000: Avg prompt throughput: 0.8 tokens/s, Avg generation throughput: 4.6 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit ra...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
