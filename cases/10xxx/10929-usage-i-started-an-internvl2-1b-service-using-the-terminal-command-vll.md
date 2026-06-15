# vllm-project/vllm#10929: [Usage]: I started an internvl2-1b service using the terminal command vllm serve ./internvl2-1b/ --tensor-parallel-size 1 --trust-remote-code. How can I implement this functionality with a Python script, as I want to customize some logs?

| 字段 | 值 |
| --- | --- |
| Issue | [#10929](https://github.com/vllm-project/vllm/issues/10929) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: I started an internvl2-1b service using the terminal command vllm serve ./internvl2-1b/ --tensor-parallel-size 1 --trust-remote-code. How can I implement this functionality with a Python script, as I want to customize some logs?

### Issue 正文摘录

### Your current environment vllm serve ./internvl2-1b/ --tensor-parallel-size 1 --trust-remote-code ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: de ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [X] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: I started an internvl2-1b service using the terminal command vllm serve ./internvl2-1b/ --tensor-parallel-size 1 --trust-remote-code. How can I implement this functionality with a Python script, as I want to cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ctionality with a Python script, as I want to customize some logs? usage;stale ### Your current environment vllm serve ./internvl2-1b/ --tensor-parallel-size 1 --trust-remote-code ### How would you like to use vllm I wa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
