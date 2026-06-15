# vllm-project/vllm#35460: [Installation]: Can VLLM 0.16.0 release a WHL package for CUDA12？

| 字段 | 值 |
| --- | --- |
| Issue | [#35460](https://github.com/vllm-project/vllm/issues/35460) |
| 状态 | open |
| 标签 | installation;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Can VLLM 0.16.0 release a WHL package for CUDA12？

### Issue 正文摘录

### Your current environment Driver Version: 560.35.05 CUDA Version: 12.6 Unable to install in offline environment ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Can VLLM 0.16.0 release a WHL package for CUDA12？ installation;stale ### Your current environment Driver Version: 560.35.05 CUDA Version: 12.6 Unable to install in offline environment ### Before subm
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: Can VLLM 0.16.0 release a WHL package for CUDA12？ installation;stale ### Your current environment Driver Version: 560.35.05 CUDA Version: 12.6 Unable to install in offline environment ### Before submitti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: llation]: Can VLLM 0.16.0 release a WHL package for CUDA12？ installation;stale ### Your current environment Driver Version: 560.35.05 CUDA Version: 12.6 Unable to install in offline environment ### Before submitting a n...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development cuda env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
