# vllm-project/vllm#9203: [RFC]: Shared Mixture of Experts

| 字段 | 值 |
| --- | --- |
| Issue | [#9203](https://github.com/vllm-project/vllm/issues/9203) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Shared Mixture of Experts

### Issue 正文摘录

### Motivation. ### Motivation We propose to add a new Mixtral-type model which can share experts across multiple model instances belonging to different clients. The change would automatically detect the identical experts and share them across instances. The de-duplication of experts reduces GPU memory requirement. Moreover, the requests directed towards different Mixtral model instances are batched during execution. This also means that the shared experts can efficiently process the requests from multiple clients in a single batch. The figure shows the request routing with 2 model instances that share 3 experts. The combination of experts (and routers) shown below will be served as a single model instance. Recent research suggests that it may be possible to find many identical experts in a cluster serving many Mixtral models, thus the opportunity to share such experts across many instances. For instance, BTX [1] from Meta AI separately trains LLMs on different datasets and integrates them as experts into an MoE. Mergoo [2] toolkit allows users to compose MoE from existing LLMs. DeepSeek-AI [3] proposes fine-tuning individual experts. MergeKit [4] also provides a toolkit to merge...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [RFC]: Shared Mixture of Experts RFC;stale ### Motivation. ### Motivation We propose to add a new Mixtral-type model which can share experts across multiple model instances belonging to different clients. The change wou...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Shared Mixture of Experts RFC;stale ### Motivation. ### Motivation We propose to add a new Mixtral-type model which can share experts across multiple model instances belonging to different clients. The change wou...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: n host several Mixtral models with little overhead in terms of inference latency. The overhead is from routing of requests across increasing models. 1. BTX: Mixing Expert LLMs into a Mixture-of-Experts LLM https://arxiv...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ts from multiple clients in a single batch. The figure shows the request routing with 2 model instances that share 3 experts. The combination of experts (and routers) shown below will be served as a single model instanc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: atched during execution. This also means that the shared experts can efficiently process the requests from multiple clients in a single batch. The figure shows the request routing with 2 model instances that share 3 exp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
