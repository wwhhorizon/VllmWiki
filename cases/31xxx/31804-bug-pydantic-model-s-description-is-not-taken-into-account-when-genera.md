# vllm-project/vllm#31804: [Bug]: Pydantic model's description is not taken into account when generating structured outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#31804](https://github.com/vllm-project/vllm/issues/31804) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Pydantic model's description is not taken into account when generating structured outputs

### Issue 正文摘录

### Your current environment vllm == 0.11.0 langchain==1.2.0 langchain-core== 1.2.6 langchain-openai == 1.1.6 ### 🐛 Describe the bug When using with_structured_output from langchain's ChatOpenAI, the model response does not seem to follow the rules mentioned in description field. Here is an example: ``` # Define a simple Pydantic schema class CarDescription(BaseModel): origin: str = Field(description="Country of origin in Uppercase") model: str = Field(description="Model of the car in lowercase") car_type: Literal["Sports", "Luxury", "Economic"] = Field(description="Type of the car") # Wrap with structured output structured_llm = llm.with_structured_output(CarDescription) # Generate Result result = structured_llm.invoke("Create a car description for VW") ``` The results looks like this: `origin='Germany' model='Golf GTI' car_type='Sports'` It can be seen that the LLM failed to generate the origin and model in the respective cases as mentioned in their descriptions. I served Qwen3-30B-A3B-Instruct using vllm to get the result. I tested this with GPT-5-mini and the results were in the correct cases. So I assume vLLM somehow does not read the description of each key but just the name...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Pydantic model's description is not taken into account when generating structured outputs bug;stale ### Your current environment vllm == 0.11.0 langchain==1.2.0 langchain-core== 1.2.6 langchain-openai == 1.1.6 ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ription is not taken into account when generating structured outputs bug;stale ### Your current environment vllm == 0.11.0 langchain==1.2.0 langchain-core== 1.2.6 langchain-openai == 1.1.6 ### 🐛 Describe the bug When us...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ptions. I served Qwen3-30B-A3B-Instruct using vllm to get the result. I tested this with GPT-5-mini and the results were in the correct cases. So I assume vLLM somehow does not read the description of each key but just...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
