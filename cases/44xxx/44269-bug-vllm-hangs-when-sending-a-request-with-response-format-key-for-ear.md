# vllm-project/vllm#44269: [Bug]: vLLM hangs when sending a request with "response_format" key for early unsuppoted models like Minimax-M2.5

| 字段 | 值 |
| --- | --- |
| Issue | [#44269](https://github.com/vllm-project/vllm/issues/44269) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM hangs when sending a request with "response_format" key for early unsuppoted models like Minimax-M2.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when sending a request to Minimax-M2.5 server including response_format like curl -X POST -s http://xx.xx.xx.xx:xxxx/v1/chat/completions -H "Content-Type: application/json" -d '{"model": "minimax","messages": [{"role": "user", "content": "San Francisco is a"}],"max_tokens": 100,"temperature": 0, "stream": false, "response_format": {"json_schema": {"name": "ExtractedAnswer", "schema": {"additionalProperties": false, "properties": {"confidence": {"title": "Confidence", "type": "integer"}, "correct": {"enum": ["yes", "no"], "title": "Correct", "type": "string"}, "extracted_final_answer": {"title": "Extracted Final Answer", "type": "string"}, "reasoning": {"title": "Reasoning", "type": "string"}, "strict": {"const": true, "type": "boolean"}}, "required": ["extracted_final_answer", "reasoning", "correct", "confidence", "strict"], "type": "object"}, "strict": true}, "type": "json_schema"}}';echo it will hang and not get any output, the server behaves like it does not receive this request without any log. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vLLM hangs when sending a request with "response_format" key for early unsuppoted models like Minimax-M2.5 bug ### Your current environment ### 🐛 Describe the bug when sending a request to Minimax-M2.5 server inc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d '{"model": "minimax","messages": [{"role": "user", "content": "San Francisco is a"}],"max_tokens": 100,"temperature": 0, "stream": false, "response_format": {"json_schema": {"name": "ExtractedAnswer", "schema": {"addi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: og. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: : "San Francisco is a"}],"max_tokens": 100,"temperature": 0, "stream": false, "response_format": {"json_schema": {"name": "ExtractedAnswer", "schema": {"additionalProperties": false, "properties": {"confidence": {"title...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vLLM hangs when sending a request with "response_format" key for early unsuppoted models like Minimax-M2.5 bug ### Your current environment ### 🐛 Describe the bug when sending a request to Minimax-M2.5 server inc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
