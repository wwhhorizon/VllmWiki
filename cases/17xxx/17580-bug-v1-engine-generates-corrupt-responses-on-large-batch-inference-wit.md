# vllm-project/vllm#17580: [Bug]: V1 Engine generates corrupt responses on large batch inference with long sequences and fails in seed control

| 字段 | 值 |
| --- | --- |
| Issue | [#17580](https://github.com/vllm-project/vllm/issues/17580) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | edge_case |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 Engine generates corrupt responses on large batch inference with long sequences and fails in seed control

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is a new issue related to [#17524 ](https://github.com/vllm-project/vllm/issues/17524). Using V1 engine in my scene will cause some weird behaviors, including: 1. Reproducibility: seed control fails. Details in [#17524 ](https://github.com/vllm-project/vllm/issues/17524). 2. Serious generation quality degradation on batch inference with long sequences. Test Scene that causes quality degradation issues: - V0.8.5 with V1 engine - and, QwQ-32B & Qwen-32B - and, offline batch inference. Codes below - and, a large batch of 400 cases. - and, each case has ~20k tokens Test Scene that won't cause issues: - V0 engine - or, small batch ~ 20, with long sequences ~20k tokens - or, small sequences with ~1k tokens, with large batch Two degradation outputs: ```plaintext " \nOkay, I need to tackle these two tasks based on the provided document about the Chronosynclastic Dominion of Aethelgard. Let me start by understanding the requirements.\n\n The user has given a comprehensive document on Aethelgard and wants a precise task. The document is extensive, and detailed. My task is to execute the following directive.\n\n## \n\nThe task is to sy...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: e has ~20k tokens Test Scene that won't cause issues: - V0 engine - or, small batch ~ 20, with long sequences ~20k tokens - or, small sequences with ~1k tokens, with large batch Two degradation outputs: ```plaintext " \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ngine in my scene will cause some weird behaviors, including: 1. Reproducibility: seed control fails. Details in [#17524 ](https://github.com/vllm-project/vllm/issues/17524). 2. Serious generation quality degradation on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ses quality degradation issues: - V0.8.5 with V1 engine - and, QwQ-32B & Qwen-32B - and, offline batch inference. Codes below - and, a large batch of 400 cases. - and, each case has ~20k tokens Test Scene that won't cau...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: large batch inference with long sequences and fails in seed control bug;stale ### Your current environment ### 🐛 Describe the bug This is a new issue related to [#17524 ](https://github.com/vllm-project/vllm/issues/1752...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: generation quality degradation on batch inference with long sequences. Test Scene that causes quality degradation issues: - V0.8.5 with V1 engine - and, QwQ-32B & Qwen-32B - and, offline batch inference. Codes below - a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
