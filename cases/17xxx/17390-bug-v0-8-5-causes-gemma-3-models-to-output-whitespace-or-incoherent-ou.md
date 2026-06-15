# vllm-project/vllm#17390: [Bug]: v0.8.5 causes gemma-3 models to output whitespace or incoherent output

| 字段 | 值 |
| --- | --- |
| Issue | [#17390](https://github.com/vllm-project/vllm/issues/17390) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.8.5 causes gemma-3 models to output whitespace or incoherent output

### Issue 正文摘录

### Your current environment ``` HF_TOKEN=... vllm serve google/gemma-3-4b-it ``` ### 🐛 Describe the bug upgrading from v0.8.4 to v0.8.5 causes gemma-3 models to experience regression in text generation, generating whitespace or incoherent text. ``` from pydantic import BaseModel from enum import Enum from openai import OpenAI client = OpenAI( base_url="http://localhost:8000/v1", api_key="-", ) completion = client.chat.completions.create( model="google/gemma-3-4b-it", messages=[ { "role": "user", "content": "tell me a joke", } ], max_tokens=100, ) content = completion.choices[0].message.content print(content) # output whitespace only ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: generation, generating whitespace or incoherent text. ``` from pydantic import BaseModel from enum import Enum from openai import OpenAI client = OpenAI( base_url="http://localhost:8000/v1", api_key="-", ) completion =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: v0.8.5 causes gemma-3 models to output whitespace or incoherent output bug ### Your current environment ``` HF_TOKEN=... vllm serve google/gemma-3-4b-it ``` ### 🐛 Describe the bug upgrading from v0.8.4 to v0.8.5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: bug upgrading from v0.8.4 to v0.8.5 causes gemma-3 models to experience regression in text generation, generating whitespace or incoherent text. ``` from pydantic import BaseModel from enum import Enum from openai impor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
