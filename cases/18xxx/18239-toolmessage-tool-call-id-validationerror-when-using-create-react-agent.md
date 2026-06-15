# vllm-project/vllm#18239: ToolMessage tool_call_id ValidationError When Using create_react_agent

| 字段 | 值 |
| --- | --- |
| Issue | [#18239](https://github.com/vllm-project/vllm/issues/18239) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ToolMessage tool_call_id ValidationError When Using create_react_agent

### Issue 正文摘录

### Example Code ```python param_parser_model = tool_model.bind_tools([db_param_parser], tool_choice="db_param_parser") param_parser_agent = create_react_agent(name=AGENT_NAMES['param_parser'], model=param_parser_model, tools=[db_param_parser], prompt=TIME_PROMPT) ``` ### Error Message and Stack Trace (if applicable) ```shell langgraph-api-1 | Traceback (most recent call last): langgraph-api-1 | File "/api/langgraph_api/worker.py", line 144, in worker langgraph-api-1 | File "/usr/local/lib/python3.11/asyncio/tasks.py", line 489, in wait_for langgraph-api-1 | return fut.result() langgraph-api-1 | ^^^^^^^^^^^^ langgraph-api-1 | File "/api/langgraph_api/stream.py", line 269, in consume langgraph-api-1 | File "/api/langgraph_api/stream.py", line 258, in consume langgraph-api-1 | File "/api/langgraph_api/stream.py", line 209, in astream_state langgraph-api-1 | File "/api/langgraph_api/asyncio.py", line 82, in wait_if_not_done langgraph-api-1 | File "/usr/local/lib/python3.11/site-packages/langgraph/pregel/__init__.py", line 2676, in astream langgraph-api-1 | async for _ in runner.atick( langgraph-api-1 | File "/deps/__outer_agent/agent/router/complaint.py", line 39, in param_parser_nod...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: create_react_agent usage;stale ### Example Code ```python param_parser_model = tool_model.bind_tools([db_param_parser], tool_choice="db_param_parser") param_parser_agent = create_react_agent(name=AGENT_NAMES['param_pars...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 144, in worker langgraph-api-1 | File "/usr/local/lib/python3.11/asyncio/tasks.py", line 489, in wait_for langgraph-api-1 | return fut.result() langgraph-api-1 | ^^^^^^^^^^^^ langgraph-api-1 | File "/api/langgraph_api/s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: {'index': 0, 'id': None, 'function': {'arguments': str(args), 'name': 'search'},'type': 'function'}]}, response_metadata={}, id=f'run--{uuid.uuid4()}', tool_calls=[{'name': 'search', 'args': args, 'id': None, 'type': 't...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ments': str(args), 'name': 'search'},'type': 'function'}]}, response_metadata={}, id=f'run--{uuid.uuid4()}', tool_calls=[{'name': 'search', 'args': args, 'id': None, 'type': 'tool_call'}], usage_metadata={'input_tokens'...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: _ in runner.atick( langgraph-api-1 | File "/deps/__outer_agent/agent/router/complaint.py", line 39, in param_parser_node langgraph-api-1 | result = await param_parser_agent.ainvoke(asdict(state)) langgraph-api-1 | ^^^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
