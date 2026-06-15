# vllm-project/vllm#1930: CUDA 12.1 vllm==0.2.3 Double Free

| 字段 | 值 |
| --- | --- |
| Issue | [#1930](https://github.com/vllm-project/vllm/issues/1930) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA 12.1 vllm==0.2.3 Double Free

### Issue 正文摘录

I tried this with FastChat that uses vLLM backend: Both inputs: ``` 1. openai.ChatCompletion.create( model=model, messages=( [ {"role": "user", "content": prompt} ] ), stream=False, # temperature=args.temperature, presence_penalty=0.0, frequency_penalty=0.0, max_tokens=max_tokens, best_of=best_of, n=n, temperature=temperature, top_p=top_p, top_k=top_k, use_beam_search=True) ``` ``` 2. openai.ChatCompletion.create( model=model, messages=( [ {"role": "user", "content": prompt} ] ), stream=True, # temperature=args.temperature, presence_penalty=0.0, frequency_penalty=0.0, max_tokens=max_tokens, best_of=best_of, n=n, temperature=temperature, top_p=top_p, top_k=top_k, use_beam_search=True) ``` raises the following error ``` 2023-12-05 08:52:19 | ERROR | stderr | File "/home/tan/tjtanaa/vllmcu12/vllm/engine/async_llm_engine.py", line 28, in _raise_exception_on_finish 2023-12-05 08:52:19 | ERROR | stderr | task.result() 2023-12-05 08:52:19 | ERROR | stderr | File "/home/tan/tjtanaa/vllmcu12/vllm/engine/async_llm_engine.py", line 359, in run_engine_loop 2023-12-05 08:52:19 | ERROR | stderr | has_requests_in_progress = await self.engine_step() 2023-12-05 08:52:19 | ERROR | stderr | File "/h...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: "role": "user", "content": prompt} ] ), stream=False, # temperature=args.temperature, presence_penalty=0.0, frequency_penalty=0.0, max_tokens=max_tokens, best_of=best_of, n=n, temperature=temperature, top_
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: CUDA 12.1 vllm==0.2.3 Double Free I tried this with FastChat that uses vLLM backend: Both inputs: ``` 1. openai.ChatCompletion.create( model=model, messages=( [ {"role": "user", "conte
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n_engine_loop 2023-12-05 08:52:19 | ERROR | stderr | has_requests_in_progress = await self.engine_step() 2023-12-05 08:52:19 | ERROR | stderr | File "/home/tan/tjtanaa/vllmcu12/vllm/engine/async_llm_engine.py", line 338,
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: A 12.1 vllm==0.2.3 Double Free I tried this with FastChat that uses vLLM backend: Both inputs: ``` 1. openai.ChatCompletion.create( model=model, messages=( [ {"role": "user", "content": prompt} ] ), stream=False, # temp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vLLM backend: Both inputs: ``` 1. openai.ChatCompletion.create( model=model, messages=( [ {"role": "user", "content": prompt} ] ), stream=False, # temperature=args.temperature, presence_penalty=0.0, frequency

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
