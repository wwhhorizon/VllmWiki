# vllm-project/vllm#13056: [Feature]: Add an endpoint to know the server config

| 字段 | 值 |
| --- | --- |
| Issue | [#13056](https://github.com/vllm-project/vllm/issues/13056) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add an endpoint to know the server config

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I use vLLM a lot, especially via the OpenAI server. There are many parameters that can be passed when starting the server. For some, it is quite intuitive to understand what they do. For others, it’s more complicated. Some parameters have default values published in the documentation, while others do not. I looked into the code a bit, and it seems that for some essential parameters (e.g., `max-num-batched-tokens`), not only is there no documented default value, but if none is provided, it is dynamically chosen based on hardcoded rules in the code. These rules take into account several factors, including the hardware on which the server is running. Exemple : ``` python if "h100" in device_name or "h200" in device_name: # For H100 and H200, we use larger default values. default_max_num_batched_tokens = { UsageContext.LLM_CLASS: 16384, UsageContext.OPENAI_API_SERVER: 8192, } else: # TODO(woosuk): Tune the default values for other hardware. default_max_num_batched_tokens = { UsageContext.LLM_CLASS: 8192, UsageContext.OPENAI_API_SERVER: 2048, } ``` (I have to admit that I didn't investigate the code very far.) What would be good for this is to ha...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the hardware on which the server is running. Exemple : ``` python if "h100" in device_name or "h200" in device_name: # For H100 and H200, we use larger default values. default_max_num_batched_tokens = { UsageContext.LLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add an endpoint to know the server config feature request;stale ### 🚀 The feature, motivation and pitch I use vLLM a lot, especially via the OpenAI server. There are many parameters that can be passed when st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: est;stale ### 🚀 The feature, motivation and pitch I use vLLM a lot, especially via the OpenAI server. There are many parameters that can be passed when starting the server. For some, it is quite intuitive to understand...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: t.LLM_CLASS: 16384, UsageContext.OPENAI_API_SERVER: 8192, } else: # TODO(woosuk): Tune the default values for other hardware. default_max_num_batched_tokens = { UsageContext.LLM_CLASS: 8192, UsageContext.OPENAI_API_SERV...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Add an endpoint to know the server config feature request;stale ### 🚀 The feature, motivation and pitch I use vLLM a lot, especially via the OpenAI server. There are many parameters that can be passed when st...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
