# vllm-project/vllm#13134: [Bug]: vllm 0.6.4.post1 request hanging.

| 字段 | 值 |
| --- | --- |
| Issue | [#13134](https://github.com/vllm-project/vllm/issues/13134) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.6.4.post1 request hanging.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug request: ```text curl http://127.0.0.1:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "default_model", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "AI能不能像人一样创造新东西"} ], "temperature": 0.6, "stream": true }' ``` output: (If using `stream=false`, there is no logs besides health check) ```text INFO 02-12 15:20:24 logger.py:37] Received request chatcmpl-5d9f00ee00c341c9a1919cb00a2d0963: prompt: ' system\nYou are a helpful assistant. \n user\nAI能不能像人一样创造新东西 \n assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.6, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=16357, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None. INFO: fdbd:dc03:c:643:2600::81:33816 - "POST /v1/chat/completions HTTP/1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tokens=16357, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: No...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 8c) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm 0.6.4.post1 request hanging. bug ### Your current environment ### 🐛 Describe the bug request: ```text curl http://127.0.0.1:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "de...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: re": 0.6, "stream": true }' ``` output: (If using `stream=false`, there is no logs besides health check) ```text INFO 02-12 15:20:24 logger.py:37] Received request chatcmpl-5d9f00ee00c341c9a1919cb00a2d0963: prompt: ' sy...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
