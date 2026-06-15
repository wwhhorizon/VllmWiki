# vllm-project/vllm#2577: Longer stop sequence not working in streaming mode

| 字段 | 值 |
| --- | --- |
| Issue | [#2577](https://github.com/vllm-project/vllm/issues/2577) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Longer stop sequence not working in streaming mode

### Issue 正文摘录

Have problems with LangChain default ReAct pipeline, because the stop tokens behavt differently between streaming and not streaming. Example: curl -X POST http://ai1.dev.init:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "mistralai/Mixtral-8x7B-Instruct-v0.1", "messages": [ { "role": "user", "content": "Answer the following questions as best you can. You have access to the following tools:\n\nWikipedia: A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, facts, historical events, or other subjects. Input should be a search query.\n\nUse the following format:\n\nQuestion: the input question you must answer\nThought: you should always think about what to do\nAction: the action to take, should be one of [Wikipedia]\nAction Input: the input to the action\nObservation: the result of the action\n... (this Thought/Action/Action Input/Observation can repeat N times)\nThought: I now know the final answer\nFinal Answer: the final answer to the original input question\n\nBegin!\n\nQuestion: what is LangChain?\nThought:" } ], "max_tokens": 1000, "n": 1, "stop": ["\nObservation"], "stream": false, "...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -H "Content-Type: application/json" \ -d '{ "model": "mistralai/Mixtral-8x7B-Instruct-v0.1", "messages": [ { "role": "user", "content": "Answer the following questions as best you can.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: panies, facts, historical events, or other subjects. Input should be a search query.\n\nUse the following format:\n\nQuestion: the input question you must answer\nThought: you should always think about what to do\nActio...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 1, "stop": ["\nObservation"], "stream": false, "temperature": 0.2, "top_p": 0.1 }' Result: {"id":"cmpl-5516211747854a32ad63d5ebb8d52d14","object":"chat.completion","created":522917,"model":"mistralai/Mixtral-8x7B-

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
