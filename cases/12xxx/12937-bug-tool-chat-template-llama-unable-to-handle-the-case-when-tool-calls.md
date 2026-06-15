# vllm-project/vllm#12937: [Bug]: tool_chat_template_llama unable to handle the case when tool_calls is empty list.

| 字段 | 值 |
| --- | --- |
| Issue | [#12937](https://github.com/vllm-project/vllm/issues/12937) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tool_chat_template_llama unable to handle the case when tool_calls is empty list.

### Issue 正文摘录

### 🐛 Describe the bug When an agent uses the deepseek-ai/DeepSeek-R1-Distill-Llama-70B model to call tools, the messages may contain a tool_calls field that is an empty list. In this case, vLLM should not throw an error but should instead continue processing the request and return a response to the frontend user. the bad message like: ``` {'content': 'Okay, so the user is asking about the weather in San Francisco and Los Angeles. I need to figure out how to respond using the given function. The function is called get_weather, and it requires two parameters: location and unit. The location should be a string like "San Francisco, CA" and the unit can be either "celsius" or "fahrenheit". But wait, the user is asking about two cities, not just one. The function only allows for one location at a time. So maybe I should call the function twice, once for each city. But the user's instruction says to respond with a single JSON for a function call. Hmm, that might be a problem. Alternatively, perhaps the function can accept multiple locations in some way, but looking at the parameters, it seems to only take one location string. So I might need to prioritize one city over the other. Which...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: tool_chat_template_llama unable to handle the case when tool_calls is empty list. bug;stale ### 🐛 Describe the bug When an agent uses the deepseek-ai/DeepSeek-R1-Distill-Llama-70B model to call tools, the message...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: plate_llama unable to handle the case when tool_calls is empty list. bug;stale ### 🐛 Describe the bug When an agent uses the deepseek-ai/DeepSeek-R1-Distill-Llama-70B model to call tools, the messages may contain a tool...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: `` {'content': 'Okay, so the user is asking about the weather in San Francisco and Los Angeles. I need to figure out how to respond using the given function. The function is called get_weather, and it requires two param...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
