# vllm-project/vllm#9692: [Usage]: How do I use langchain for tool calls？

| 字段 | 值 |
| --- | --- |
| Issue | [#9692](https://github.com/vllm-project/vllm/issues/9692) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How do I use langchain for tool calls？

### Issue 正文摘录

### Your current environment ``` vllm = 0.6.3.post1 ``` ### How would you like to use vllm #### langchain test code ``` llm = ChatOpenAI( api_key="api_key", temperature=0.1, top_p=0.7, max_tokens=8192, model="glm4-9b-chat", base_url="http://host:port/v1/" ) tools = {"weather": weather} context = [] def process_query(query): global context context.append({"role": "user", "content": query}) response = llm_with_tools.invoke(context) print(response) if response.tool_calls: tool_call = response.tool_calls[0] tool_name = tool_call["name"] tool = tools[tool_name] tool_arguments = tool_call["args"] tool_result = tool(**tool_arguments) context.append({"role": "system", "content": f"你可以通过工具得到实时的天气信息，工具得到的结果是：\n\n{tool_result}\n\n，这个结果绝对准确，你可以直接使用该结果进行表述。"}) response = llm.invoke(context) context.append({"role": "assistant", "content": response.content}) return response.content query_1 = "今天深圳的天气怎么样?" response_1 = process_query(query_1) print("LLM_response:", response_1) ``` #### Run command: `vllm serve glm-4-9b-chat_path --served-model-name glm4-9b-chat --host xxx --port xxx --max_model_len=128000 --tensor_parallel_size 2 --gpu_memory_utilization 0.4 --trust_remote_code` How do I use langc...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ls？ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: api_key", temperature=0.1, top_p=0.7, max_tokens=8192, model="glm4-9b-chat", base_url="http://host:port/v1/" ) tools = {"weather": weather} context = [] def process_query(query): global context context.append({"role": "...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How do I use langchain for tool calls？ usage;stale ### Your current environment ``` vllm = 0.6.3.post1 ``` ### How would you like to use vllm #### langchain test code ``` llm = ChatOpenAI( api_key="api_key", te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: lm = 0.6.3.post1 ``` ### How would you like to use vllm #### langchain test code ``` llm = ChatOpenAI( api_key="api_key", temperature=0.1, top_p=0.7, max_tokens=8192, model="glm4-9b-chat", base_url="http://host:port/v1/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
