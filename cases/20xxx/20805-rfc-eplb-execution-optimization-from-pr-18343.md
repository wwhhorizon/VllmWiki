# vllm-project/vllm#20805: [RFC]: EPLB Execution Optimization From pr 18343

| 字段 | 值 |
| --- | --- |
| Issue | [#20805](https://github.com/vllm-project/vllm/issues/20805) |
| 状态 | closed |
| 标签 | RFC;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;moe |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;moe |
| 症状 | slowdown |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: EPLB Execution Optimization From pr 18343

### Issue 正文摘录

### Motivation. #18343 - EPLB Execution - [ ] Parallelize the rearrangement algorithm (calculating new expert mapping, not the communication) - [x] Shuffle one layer at once and use multiple steps, to lower the impact on inter-token latency - [x] Investigate should we pre-allocate expert weight buffer used for transferring - [ ] Take locality into consideration in expert weight transmission, e.g. prioritize transferring to GPUs on the same node - [x] Use cuda.Stream() asynchronously moves the weight to the buffer ### Proposed Change. Advantages over the synchronous solution: TTFT/TPOT fluctuations are small. The synchronous solution will block reasoning when reordering, causing TTFT/TPOT time to increase by hundreds of milliseconds. ### Feedback Period. July 11th ~ July 30th ### CC List. @abmfy ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#18343 [Feature] Expert Parallelism Load Balancer (EPLB) | #20990 [Performance] EPLB Execution Optimization | #21813 [WIP][Performance] EPLB Execution Optimization | #22179 [EPLB] Optimize EPLB for Async Rearrange Experts

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ransferring - [ ] Take locality into consideration in expert weight transmission, e.g. prioritize transferring to GPUs on the same node - [x] Use cuda.Stream() asynchronously moves the weight to the buffer ### Proposed...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: n - [ ] Parallelize the rearrangement algorithm (calculating new expert mapping, not the communication) - [x] Shuffle one layer at once and use multiple steps, to lower the impact on inter-token latency - [x] Investigat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: layer at once and use multiple steps, to lower the impact on inter-token latency - [x] Investigate should we pre-allocate expert weight buffer used for transferring - [ ] Take locality into consideration in expert weigh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: xecution - [ ] Parallelize the rearrangement algorithm (calculating new expert mapping, not the communication) - [x] Shuffle one layer at once and use multiple steps, to lower the impact on inter-token latency - [x] Inv...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: EPLB Execution Optimization From pr 18343 RFC;unstale ### Motivation. #18343 - EPLB Execution - [ ] Parallelize the rearrangement algorithm (calculating new expert mapping, not the communication) - [x] Shuffle on...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18343](https://github.com/vllm-project/vllm/pull/18343) | mentioned | 0.45 | [Feature] Expert Parallelism Load Balancer (EPLB) | [rfc]: eplb execution optimization from pr 18343 ### motivation. #18343 - eplb execution - [ ] parallelize the rearrangement algorithm (calculating new expert mapping, not the co |
| [#20990](https://github.com/vllm-project/vllm/pull/20990) | mentioned | 0.6 | [Performance] EPLB Execution Optimization | pported_models.md` and `examples` for a new model. ## Purpose issue #20805 pr #18343 EPLB Execution - [ ] Parallelize the rearrangement algorithm (calculating new expert mapping, n |
| [#21813](https://github.com/vllm-project/vllm/pull/21813) | mentioned | 0.6 | [WIP][Performance] EPLB Execution Optimization | pported_models.md` and `examples` for a new model. ## Purpose issue #20805 pr #18343 EPLB Execution - [ ] Parallelize the rearrangement algorithm (calculating new expert mapping, n |
| [#22179](https://github.com/vllm-project/vllm/pull/22179) | mentioned | 0.6 | [EPLB] Optimize EPLB for Async Rearrange Experts  | pported_models.md` and `examples` for a new model. ## Purpose issue #20805 #24116 pr #18343 EPLB Execution - [ ] Parallelize the rearrangement algorithm (calculating new expert ma |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
