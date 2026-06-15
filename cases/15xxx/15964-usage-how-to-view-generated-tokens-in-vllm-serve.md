# vllm-project/vllm#15964: [Usage]: how to view generated tokens in vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#15964](https://github.com/vllm-project/vllm/issues/15964) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to view generated tokens in vllm serve

### Issue 正文摘录

### Your current environment I'm running vllm. I wanted to see the total generated tokens in OpenAI-Compatible Server. Input: Using this watch -n 1 'curl -X POST "http://localhost:80/vllm-server/v1/completions" \ -H "Content-Type: application/json" \ -d "{\"model\": \"meta-llama/Llama-3.1-8B-Instruct\", \"prompt\": \"vhoirehvoe fieorwhfrioe fhoweifbroe?\", \"max_tokens\": 100}"' Output: vllm-server | INFO 04-02 12:30:21 engine.py:280] Added request cmpl-e9839b685fba45a98d309f875a8104b7-0. vllm-server | INFO: 172.20.0.2:53812 - "POST /v1/completions HTTP/1.1" 200 OK vllm-server | INFO 04-02 12:30:23 logger.py:39] Received request cmpl-a9e39f9d2a8f44ceab7f9acc4e793fbd-0: prompt: 'vhoirehvoe fieorwhfrioe fhoweifbroe?', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=100, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: [128000, 85, 6292, 556,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: v1/completions" \ -H "Content-Type: application/json" \ -d "{\"model\": \"meta-llama/Llama-3.1-8B-Instruct\", \"prompt\": \"vhoirehvoe fieorwhfrioe fhoweifbroe?\", \"max_tokens\": 100}"' Output: vllm-server | INFO 04-02...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: t: 57.2 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. vllm-server | INFO 04-02 12:30:23 metrics.py:471] Prefix cache hit rate: GPU: 99.53%, CPU: 0.00% v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: how to view generated tokens in vllm serve usage;stale ### Your current environment I'm running vllm. I wanted to see the total generated tokens in OpenAI-Compatible Server. Input: Using this watch -n 1 'curl -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 793fbd-0. vllm-server | INFO 04-02 12:30:23 metrics.py:455] Avg prompt throughput: 11.4 tokens/s, Avg generation throughput: 57.2 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CP...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: usage: 0.0%. vllm-server | INFO 04-02 12:30:23 metrics.py:471] Prefix cache hit rate: GPU: 99.53%, CPU: 0.00% vllm-server | INFO: 172.20.0.2:53812 - "POST /v1/completions HTTP/1.1" 200 OK vllm-server | INFO 04-02 12:30:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
