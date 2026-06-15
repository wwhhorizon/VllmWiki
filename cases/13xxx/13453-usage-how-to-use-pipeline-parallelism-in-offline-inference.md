# vllm-project/vllm#13453: [Usage]: How to use pipeline parallelism in offline inference?

| 字段 | 值 |
| --- | --- |
| Issue | [#13453](https://github.com/vllm-project/vllm/issues/13453) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use pipeline parallelism in offline inference?

### Issue 正文摘录

### Your current environment Hi I want to know how to use pipeline parallelism in offline inference? Can anyone give a concrete example about how to use pipeline? Looking forward to the reply ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ly ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: How to use pipeline parallelism in offline inference? usage;stale ### Your current environment Hi I want to know how to use pipeline parallelism in offline inference? Can anyone give a concrete example about ho...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to use pipeline parallelism in offline inference? usage;stale ### Your current environment Hi I want to know how to use pipeline parallelism in offline inference? Can anyone give a concrete example about ho...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
