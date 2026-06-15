# vllm-project/vllm#9960: [Installation]: I was never able to install it, which cuda version is required?

| 字段 | 值 |
| --- | --- |
| Issue | [#9960](https://github.com/vllm-project/vllm/issues/9960) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: I was never able to install it, which cuda version is required?

### Issue 正文摘录

### Your current environment I use ubunt 22.04 Installing this is almost impossible, what are actually requirements lets say for cuda. I spend many hours trying to install and never worked, there way always an error, something related to cuda version. ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: I was never able to install it, which cuda version is required? installation;stale ### Your current environment I use ubunt 22.04 Installing this is almost impossible, what are actually requirements lets
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: I was never able to install it, which cuda version is required? installation;stale ### Your current environment I use ubunt 22.04 Installing this is almost impossible, what are actually requirements lets...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s never able to install it, which cuda version is required? installation;stale ### Your current environment I use ubunt 22.04 Installing this is almost impossible, what are actually requirements lets say for cuda. I spe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
