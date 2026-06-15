# vllm-project/vllm#10102: [Bug]: Engine loop has died for Meta-Llama-3.1-8B-Instruct TP=2

| 字段 | 值 |
| --- | --- |
| Issue | [#10102](https://github.com/vllm-project/vllm/issues/10102) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine loop has died for Meta-Llama-3.1-8B-Instruct TP=2

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The error message: ``` INFO 11-07 19:58:29 metrics.py:345] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. DEBUG 11-07 19:58:29 engine.py:215] Waiting for new requests in engine loop. INFO 11-07 19:58:30 logger.py:37] Received request chat-d4bc2e3f9df643d5ae0a7712c781874c: prompt: ' system \n\nCutting Knowledge Date: December 2023\nToday Date: 07 Nov 2024\n\nYou are a helpful assistant. user \n\nTell me something about large language models. assistant \n\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.05, temperature=0.7, top_p=0.8, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=8143, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), guided_decoding=GuidedDecodingParams(json=None, regex=None, choice=None, grammar=None, json_object=None, backend=None...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _tokens=8143, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), guided_decoding=GuidedDecodingParams(json=None, regex=None, ch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Engine loop has died for Meta-Llama-3.1-8B-Instruct TP=2 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The error message: ``` INFO 11-07 19:58:29 metrics.py:345] Avg...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: age: 0.0%, CPU KV cache usage: 0.0%. DEBUG 11-07 19:58:29 engine.py:215] Waiting for new requests in engine loop. INFO 11-07 19:58:30 logger.py:37] Received request chat-d4bc2e3f9df643d5ae0a7712c781874c: prompt: ' syste...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rams(json=None, regex=None, choice=None, grammar=None, json_object=None, backend=None, whitespace_pattern=None), prompt_token_ids: [128000, 128006, 9125, 128007, 271, 38766, 1303, 33025, 2696, 25, 6790, 220, 2366, 18, 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: NFO: Finished server process [116760] ``` My serving script is ``` CUDA_VISIBLE_DEVICES=0,1 python -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 11600 \ --gpu_memory_utilization 0.50 \ --tensor_parallel_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
