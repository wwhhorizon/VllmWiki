# vllm-project/vllm#7958: [Usage]: How to specify certain GPUs for Tensor Parallelism and Pipeline Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#7958](https://github.com/vllm-project/vllm/issues/7958) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to specify certain GPUs for Tensor Parallelism and Pipeline Parallelism

### Issue 正文摘录

### Your current environment I have a server with only one NVLink connection, so I need to use pipeline parallelism and tensor parallelism within a single node to improve its performance. I would like to know how to specify the corresponding GPUs for this setup (since tensor parallelism requires [GPU0, GPU2] and [GPU1, GPU3], and pipeline parallelism should occur between [GPU0, GPU2] and [GPU1, GPU3]). How should I specify the api_server parameters to achieve this? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Usage]: How to specify certain GPUs for Tensor Parallelism and Pipeline Parallelism usage;stale ### Your current environment I have a server with only one NVLink connection, so I need to use pipeline parallelism and te...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: How to specify certain GPUs for Tensor Parallelism and Pipeline Parallelism usage;stale ### Your current environment I have a server with only one NVLink connection, so I need to use pipeline parallelism and te...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [X] Make sure you already searched for re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ecify certain GPUs for Tensor Parallelism and Pipeline Parallelism usage;stale ### Your current environment I have a server with only one NVLink connection, so I need to use pipeline parallelism and tensor parallelism w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
