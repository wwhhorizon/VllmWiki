# vllm-project/vllm#8226: [Bug]: sm75 --num-scheduler-steps 8, unhandled errors in a TaskGroup

| 字段 | 值 |
| --- | --- |
| Issue | [#8226](https://github.com/vllm-project/vllm/issues/8226) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;sampling |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: sm75 --num-scheduler-steps 8, unhandled errors in a TaskGroup

### Issue 正文摘录

### Your current environment sm75 cuda 12.4 torch 2.4 vllm 0.6.0 ### 🐛 Describe the bug ### for sm75 gpu, unhandled errors in a TaskGroup, removing this instruction resolves the issue: --num-scheduler-steps 8 ### error: Sep 05 11:47:55 ubuntu22lts bash[20364]: INFO: Uvicorn running on http://0.0.0.0:1234 (Press CTRL+C to quit) Sep 05 11:48:03 ubuntu22lts bash[20364]: INFO 09-05 11:48:03 logger.py:36] Received request chat-38aeae4397294fd1af9711900e096429: prompt: ' user\nfda \n user\nwhat? \n assistant\n', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=6183, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [151644, 872, 198, 69, 3235, 151645, 198, 151644, 872, 198, 12555, 30, 151645, 198, 151644, 77091, 198], lora_request: None, prompt_adapter_request: None. Sep 05 11:48:03 ubuntu22lts bash[20364]:...

## 现有链接修复摘要

#35697 [CPU] Support int8 compute mode in CPU AWQ

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 05 11:48:04 async_llm_engine.py:63] assert isinstance(attn_metadata, FlashAttentionMetadata) Sep 05 11:48:04 ubuntu22lts bash[20397]: ERROR 09-05 11:48:04 async_llm_engine.py:63] AssertionError Sep 05 11:48:04 ubuntu22l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: sm75 --num-scheduler-steps 8, unhandled errors in a TaskGroup bug;stale ### Your current environment sm75 cuda 12.4 torch 2.4 vllm 0.6.0 ### 🐛 Describe the bug ### for sm75 gpu, unhandled errors in a TaskGroup, r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: sm75 --num-scheduler-steps 8, unhandled errors in a TaskGroup bug;stale ### Your current environment sm75 cuda 12.4 torch 2.4 vllm 0.6.0 ### 🐛 Describe the bug ### for sm75 gpu, unhandled errors in a TaskGroup, r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: _tokens=6183, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [151644, 872, 198, 69, 3235, 151645, 198, 15...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ut: 0.1 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.5%, CPU KV cache usage: 0.0%. Sep 05 11:48:04 ubuntu22lts bash[20397]: INFO 09-05 11:48:04 metrics.py:367] Prefix cache hit rate...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35697](https://github.com/vllm-project/vllm/pull/35697) | mentioned | 0.6 | [CPU] Support int8 compute mode in CPU AWQ | glang#8225](https://github.com/sgl-project/sglang/pull/8225) / [sglang#8226](https://github.com/sgl-project/sglang/pull/8226)) - At model-loading time, INT4 weights are repacked i… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
