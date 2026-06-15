# vllm-project/vllm#9454: [Bug]: langchain qwen2.5 function calling error

| 字段 | 值 |
| --- | --- |
| Issue | [#9454](https://github.com/vllm-project/vllm/issues/9454) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: langchain qwen2.5 function calling error

### Issue 正文摘录

### Your current environment ### Model Input Dumps Test code: ``` test_llm = ChatOpenAI( openai_api_key="xxx", openai_api_base="http://xxxxx:6000/v1", model_name="Qwen2.5-7B-Instruct", temperature=0.01, max_tokens=1024, streaming=True, max_retries=0, request_timeout=60, callbacks=[], frequency_penalty=1.05, model_kwargs={"stop": [" ", " "], "extra_body": {"skip_special_tokens": False}}, ) agent = create_react_agent( model=test_llm, tools=[get_current_time, get_current_hour, get_current_date, get_current_week, get_current_month, get_current_year], debug=True, ) async for chunk in agent.astream( input={"messages": [HumanMessage(content="现在是几月份")]}, config=RunnableConfig( configurable={"thread_id": 1}, recursion_limit=15, ), ): print(chunk) ``` Output: {'agent': {'messages': [AIMessage(content='', additional_kwargs={'tool_calls': [{'index': 0, 'id': 'chatcmpl-tool-62111907b5634a5ca584761b1528a2be', 'function': {'arguments': None, 'name': 'get_current_month'}, 'type': 'function'}]}, response_metadata={'finish_reason': 'tool_calls', 'model_name': 'Qwen2.5-7B-Instruct'}, id='run-e81f28b5-51f6-4114-8fa6-90b4e9fee7c6-0', invalid_tool_calls=[{'name': 'get_current_month', 'args': None, 'id'...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: langchain qwen2.5 function calling error bug ### Your current environment ### Model Input Dumps Test code: ``` test_llm = ChatOpenAI( openai_api_key="xxx", openai_api_base="http://xxxxx:6000/v1", model_name="Qwen
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: odel_kwargs={"stop": [" ", " "], "extra_body": {"skip_special_tokens": False}}, ) agent = create_react_agent( model=test_llm, tools=[get_current_time, get_current_hour, get_current_date, get_current_week, get_current_mo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: alling error bug ### Your current environment ### Model Input Dumps Test code: ``` test_llm = ChatOpenAI( openai_api_key="xxx", openai_api_base="http://xxxxx:6000/v1", model_name="Qwen2.5-7B-Instruct", temperature=0.01,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rams(json=None, regex=None, choice=None, grammar=None, json_object=None, backend=None, whitespace_pattern=None), prompt_token_ids: [151644, 8948, 198, 2610, 525, 264, 10950, 17847, 382, 2, 13852, 271, 2610, 1231, 1618,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: alty=1.05, model_kwargs={"stop": [" ", " "], "extra_body": {"skip_special_tokens": False}}, ) agent = create_react_agent( model=test_llm, tools=[get_current_time, get_current_hour, get_current_date, get_current_week, ge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
