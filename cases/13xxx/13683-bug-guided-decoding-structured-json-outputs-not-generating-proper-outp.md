# vllm-project/vllm#13683: [Bug]: Guided Decoding (structured json outputs) not generating proper outputs.

| 字段 | 值 |
| --- | --- |
| Issue | [#13683](https://github.com/vllm-project/vllm/issues/13683) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Guided Decoding (structured json outputs) not generating proper outputs.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from pydantic import BaseModel from enum import Enum from openai import OpenAI import json client = OpenAI( base_url="http://localhost:8080/v1", api_key="-", ) class CarType(str, Enum): sedan = "sedan" suv = "SUV" truck = "Truck" coupe = "Coupe" class CarDescription(BaseModel): brand: str model: str car_type: CarType json_schema = CarDescription.model_json_schema() completion = client.chat.completions.create( model="h2oai/h2o-danube2-1.8b-chat", messages=[ { "role": "user", "content": "Generate a JSON with the brand, model and car_type of the most iconic car from the 90's", } ], extra_body={"guided_json": json_schema, "guided_decoding_backend":"outlines", "guided_whitespace_pattern":" "}, ) print(completion.choices[0].message.content) ``` Issue The outputs generated aren't structured properly. Tested with bunch of other models - ```google/gemma-1.1-7b-it, meta-llama/Llama-3.1-8B-Instruct, meta-llama/Llama-3.1-8B, google/gemma-2-9b, h2oai/h2o-danube2-1.8b-chat (as above).``` And with different backends. xgrammar and lm-format-enforcer generate repeated {{ or a variation. For some models, Outlines generates {{'bran, as if...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: current environment ### 🐛 Describe the bug ```python from pydantic import BaseModel from enum import Enum from openai import OpenAI import json client = OpenAI( base_url="http://localhost:8080/v1", api_key="-", ) class...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: vironment ### 🐛 Describe the bug ```python from pydantic import BaseModel from enum import Enum from openai import OpenAI import json client = OpenAI( base_url="http://localhost:8080/v1", api_key="-", ) class CarType(st...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: } ], extra_body={"guided_json": json_schema, "guided_decoding_backend":"outlines", "guided_whitespace_pattern":" "}, ) print(completion.choices[0].message.content) ``` Issue The outputs generated aren't structured prope...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tured json outputs) not generating proper outputs. bug;structured-output;stale ### Your current environment ### 🐛 Describe the bug ```python from pydantic import BaseModel from enum import Enum from openai import OpenAI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
