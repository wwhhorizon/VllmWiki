# vllm-project/vllm#24603: [RFC]: Responses API full functionality without stores

| 字段 | 值 |
| --- | --- |
| Issue | [#24603](https://github.com/vllm-project/vllm/issues/24603) |
| 状态 | closed |
| 标签 | RFC;stale;gpt-oss |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Responses API full functionality without stores

### Issue 正文摘录

### Motivation. The current implementation for the Responses API requires the responses store and message store to be enabled in order to provide full functionality for the API. This functionality is critical for large scale deployments of vLLM as you need to be able to route follow up requests to different servers, which is not currently possible. These stores are required because the Responses API is meant to be able to keep state in the backend to use for subsequent generations without showing it to the use. For OpenAI this is how they quote better performance for their models when using Responses API compared to Chat Completions API, since they can do things like use the full reasoning messages instead of just summaries of reasoning messages send back by the user. Additionally, there is metadata in messages that is not present in the Responses API output (i.e OpenAI Harmony "channel") that is useful for developers to verify that implementations are correct. The current implementation: For the first request: For a follow up request: These diagrams show the use of the stores between requests and what gets persisted in them. ### Proposed Change. The proposed change is to add addi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Responses API full functionality without stores RFC;stale;gpt-oss ### Motivation. The current implementation for the Responses API requires the responses store and message store to be enabled in order to provide...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Responses API full functionality without stores RFC;stale;gpt-oss ### Motivation. The current implementation for the Responses API requires the responses store and message store to be enabled in order to provide...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uired because the Responses API is meant to be able to keep state in the backend to use for subsequent generations without showing it to the use. For OpenAI this is how they quote better performance for their models whe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: utItem` list for follow up requests because it is sometimes necessary to link metadata between requests. For example, Harmony messages don't have `tool_call_id`, only the `ResponseOutputItem` does, so to output the corr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: full functionality for the API. This functionality is critical for large scale deployments of vLLM as you need to be able to route follow up requests to different servers, which is not currently possible. These stores a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
