# vllm-project/vllm#28243: [RFC]: Externally managed elastic EP (decouple from Ray backend)

| 字段 | 值 |
| --- | --- |
| Issue | [#28243](https://github.com/vllm-project/vllm/issues/28243) |
| 状态 | open |
| 标签 | RFC;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Externally managed elastic EP (decouple from Ray backend)

### Issue 正文摘录

### Motivation. The `scale_elastic_ep()` API is tightly-coupled with Ray and conflicts with k8s orchestrators (AIBrix, llm-d, Dynamo, etc). We should allow scaling decisions should be made externally (i.e. by an orchestrator), allowing them to manage pod scaling from the operator level and implement their own scaling policies. --- ### Proposed Change. #### Overview This RFC builds on top of #20323 and is relevant for phase 2 of #27774 Currently, elastic EP scaling forces use of `DPLBAsyncMPClient` which uses the `CoreEngineActorManager` to create new Ray Actors holding `EngineCore` instances on scale-up/scale-down. However, there should exist an alternate path where elastic EP can be managed externally, allowing the orchestrator to dynamically create/tear down pods that each correspond to a DP rank. There already exists a path for DP engines/ranks to be managed by the orchestrator, via `DPAsyncMPClient`. Our goal is to extend `DPAsyncMPClient` to support externally-managed elastic EP while ensuring internally managed elastic EP works well. ![Proposed architecture](https://github.com/user-attachments/assets/e7d2295f-c7fc-42cb-8ece-6b0f471f8612) *Proposed architecture for managing e...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 8s orchestrators (AIBrix, llm-d, Dynamo, etc). We should allow scaling decisions should be made externally (i.e. by an orchestrator), allowing them to manage pod scaling from the operator level and implement their own s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Externally managed elastic EP (decouple from Ray backend) RFC;unstale ### Motivation. The `scale_elastic_ep()` API is tightly-coupled with Ray and conflicts with k8s orchestrators (AIBrix, llm-d, Dynamo, etc). We...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: EP while ensuring internally managed elastic EP works well. ![Proposed architecture](https://github.com/user-attachments/assets/e7d2295f-c7fc-42cb-8ece-6b0f471f8612) *Proposed architecture for managing elastic EP extern...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [RFC]: Externally managed elastic EP (decouple from Ray backend) RFC;unstale ### Motivation. The `scale_elastic_ep()` API is tightly-coupled with Ray and conflicts with k8s orchestrators (AIBrix, llm-d, Dynamo, etc). We...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: elastic EP (decouple from Ray backend) RFC;unstale ### Motivation. The `scale_elastic_ep()` API is tightly-coupled with Ray and conflicts with k8s orchestrators (AIBrix, llm-d, Dynamo, etc). We should allow scaling deci...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
