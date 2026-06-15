# vllm-project/vllm#4966: [Bug]: vllm with gemma7b still slow

| 字段 | 值 |
| --- | --- |
| Issue | [#4966](https://github.com/vllm-project/vllm/issues/4966) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm with gemma7b still slow

### Issue 正文摘录

### Your current environment python3.11 vllm4.1 torch2.21-cu118 ### 🐛 Describe the bug here is my log with vllm, when inference gemma7b ,it shows 6 logs for one request which spend 30s , why so slow? ``` INFO 05-22 02:20:59 async_llm_engine.py:524] Received request 10390bd4d2dc4936bd1a62e5793a4fd8: prompt: ' user\n请讲一下python语言的特点 \n model\n', sampling_params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.8, top_p=0.8, top_k=1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[1], include_stop_str_in_output=False, ignore_eos=False, max_tokens=4096, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: None, lora_request: None. INFO 05-22 02:20:59 metrics.py:229] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0% INFO 05-22 02:21:04 metrics.py:229] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 12.0 tokens/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm with gemma7b still slow bug;stale ### Your current environment python3.11 vllm4.1 torch2.21-cu118 ### 🐛 Describe the bug here is my log with vllm, when inference gemma7b ,it shows 6 logs for one request whic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm with gemma7b still slow bug;stale ### Your current environment python3.11 vllm4.1 torch2.21-cu118 ### 🐛 Describe the bug here is my log with vllm, when inference gemma7b ,it shows 6 logs for one request whic...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _tokens=4096, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: None, lora_request: None. INFO 05-22 02:20:5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0, temperature=0.8, top_p=0.8, top_k=1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[1], include_stop_str_in_output=False, ignore_eos=False, max_tokens=...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.1 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0% INFO 05-22 02:21:04 metrics.py:229] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
