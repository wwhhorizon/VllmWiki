# vllm-project/vllm#21914: [Doc]: Syntax error of example code in structured_outputs.md

| 字段 | 值 |
| --- | --- |
| Issue | [#21914](https://github.com/vllm-project/vllm/issues/21914) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Syntax error of example code in structured_outputs.md

### Issue 正文摘录

### 📚 The doc issue There is a syntax error of example code showing how to use the guided_json parameter with a Pydantic mode in structured_outputs.md. Code ```Python from pydantic import BaseModel from enum import Enum class CarType(str, Enum): sedan = "sedan" suv = "SUV" truck = "Truck" coupe = "Coupe" class CarDescription(BaseModel): brand: str model: str car_type: CarType json_schema = CarDescription.model_json_schema() completion = client.chat.completions.create( model=model, messages=[ { "role": "user", "content": "Generate a JSON with the brand, model and car_type of the most iconic car from the 90's", } ], "response_format": { "type": "json_schema", "json_schema": { "name": "car-description", "schema": CarDescription.model_json_schema() }, }, ) print(completion.choices[0].message. Content) ``` Output: ``` File "/path/to/guided_json.py", line 32 "response_format": { ^ SyntaxError: positional argument follows keyword argument ``` ### Suggest a potential alternative/fix The correct syntax should be ```Python completion = client.chat.completions.create( model=model, messages=[ { "role": "user", "content": "Generate a JSON with the brand, model and car_type of the most iconic c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mode in structured_outputs.md. Code ```Python from pydantic import BaseModel from enum import Enum class CarType(str, Enum): sedan = "sedan" suv = "SUV" truck = "Truck" coupe = "Coupe" class CarDescription(BaseModel): b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a Pydantic mode in structured_outputs.md. Code ```Python from pydantic import BaseModel from enum import Enum class CarType(str, Enum): sedan = "sedan" suv = "SUV" truck = "Truck" coupe = "Coupe" class CarDescription(Ba...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
