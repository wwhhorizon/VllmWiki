# vllm-project/vllm#22324: [Bug]: Error using openai's json_schema

| 字段 | 值 |
| --- | --- |
| Issue | [#22324](https://github.com/vllm-project/vllm/issues/22324) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error using openai's json_schema

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from pydantic import BaseModel from enum import Enum import openai class CarType(str, Enum): sedan = "sedan" suv = "SUV" truck = "Truck" coupe = "Coupe" class CarDescription(BaseModel): brand: str model: str car_type: CarType base_url = "http://localhost:9997/v1" client = openai.Client(base_url=base_url, api_key="EMPTY") model ="qwen3-0.6b" # model ="ernie4.5-0.3b" completion = client.chat.completions.create( # completion = client.chat.completions.parse( model=model, messages=[ { "role": "user", "content": "Generate a JSON with the brand, model and car_type of the most iconic car from the 90's\nReturn only valid JSON, no markdown fences or extra text.", } ], response_format={ "type": "json_schema", "json_schema": { "name": "car-description", "schema": CarDescription.model_json_schema(), "strict": False, }, }, # extra_body={ # "guided_json": CarDescription.model_json_schema(), # }, # response_format=CarDescription, ) print(completion.choices[0].message.content) ``` ``` response_format={ "type": "json_schema", "json_schema": { "name": "car-description", "schema": CarDescription.model_json_schema(), "strict": False, }, },...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: current environment ### 🐛 Describe the bug ```python from pydantic import BaseModel from enum import Enum import openai class CarType(str, Enum): sedan = "sedan" suv = "SUV" truck = "Truck" coupe = "Coupe" class CarDesc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vironment ### 🐛 Describe the bug ```python from pydantic import BaseModel from enum import Enum import openai class CarType(str, Enum): sedan = "sedan" suv = "SUV" truck = "Truck" coupe = "Coupe" class CarDescription(Ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Error using openai's json_schema bug;stale ### Your current environment ### 🐛 Describe the bug ```python from pydantic import BaseModel from enum import Enum import openai class CarType(str, Enum): sedan = "sedan...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
