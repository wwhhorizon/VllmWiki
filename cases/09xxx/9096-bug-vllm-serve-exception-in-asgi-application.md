# vllm-project/vllm#9096: [Bug]: vllm serve Exception in ASGI application

| 字段 | 值 |
| --- | --- |
| Issue | [#9096](https://github.com/vllm-project/vllm/issues/9096) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve Exception in ASGI application

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Greetings, I am trying to serve a finetuned Llama 3.1 8B model with tool_chat_template_llama3.1_json.jinja template provided by vllm. However I run into this error. I've tried to remove the template, it still gives me the same error. I am just using curl command to test if the model works. Detailed error message is below, could you help me figure out what's wrong? Thanks ``` INFO 10-05 21:26:23 logger.py:36] Received request chat-7656eedcced64cadbb0eb588c2369195: prompt: ' system \n\nCutting Knowledge Date: December 2023\nToday Date: 05 Oct 2024\n\nYou are a helpful assistant. user \n\nWho won the world series in 2020? assistant \n\n', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=46445, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=...

## 现有链接修复摘要

#9850 [Bugfix] Fix chunked prefill with model dtype float32 on Turing Devices | #9931 [Bugfix] Fix pickle of input when async output processing is on

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tokens=46445, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [128000, 128006, 9125, 128007, 271, 38766, 1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: "/home/xz479/miniconda3/envs/vllm/lib/python3.9/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/home/xz479/miniconda3/envs/vllm/lib/python3.9/site-pack...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: , temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: out what's wrong? Thanks ``` INFO 10-05 21:26:23 logger.py:36] Received request chat-7656eedcced64cadbb0eb588c2369195: prompt: ' system \n\nCutting Knowledge Date: December 2023\nToday Date: 05 Oct 2024\n\nYou are a hel...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ash;nan_inf env_dependency #9850 [Bugfix] Fix chunked prefill with model dtype float32 on Turing Devices | #9931 [Bugfix] Fix pickle of input when async output processing is on Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9850](https://github.com/vllm-project/vllm/pull/9850) | closes_keyword | 0.95 | [Bugfix] Fix chunked prefill with model dtype float32 on Turing Devices | FIX #9096 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- insi |
| [#9931](https://github.com/vllm-project/vllm/pull/9931) | closes_keyword | 0.95 | [Bugfix] Fix pickle of input when async output processing is on | Fix pickle of input when async output processing is on From the log of these issues: #9096 and #9306 ```log WARNING 10-05 21:26:25 model_runner_base.py:143] Failed to pickle in |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
