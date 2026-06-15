# vllm-project/vllm#5699: [Misc]: output text is not match with first top_logprobs  item on stream mode.

| 字段 | 值 |
| --- | --- |
| Issue | [#5699](https://github.com/vllm-project/vllm/issues/5699) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: output text is not match with first top_logprobs  item on stream mode.

### Issue 正文摘录

### Anything you want to discuss about vllm. Env: vllm: v0.4.1-v0.5.0 request parms { "prompt": ( "function_metadata\n\nAssistant have access to the following functions. Use them if required:\n" "[{\"type\": \"function\", \"function\": {\"name\": \"calculate_triangle_area\", \"description\": \"Calculate the area of a triangle given its base and height.\", \"parameters\": {\"type\": \"object\", \"properties\": {\"base\": {\"type\": \"number\", \"description\": \"The base of the triangle.\"}, \"height\": {\"type\": \"number\", \"description\": \"The height of the triangle.\"}, \"unit\": {\"type\": \"string\", \"description\": \"The unit of measure (defaults to 'units' if not specified)\"}}, \"required\": [\"base\", \"height\"]}}}]user\n\n" "Find the area of a triangle with a base of 10 units and height of 5 units. assistant\n\n" ), "max_tokens": 500, "temperature": 0.5, "repetition_penalty": 1.0, "presence_penalty": 0.0, "top_k": 50, "logprobs": False, "stop":[' '], "skip_special_tokens":True, "spaces_between_special_tokens":True, "stream":True, } Streaming response: data: {"id":"cmpl-02313246eab24d57b890ad13fd0b57f0","created":1718849637,"model":"/models/llama3-8b-instruct-ft-0522/...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: m: v0.4.1-v0.5.0 request parms { "prompt": ( "function_metadata\n\nAssistant have access to the following functions. Use them if required:\n" "[{\"type\": \"function\", \"function\": {\"name\": \"calculate_triangle_area...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ata: {"id":"cmpl-02313246eab24d57b890ad13fd0b57f0","created":1718849637,"model":"/models/llama3-8b-instruct-ft-0522/","choices":[{"index":0,"text":" "],"top_logprobs":[{" ":0.0}]},"finish_reason":null,"stop_reason":null...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: : output text is not match with first top_logprobs item on stream mode. stale ### Anything you want to discuss about vllm. Env: vllm: v0.4.1-v0.5.0 request parms { "prompt": ( "function_metadata\n\nAssistant have access...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ", \"description\": \"The unit of measure (defaults to 'units' if not specified)\"}}, \"required\": [\"base\", \"height\"]}}}]user\n\n" "Find the area of a triangle with a base of 10 units and height of 5 units. assista...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
