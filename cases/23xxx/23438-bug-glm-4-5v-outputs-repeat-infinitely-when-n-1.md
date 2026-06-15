# vllm-project/vllm#23438: [Bug]: GLM-4.5V outputs repeat infinitely when `n > 1`

| 字段 | 值 |
| --- | --- |
| Issue | [#23438](https://github.com/vllm-project/vllm/issues/23438) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5V outputs repeat infinitely when `n > 1`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I found that GLM-4.5V outputs repeat infinitely whenever `n > 1`. Notably, this occurs even when I only pass in text input and thinking is disabled. Serve command: ``` vllm serve zai-org/GLM-4.5V -tp 4 ``` Example: ``` from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) model = client.models.list().data[0].id print("Model:", model) normal_response = client.chat.completions.create( model=model, messages=[ { "role": "user", "content": [ {"type": "text", "text": "Who are you?"}, ], } ], n=1, extra_body={"chat_template_kwargs": {"enable_thinking": False}}, ) print("[Normal response]") print(normal_response.choices[0].message.content) buggy_response = client.chat.completions.create( model=model, messages=[ { "role": "user", "content": [ {"type": "text", "text": "Who are you?"}, ], } ], n=2, # n > 1 max_tokens=8192, # Otherwise this example would run for 20 mins until the context length is reached extra_body={"chat_template_kwargs": {"enable_thinking": False}}, ) print("[Buggy response]") print(buggy_response.choices[0].mess...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nd: ``` vllm serve zai-org/GLM-4.5V -tp 4 ``` Example: ``` from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_bas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: t = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) model = client.models.list().data[0].id print("Model:", model) normal_response = client.chat.completions.create( model=model, messages=[ { "role": "user",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: zR ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , n=1, extra_body={"chat_template_kwargs": {"enable_thinking": False}}, ) print("[Normal response]") print(normal_response.choices[0].message.content) buggy_response = client.chat.completions.create( model=model, messag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
