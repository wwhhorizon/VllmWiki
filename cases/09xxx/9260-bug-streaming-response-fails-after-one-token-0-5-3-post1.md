# vllm-project/vllm#9260: [Bug]: Streaming response fails after one token (0.5.3.post1)

| 字段 | 值 |
| --- | --- |
| Issue | [#9260](https://github.com/vllm-project/vllm/issues/9260) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Streaming response fails after one token (0.5.3.post1)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I add `stream=True` to a request, I get a single token returned and then exceptions logged by the vLLM server and my client making the request. I do not see any errors for non-streaming requests; I am using the Docker container 0.5.3.post1. Minimal test code: ```python from openai import OpenAI openai = OpenAI( base_url=" ", api_key=" ", ) completion = openai.chat.completions.create( model=" ", messages=[{"role": "user", "content": "who are you"}], max_tokens=1024, temperature=0, extra_body={ "add_special_tokens": True, "repetition_penalty": 1.05, "use_beam_search": True, "best_of": 5, }, stream=True ) response = "" for chunk in completion: if chunk.choices[0].delta.content: response += chunk.choices[0].delta.content print(response) ``` VLLM Log: ``` INFO 10-10 20:37:35 logger.py:36] Received request chat-8bde1dd570064156af091ff3828091cd: prompt: ' user\nwho are you \n assistant\n', params: SamplingParams(n=1, best_of=5, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.05, temperature=0.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=True, length_penalty=1.0,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: uest. I do not see any errors for non-streaming requests; I am using the Docker container 0.5.3.post1. Minimal test code: ```python from openai import OpenAI openai = OpenAI( base_url=" ", api_key=" ", ) completion = op...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Streaming response fails after one token (0.5.3.post1) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I add `stream=True` to a request, I get a single token...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: () as task_group: File "/usr/local/lib/python3.10/dist-packages/anyio/_backends/_asyncio.py", line 680, in __aexit__ raise BaseExceptionGroup( exceptiongroup.ExceptionGroup: unhandled errors in a TaskGroup (1 sub-except...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l_tokens": True, "repetition_penalty": 1.05, "use_beam_search": True, "best_of": 5, }, stream=True ) response = "" for chunk in completion: if chunk.choices[0].delta.content: response += chunk.choices[0].delta.content p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: treaming requests; I am using the Docker container 0.5.3.post1. Minimal test code: ```python from openai import OpenAI openai = OpenAI( base_url=" ", api_key=" ", ) completion = openai.chat.completions.create( model=" "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
