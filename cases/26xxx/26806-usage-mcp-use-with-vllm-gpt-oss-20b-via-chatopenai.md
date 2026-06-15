# vllm-project/vllm#26806: [Usage]: MCP-USE with VLLM gpt-oss:20b via ChatOpenAI

| 字段 | 值 |
| --- | --- |
| Issue | [#26806](https://github.com/vllm-project/vllm/issues/26806) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: MCP-USE with VLLM gpt-oss:20b via ChatOpenAI

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm i am trying to create an agent using gpt-oss:20B with mcp-use most times the model returns "Agent completed the task successfully.", and sometimes the proper output which is required ### code `vllm serve openai/gpt-oss-20b --max-model-len 100000 --gpu-memory-utilization 0.9 --port 8000 --tool-call-parser openai --enable-auto-tool-choice` client = MCPClient.from_dict(config) llm = ChatOpenAI( model="openai/gpt-oss-20b", base_url="http://127.0.0.1:8000/v1", api_key="not-needed", temperature=0.8, max_tokens=2048 ) agent = MCPAgent(llm=llm, client=client, max_steps=30) also raising this on mcp-use ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: MCP-USE with VLLM gpt-oss:20b via ChatOpenAI usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm i am trying to create an agent using gp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: use ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: MCP-USE with VLLM gpt-oss:20b via ChatOpenAI usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm i am trying to create an agent using gp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
