# vllm-project/vllm#8912: [Bug]: Tool calling on Llama 3.1/3.2 fails with KeyError: '<tool_call>'

| 字段 | 值 |
| --- | --- |
| Issue | [#8912](https://github.com/vllm-project/vllm/issues/8912) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tool calling on Llama 3.1/3.2 fails with KeyError: '<tool_call>'

### Issue 正文摘录

### Your current environment ### Model Input Dumps ``` Received request chat-d7b6885bb0a14fa3b3da22dbbd580234: prompt: ' system \n\nEnvironment: ipython\nCutting Knowledge Date: December 2023\nToday Date: 27 Sep 2024\n\n user \n\nGiven the following functions, please respond with a JSON for a function call with its proper arguments that best answers the given prompt.\n\nRespond in the format {"name": function name, "parameters": dictionary of argument name and its value}.Do not use variables.\n\n{\n "type": "function",\n "function": {\n "name": "tavily_search_results_json",\n "description": "A search engine optimized for comprehensive, accurate, and trusted results. Useful for when you need to answer questions about current events. Input should be a search query.",\n "parameters": {\n "properties": {\n "query": {\n "description": "search query to look up",\n "type": "string"\n }\n },\n "required": [\n "query"\n ],\n "type": "object"\n }\n }\n}\n\nTell me about langgraph assistant \n\n', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: okens=130854, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [128000, 128006, 9125, 128007, 271, 13013, 2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: bug ### Your current environment ### Model Input Dumps ``` Received request chat-d7b6885bb0a14fa3b3da22dbbd580234: prompt: ' system \n\nEnvironment: ipython\nCutting Knowledge Date: December 2023\nToday Date: 27 Sep 202...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: onment ### Model Input Dumps ``` Received request chat-d7b6885bb0a14fa3b3da22dbbd580234: prompt: ' system \n\nEnvironment: ipython\nCutting Knowledge Date: December 2023\nToday Date: 27 Sep 2024\n\n user \n\nGiven the f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: _ALLOC_CONF=expandable_segments:True vllm serve ../Llama-3.2-3B-Instruct-quantized.w8a8 --served-model-name Llama-3.2 --enable-auto-tool-choice --tool-call-parser hermes --gpu-memory-utilization 0.8 INFO 09-27 14:05:08...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Tool calling on Llama 3.1/3.2 fails with KeyError: '<tool_call>' bug ### Your current environment ### Model Input Dumps ``` Received request chat-d7b6885bb0a14fa3b3da22dbbd580234: prompt: ' system \n\nEnvironment...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
