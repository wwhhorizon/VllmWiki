# vllm-project/vllm#33455: [Feature][Performance][Speculative Decoding]: Kernel Fusion for EAGLE Steps

| 字段 | 值 |
| --- | --- |
| Issue | [#33455](https://github.com/vllm-project/vllm/issues/33455) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature][Performance][Speculative Decoding]: Kernel Fusion for EAGLE Steps

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Updating the slot mapping and metadata between EAGLE steps issues many small kernels that could be fused into a single triton kernel to reduce the overhead of EAGLE drafting. An alternative solution to this problem would be to apply torch.compile on the entire autoregressive drafting portion for EAGLE. This may be more complex to implement, but would be more flexible for future changes and might enable future work on fusing multiple EAGLE iterations into a single CUDA graph. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#33503 feat(spec_decode): fuse EAGLE step slot mapping and metadata updates

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Feature][Performance][Speculative Decoding]: Kernel Fusion for EAGLE Steps feature request;stale ### 🚀 The feature, motivation and pitch Updating the slot mapping and metadata between EAGLE steps issues many small kern...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: afting. An alternative solution to this problem would be to apply torch.compile on the entire autoregressive drafting portion for EAGLE. This may be more complex to implement, but would be more flexible for future chang...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Updating the slot mapping and metadata between EAGLE steps issues many small kernels that could be fused into a single triton kernel to reduce the overhead of EAGLE drafting. An alternative solution to this problem woul...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ture request;stale ### 🚀 The feature, motivation and pitch Updating the slot mapping and metadata between EAGLE steps issues many small kernels that could be fused into a single triton kernel to reduce the overhead of E...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: EAGLE steps issues many small kernels that could be fused into a single triton kernel to reduce the overhead of EAGLE drafting. An alternative solution to this problem would be to apply torch.compile on the entire autor...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33503](https://github.com/vllm-project/vllm/pull/33503) | mentioned | 0.6 | feat(spec_decode): fuse EAGLE step slot mapping and metadata updates | ive drafting steps to reduce kernel launch overhead. **Addresses:** [#33455](https://github.com/vllm-project/vllm/issues/33455) Between EAGLE steps, slot mapping and metadata upda… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
