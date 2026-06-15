# vllm-project/vllm#10093: [Usage]: disable pydantic request validation

| 字段 | 值 |
| --- | --- |
| Issue | [#10093](https://github.com/vllm-project/vllm/issues/10093) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: disable pydantic request validation

### Issue 正文摘录

### Your current environment How do I ignore request validation through the openai compatible api? I want to pass in custom roles. ### How would you like to use vllm ``` Error processing publish message Traceback (most recent call last): File "/home/acidhax/dev/autogen/python/packages/autogen-core/src/autogen_core/application/_single_threaded_agent_runtime.py", line 385, in _process_publish await asyncio.gather(*responses) File "/home/acidhax/dev/autogen/python/packages/autogen-core/src/autogen_core/application/_single_threaded_agent_runtime.py", line 377, in _on_message return await agent.on_message( File "/home/acidhax/dev/autogen/python/packages/autogen-core/src/autogen_core/components/_routed_agent.py", line 468, in on_message return await h(self, message, ctx) File "/home/acidhax/dev/autogen/python/packages/autogen-core/src/autogen_core/components/_routed_agent.py", line 148, in wrapper return_value = await func(self, message, ctx) File "/home/acidhax/dev/autogen/python/packages/autogen-magentic-one/src/autogen_magentic_one/agents/base_agent.py", line 83, in handle_incoming_message await future File "/home/acidhax/dev/autogen/python/packages/autogen-magentic-one/src/autogen_m...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: chestrator.py", line 153, in _initialize_task response = await self._model_client.create( File "/home/acidhax/dev/autogen/python/packages/autogen-ext/src/autogen_ext/models/_openai/_openai_client.py", line 479, in creat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: disable pydantic request validation usage;stale ### Your current environment How do I ignore request validation through the openai compatible api? I want to pass in custom roles. ### How would you like to use v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: essing publish message Traceback (most recent call last): File "/home/acidhax/dev/autogen/python/packages/autogen-core/src/autogen_core/application/_single_threaded_agent_runtime.py", line 385, in _process_publish await...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
