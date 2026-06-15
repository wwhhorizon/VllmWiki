# vllm-project/vllm#19061: [RFC]: Drop CUDA 11.8 Support

| 字段 | 值 |
| --- | --- |
| Issue | [#19061](https://github.com/vllm-project/vllm/issues/19061) |
| 状态 | closed |
| 标签 | RFC;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Drop CUDA 11.8 Support

### Issue 正文摘录

### Motivation. We plan to drop CUDA 11.8 Support when PyTorch release 2.8 https://github.com/pytorch/pytorch/issues/147383 ### Proposed Change. This change means we no longer ensure vLLM can properly build using the CUDA 11.8 toolkit. No wheels will be produced as part of release process. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: roposed Change. This change means we no longer ensure vLLM can properly build using the CUDA 11.8 toolkit. No wheels will be produced as part of release process. ### Feedback Period. _No response_ ### CC List. _No respo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Drop CUDA 11.8 Support RFC;unstale ### Motivation. We plan to drop CUDA 11.8 Support when PyTorch release 2.8 https://github.com/pytorch/pytorch/issues/147383 ### Proposed Change. This change means we no longer e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [RFC]: Drop CUDA 11.8 Support RFC;unstale ### Motivation. We plan to drop CUDA 11.8 Support when PyTorch release 2.8 https://github.com/pytorch/pytorch/issues/147383 ### Proposed Change. This change means we no longer e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error Motivation.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
