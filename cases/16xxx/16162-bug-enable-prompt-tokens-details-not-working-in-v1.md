# vllm-project/vllm#16162: [Bug]: --enable-prompt-tokens-details not working in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#16162](https://github.com/vllm-project/vllm/issues/16162) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --enable-prompt-tokens-details not working in V1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug V1 does not report prompt token details if enabled. Seems implementation is missing. ``` python -m vllm.entrypoints.openai.api_server --model "facebook/opt-125m" \ --enable-prompt-tokens-details \ --enable-prefix-caching \ --served-model-name latest \ --chat-template="{% for message in messages %} {% if message[\"role\"] == \"user\" %} {{ \"Question:\n\" + message[\"content\"] + \"\n\" }} {% elif message[\"role\"] == \"system\" %} {{ \"System:\n\" > ``` ```python from openai import OpenAI client = OpenAI(api_key="dummy", base_url="http://localhost:8000/v1") # prompt with more than 16 tokens messages = [{"role": "user", "content": "Hello! What's your name? What do you do?"}] # first request to cache the prompt response = client.chat.completions.create(model="latest",messages=messages,max_tokens=256) # second request to fetch from prefix cache response = client.chat.completions.create(model="latest",messages=messages,max_tokens=256) print(response.usage) ``` V0 output ``` CompletionUsage(completion_tokens=73, prompt_tokens=24, total_tokens=97, completion_tokens_details=None, prompt_tokens_details=PromptTokensDetails(audio_tokens=No...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: \"role\"] == \"system\" %} {{ \"System:\n\" > ``` ```python from openai import OpenAI client = OpenAI(api_key="dummy", base_url="http://localhost:8000/v1") # prompt with more than 16 tokens messages = [{"role": "user",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: "user", "content": "Hello! What's your name? What do you do?"}] # first request to cache the prompt response = client.chat.completions.create(model="latest",messages=messages,max_tokens=256) # second request to fetch fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: latest",messages=messages,max_tokens=256) # second request to fetch from prefix cache response = client.chat.completions.create(model="latest",messages=messages,max_tokens=256) print(response.usage) ``` V0 output ``` Co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
