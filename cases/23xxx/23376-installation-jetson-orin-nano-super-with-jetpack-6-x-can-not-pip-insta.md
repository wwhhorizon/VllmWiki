# vllm-project/vllm#23376: [Installation]: Jetson Orin Nano Super with Jetpack 6.x can not pip install vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#23376](https://github.com/vllm-project/vllm/issues/23376) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Jetson Orin Nano Super with Jetpack 6.x can not pip install vllm

### Issue 正文摘录

### Your current environment ```text I can't even pip install vllm so I don't have the package ``` Basically title, I can not pip install vllm as it just crashes my whole Jetson Orin Nano before completing. The installation stalls at the building wheels part and I don't know how I can port this library over to build as a smaller version on the Jetson Orin Nano ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Jetson Orin Nano Super with Jetpack 6.x can not pip install vllm installation;stale ### Your current environment ```text I can't even pip install vllm so I don't have the package ``` Basically title, I c
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: els part and I don't know how I can port this library over to build as a smaller version on the Jetson Orin Nano ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x]...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n Orin Nano Super with Jetpack 6.x can not pip install vllm installation;stale ### Your current environment ```text I can't even pip install vllm so I don't have the package ``` Basically title, I can not pip install vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
