# vllm-project/vllm#12201: [Bug]: `minItems` and `maxItems` json schema constraint fails on `xgrammar` and did not fallback to `outlines`

| 字段 | 值 |
| --- | --- |
| Issue | [#12201](https://github.com/vllm-project/vllm/issues/12201) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `minItems` and `maxItems` json schema constraint fails on `xgrammar` and did not fallback to `outlines`

### Issue 正文摘录

### Your current environment using `vllm/vllm-openai:v0.6.6.post1` docker image ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLM server fails to conform guided decoding with JSON schema `minItems` and `maxItems` for array types. ```python from openai import OpenAI from pydantic import BaseModel client = OpenAI( base_url="http://localhost:8000/v1", api_key="-", ) class Person(BaseModel): names: list[str]: Field(..., min_length=2, max_length=2) print(Person.model_json_schema()) # {'properties': {'names': {'items': {'type': 'string'}, 'maxItems': 2, 'minItems': 2, 'title': 'Names', 'type': 'array'}}, 'required': ['names'], 'title': 'Person', 'type': 'object'} response = client.chat.completions.create( model='aya-23-35b', messages=[ { 'role': 'user', 'content': 'Generate 4 names. Respond in json format.' } ], extra_body={"guided_json": Person.model_json_schema()} ) print(response.choices[0].message.content) ``` * 2 names should be generated due to JSON constraint, but 4 names is still generated ## Fallback to outlines The default grammar backend is now `xgrammar`, and it currently still does not support the following keywords for `array`: https://github.com/mlc-ai/xgram...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s` and `maxItems` json schema constraint fails on `xgrammar` and did not fallback to `outlines` bug ### Your current environment using `vllm/vllm-openai:v0.6.6.post1` docker image ### Model Input Dumps _No response_ ###...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: bug ### Your current environment using `vllm/vllm-openai:v0.6.6.post1` docker image ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLM server fails to conform guided decoding with JSON schema `minItems` and...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ent environment using `vllm/vllm-openai:v0.6.6.post1` docker image ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLM server fails to conform guided decoding with JSON schema `minItems` and `maxItems` for a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: schema.count("items") || schema.count("prefixItems") || schema.count("unevaluatedItems") ); WarnUnsupportedKeywords( schema, { "uniqueItems", "contains", "minContains", "maxContains", "minItems", "maxItems", }
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: L35 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
