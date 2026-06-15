# vllm-project/vllm#2067: Runtime AsyncEngineDeadError: "This should never happen! Please open an issue on Github."

| 字段 | 值 |
| --- | --- |
| Issue | [#2067](https://github.com/vllm-project/vllm/issues/2067) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;sampling |
| 症状 | crash;slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Runtime AsyncEngineDeadError: "This should never happen! Please open an issue on Github."

### Issue 正文摘录

Report this per the request in the error message. I got this error on A100 without distributed inference. I can consistently repro with this query, and other queries work fine. ``` INFO 12-12 20:00:59 async_llm_engine.py:379] Received request cmpl-e044ab19e61a4b0ba256c262c7975267: prompt: 'How to make Sushi?', sampling params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], ignore_eos=False, max_tokens=1024, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True), prompt token ids: [1, 1602, 298, 1038, 318, 1426, 28710, 28804]. INFO 12-12 20:00:59 llm_engine.py:649] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 12-12 20:01:00 async_llm_engine.py:134] Aborted request cmpl-e044ab19e61a4b0ba256c262c7975267. Exception in callback functools.partial( , request_tracker= ) handle: , request_tracker= )> Traceback (most r...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: hould never happen! Please open an issue on Github." Report this per the request in the error message. I got this error on A100 without distributed inference. I can consistently repro with this query, and other queries...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: on_utils_fast.py", line 612, in convert_tokens_to_string return self.backend_tokenizer.decoder.decode(tokens) TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString' The above exception was the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: " Report this per the request in the error message. I got this error on A100 without distributed inference. I can consistently repro with this query, and other queries work fine. ``` INFO 12-12 20:00:59 async_llm_engine...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eos=False, max_tokens=1024, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True), prompt token ids: [1, 1602, 298, 1038, 318, 1426, 28710, 28804]. INFO 12-12 20:00:59 llm_en...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 12-12 20:01:00 async_llm_engine.py:134] Aborted request cmpl-e044ab19e61a4b0ba256c262c7975267....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
