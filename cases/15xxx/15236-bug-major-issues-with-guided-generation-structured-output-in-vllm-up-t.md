# vllm-project/vllm#15236: [Bug]: Major issues with guided generation / structured output in vLLM (up to and including v0.8.1);  many examples provided by vllm in /examples and structured_outputs.html doc do not work

| 字段 | 值 |
| --- | --- |
| Issue | [#15236](https://github.com/vllm-project/vllm/issues/15236) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Major issues with guided generation / structured output in vLLM (up to and including v0.8.1);  many examples provided by vllm in /examples and structured_outputs.html doc do not work

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm following the examples entirely from vllm's example code for structured output found here: https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_structured_outputs.py and getting errors in many examples. Additionally using `response_format` has had many errors which have varied from release v0.6.3-post1 through v0.8.1; I've tested all versions between the two previously mentioned with llama 3.3 and found inconsistencies. The unit tests occurring for guided generation do not seem robust; especially when the examples provided in the examples section don't work when running without modification. Specifically the issues start with the following code in [openai_chat_completion_structured_outputs.py](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/openai_chat_completion_structured_outputs.py); all subsequent examples in that .py file are also throwing errors: ``` # Guided decoding by JSON using Pydantic schema class CarType(str, Enum): sedan = "sedan" suv = "SUV" truck = "Truck" coupe = "Coupe" class CarDescription(BaseModel): brand: str model: str car_type: CarType jso...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ch have varied from release v0.6.3-post1 through v0.8.1; I've tested all versions between the two previously mentioned with llama 3.3 and found inconsistencies. The unit tests occurring for guided generation do not seem...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: uts.py and getting errors in many examples. Additionally using `response_format` has had many errors which have varied from release v0.6.3-post1 through v0.8.1; I've tested all versions between the two previously mentio...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ) } }, "additionalProperties": False, "required": ["variety"], }, "strict": True } } ``` Results in the following error on v0.8.1 when running the cell which contains ``` answer = call_model('gpt-4o', generate_prompt(df_
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: iving some sort of error; those are "Guided decoding by Grammar", "Extra backend options". I'm also running into many issues using `response format`. For example, when running this specific code from openai: https://git...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
