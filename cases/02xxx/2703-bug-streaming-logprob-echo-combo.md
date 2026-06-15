# vllm-project/vllm#2703: [BUG]: Streaming `logprob` & `echo` combo.

| 字段 | 值 |
| --- | --- |
| Issue | [#2703](https://github.com/vllm-project/vllm/issues/2703) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BUG]: Streaming `logprob` & `echo` combo.

### Issue 正文摘录

I'm trying to start writing a `logprob` & `echo` support for chat request. Unfortunately, running test like #1992 when `echo` is setted as `true` server doesn't respond. Seeing furtherer I checked that the **bug** begging in #2449 (sha: dd7e8f5f643167e3f13045cf75cbead54cb2ccfe). Previous commit #2463 (sha: d2a68364c473a3167a1c2b90f947bb611322a867) worked ok. ## LOG: ``` vllm-openai-main | INFO 02-01 04:31:38 async_llm_engine.py:385] Received request cmpl-dc7fb40d1b534a879768966f3dc50d39: prompt: None, prefix_pos: None,sampling params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=True, max_tokens=20, logprobs=0, prompt_logprobs=0, skip_special_tokens=True, spaces_between_special_tokens=True), prompt token ids: [2, 12375, 351, 5, 232, 651, 11, 2760, 116, 50118, 6557, 45117, 35, 50118]. vllm-openai-main | ERROR: Exception in ASGI application vllm-openai-main | Traceback (most recent call last): vllm-openai-main | File "/usr/local/lib/python3.10/d...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: openai-main | File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 746, in __call__ vllm-openai-main | await route.handle(scope, receive, send) vllm-openai-main | File "/usr/local/lib/python3.10/dis...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , ignore_eos=True, max_tokens=20, logprobs=0, prompt_logprobs=0, skip_special_tokens=True, spaces_between_special_tokens=True), prompt token ids: [2, 12375, 351, 5, 232, 651, 11, 2760, 116, 50118, 6557, 45117, 35, 50118...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=True, max_tokens=20...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: =1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=True, max_tokens=20, logpr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: openai-main | File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 746, in __call__ vllm-openai-main | await route.handle(scope, receive, send) vllm-openai-main | File "/usr/local/lib/python3.10/dis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
