# vllm-project/vllm#22932: [RFC]: Path to vLLM 1.0 Release

| 字段 | 值 |
| --- | --- |
| Issue | [#22932](https://github.com/vllm-project/vllm/issues/22932) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Path to vLLM 1.0 Release

### Issue 正文摘录

### Motivation. vLLM's V1 architecture has been in production for a while now, and we have seen good results with the transition from V0 to V1. We are now in progress of deprecating the V0 code path and removing the technical debt from vLLM. As we complete this effort, it is now time to begin planning for the 1.0 release which will occur sometime this fall. With the V1 engine update focused on refactoring and eliminating the technical debt in vLLM's internal subsystems, with the major version update for 1.0, we will now take the opportunity to clean up vLLM's external interfaces and adhere to a semantic versioning scheme. This is increasingly important as more interfaces are becoming pluggable in vLLM V1 - V0 Deprecation Issue: https://github.com/vllm-project/vllm/issues/18571 ### Proposed Change. We are developing a work plan towards this 1.0 release. Major items we have targeted are: - [ ] Stabilize and document the existing Pluggable Interfaces (`Scheduler`, `KVConnector`, `ModelRunner`, `Model`) - [ ] Clarify and document which subsystems are intended to be pluggable (public apis) vs not (private apis) - [ ] Stabilize and document `AsyncLLM` and `LLM` interfaces - what is publ...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: inating the technical debt in vLLM's internal subsystems, with the major version update for 1.0, we will now take the opportunity to clean up vLLM's external interfaces and adhere to a semantic versioning scheme. This i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Path to vLLM 1.0 Release RFC;keep-open ### Motivation. vLLM's V1 architecture has been in production for a while now, and we have seen good results with the transition from V0 to V1. We are now in progress of dep...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: document the existing Pluggable Interfaces (`Scheduler`, `KVConnector`, `ModelRunner`, `Model`) - [ ] Clarify and document which subsystems are intended to be pluggable (public apis) vs not (private apis) - [ ] Stabiliz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: @mgoin @ywang96 @yeqcharlotte @houseroad ### Any Other Things. What else are we missing ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ed are: - [ ] Stabilize and document the existing Pluggable Interfaces (`Scheduler`, `KVConnector`, `ModelRunner`, `Model`) - [ ] Clarify and document which subsystems are intended to be pluggable (public apis) vs not (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
