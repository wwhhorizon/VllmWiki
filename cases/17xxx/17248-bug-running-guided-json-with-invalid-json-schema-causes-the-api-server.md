# vllm-project/vllm#17248: [Bug]: Running `guided_json` with invalid json schema causes the API server to crash

| 字段 | 值 |
| --- | --- |
| Issue | [#17248](https://github.com/vllm-project/vllm/issues/17248) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Running `guided_json` with invalid json schema causes the API server to crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve microsoft/Phi-4-mini-instruct --tensor-parallel-size 2` expected API server to return 422 or 400 error, but the server crashes instead ![Image](https://github.com/user-attachments/assets/683c57b8-7875-4d30-ac68-830009a5e2d5) ```python from pydantic import BaseModel from enum import Enum from openai import OpenAI client = OpenAI( base_url="http://localhost:8000/v1", api_key="-", ) class CarType(str, Enum): sedan = "sedan" suv = "SUV" truck = "Truck" coupe = "Coupe" class CarDescription(BaseModel): brand: str model: str car_type: CarType json_schema = CarDescription.model_json_schema() # adding an invalid key to the json schema json_schema['properties']['foo'] = 'bar' completion = client.chat.completions.create( model="microsoft/Phi-4-mini-instruct", messages=[ { "role": "user", "content": "Generate a JSON with the brand, model and car_type of the most iconic car from the 90's", } ], extra_body={"guided_json": json_schema}, ) content = completion.choices[0].message.content print(completion.choices[0].message.content) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ts/assets/683c57b8-7875-4d30-ac68-830009a5e2d5) ```python from pydantic import BaseModel from enum import Enum from openai import OpenAI client = OpenAI( base_url="http://localhost:8000/v1", api_key="-", ) class CarType...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 83c57b8-7875-4d30-ac68-830009a5e2d5) ```python from pydantic import BaseModel from enum import Enum from openai import OpenAI client = OpenAI( base_url="http://localhost:8000/v1", api_key="-", ) class CarType(str, Enum)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
