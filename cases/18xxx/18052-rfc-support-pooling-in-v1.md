# vllm-project/vllm#18052: [RFC]: Support pooling in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#18052](https://github.com/vllm-project/vllm/issues/18052) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support pooling in V1

### Issue 正文摘录

### Motivation. In many use cases, such as Search, Recommendation, Content Understanding, LLMs are utilized to generate embeddings for downstream use. In these cases, we do not need the sampling steps. In V0, pooling/embedding use cases are supported ([doc](https://docs.vllm.ai/en/v0.8.3/models/pooling_models.html)). Currently, when a pooling task is specified, vLLM would [fallback](https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/engine/arg_utils.py#L1397) to V0 on engine initialization. We propose to add pooling support in V1. I'd like to seek some early feedback on the ideas as well as implementations in https://github.com/22quinn/vllm/pull/2 before I fully implement it. ### Proposed Change. ### V0 Overview Key pointers: * Worker initialize with a pooling model runner: [code](https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/worker/worker.py#L79) * encode call adds a request with PoolingParams: [code](https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/entrypoints/llm.py#L946) * Pooling model runner executes the model and returns the pooled hidden states: [code](https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/worker/pooling_model_runner.py#L148) Key design: * P...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Support pooling in V1 RFC;stale ### Motivation. In many use cases, such as Search, Recommendation, Content Understanding, LLMs are utilized to generate embeddings for downstream use. In these cases, we do not nee...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: _models.html)). Currently, when a pooling task is specified, vLLM would [fallback](https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/engine/arg_utils.py#L1397) to V0 on engine initialization. We propose to add pooli...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: /embedding use cases are supported ([doc](https://docs.vllm.ai/en/v0.8.3/models/pooling_models.html)). Currently, when a pooling task is specified, vLLM would [fallback](https://github.com/vllm-project/vllm/blob/v0.8.5/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 0.8.3/models/pooling_models.html)). Currently, when a pooling task is specified, vLLM would [fallback](https://github.com/vllm-project/vllm/blob/v0.8.5/vllm/engine/arg_utils.py#L1397) to V0 on engine initialization. We...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rt pooling in V1 RFC;stale ### Motivation. In many use cases, such as Search, Recommendation, Content Understanding, LLMs are utilized to generate embeddings for downstream use. In these cases, we do not need the sampli...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
