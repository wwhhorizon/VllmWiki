# vllm-project/vllm#23992: [Bug]: vLLM Deployment of Qwen3-8B Model Streaming Output Tool Content Missing Issue

| 字段 | 值 |
| --- | --- |
| Issue | [#23992](https://github.com/vllm-project/vllm/issues/23992) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM Deployment of Qwen3-8B Model Streaming Output Tool Content Missing Issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deploying the Qwen3-8B model using vLLM and providing an OpenAI-compatible API, it was found that tool call content is missing in streaming call scenarios. ## Problem Description When using non-streaming calls, the code runs normally and the tool call content is returned completely. As shown below: ```python async def main(): from langchain_mcp_adapters.client import MultiServerMCPClient client = MultiServerMCPClient( { "mcp-server-chart": { "command": "npx", "args": ["-y", "@antv/mcp-server-chart"], "transport": "stdio", } } ) tools = await client.get_tools() openai_tools = [convert_to_openai_tool(tool) for tool in tools] client = AsyncOpenAI(base_url="http://localhost:6006/v1", api_key="1111") response = await client.chat.completions.create( model="qwen3-8B", messages=[ { "role": "user", "content": "请你绘制10个点，y=x从(0,0)开始到(10,10)十个点", } ], tools=openai_tools, # type: ignore extra_body={"enable_thinking": False}, # stream=True, ) print(response.choices[0].message.tool_calls) if __name__ == "__main__": asyncio.run(main()) ``` The execution result is as follows: ```python [ChatCompletionMessageFunctionToolCall(id='chatcmpl-tool...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ow: ```python async def main(): from langchain_mcp_adapters.client import MultiServerMCPClient client = MultiServerMCPClient( { "mcp-server-chart": { "command": "npx", "args": ["-y", "@antv/mcp-server-chart"], "tra
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: oyment of Qwen3-8B Model Streaming Output Tool Content Missing Issue bug;stale ### Your current environment ### 🐛 Describe the bug When deploying the Qwen3-8B model using vLLM and providing an OpenAI-compatible API, it...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vLLM Deployment of Qwen3-8B Model Streaming Output Tool Content Missing Issue bug;stale ### Your current environment ### 🐛 Describe the bug When deploying the Qwen3-8B model using vLLM and providing an OpenAI-com...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
