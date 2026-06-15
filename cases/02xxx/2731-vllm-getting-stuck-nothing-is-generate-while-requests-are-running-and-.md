# vllm-project/vllm#2731: vLLM getting stuck. Nothing is generate while requests are running and pending.

| 字段 | 值 |
| --- | --- |
| Issue | [#2731](https://github.com/vllm-project/vllm/issues/2731) |
| 状态 | closed |
| 标签 |  |
| 评论 | 35; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vLLM getting stuck. Nothing is generate while requests are running and pending.

### Issue 正文摘录

We are seeing the latest version of vllm getting stuck randomly after some minutes of work. Sometimes after an hour. The server still receives new request and can reply to health and metrics, but no tokens are generate, no requests complete. Server keeps printing the status every 5 seconds, but no tokens are generated. As if the loop is stuck. ``` INFO 02-01 06:36:05 llm_engine.py:921] Avg prompt throughput: 382.6 tokens/s, Avg generation throughput: 118.5 tokens/s, Max iteration time: 386.7 ms, Avg time/tok:149.4 ms, Running: 35 reqs, Swapped: 0 reqs, Pending: 115 reqs, GPU KV cache usage: 99.0%, CPU KV cache usage: 0.0% INFO 02-01 06:36:05 async_llm_engine.py:110] Finished request cmpl-50c32d7a66084c3f9980d2bf06d79900-0. INFO 02-01 06:36:05 async_llm_engine.py:110] Finished request cmpl-90590e17ce6b4fa4b19f0812c0c98446-0. INFO: 10.244.5.235:41834 - "POST /v1/completions HTTP/1.1" 200 OK INFO: 10.244.5.237:53262 - "POST /v1/completions HTTP/1.1" 200 OK INFO 02-01 06:36:05 async_llm_engine.py:436] Received request cmpl-a523b4f84b1b491d9f61ddc4558f532b-0: prompt: None, prefix_pos: None,sampling_params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: enerate while requests are running and pending. We are seeing the latest version of vllm getting stuck randomly after some minutes of work. Sometimes after an hour. The server still receives new request and can reply to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: is generate while requests are running and pending. We are seeing the latest version of vllm getting stuck randomly after some minutes of work. Sometimes after an hour. The server still receives new request and can repl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: penalty=1.0, temperature=0.0, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=5...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: /tok:149.4 ms, Running: 35 reqs, Swapped: 0 reqs, Pending: 115 reqs, GPU KV cache usage: 99.0%, CPU KV cache usage: 0.0% INFO 02-01 06:36:05 async_llm_engine.py:110] Finished request cmpl-50c32d7a66084c3f9980d2bf06d7990...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: =1.0, temperature=0.0, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=512, log...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
