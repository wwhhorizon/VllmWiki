# vllm-project/vllm#33421: [Bug]: FlashInfer backend stopped working with Batch Invariant after moving from 0.14.1 to 0.15.0, Qwen3-4B

| 字段 | 值 |
| --- | --- |
| Issue | [#33421](https://github.com/vllm-project/vllm/issues/33421) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 |  |
| Operator 关键词 | kernel |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer backend stopped working with Batch Invariant after moving from 0.14.1 to 0.15.0, Qwen3-4B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug flashinfer kernels fail to compile when VLLM_BATCH_INVARIANT=1 is set for Qwen3-4B Instruct 2507 on H100, it worked in 0.14.1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rrent environment ### 🐛 Describe the bug flashinfer kernels fail to compile when VLLM_BATCH_INVARIANT=1 is set for Qwen3-4B Instruct 2507 on H100, it worked in 0.14.1 ### Before submitting a new issue... - [x] Make sure...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: FlashInfer backend stopped working with Batch Invariant after moving from 0.14.1 to 0.15.0, Qwen3-4B bug;stale ### Your current environment ### 🐛 Describe the bug flashinfer kernels fail to compile when VLLM_BATC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: compile when VLLM_BATCH_INVARIANT=1 is set for Qwen3-4B Instruct 2507 on H100, it worked in 0.14.1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot liv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: stopped working with Batch Invariant after moving from 0.14.1 to 0.15.0, Qwen3-4B bug;stale ### Your current environment ### 🐛 Describe the bug flashinfer kernels fail to compile when VLLM_BATCH_INVARIANT=1 is set for Q...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ng with Batch Invariant after moving from 0.14.1 to 0.15.0, Qwen3-4B bug;stale ### Your current environment ### 🐛 Describe the bug flashinfer kernels fail to compile when VLLM_BATCH_INVARIANT=1 is set for Qwen3-4B Instr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
