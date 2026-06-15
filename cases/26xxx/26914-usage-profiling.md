# vllm-project/vllm#26914: [Usage]: 为什么在采集的profiling中看不到通信算子？

| 字段 | 值 |
| --- | --- |
| Issue | [#26914](https://github.com/vllm-project/vllm/issues/26914) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 为什么在采集的profiling中看不到通信算子？

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` 通过llm.start_profile和stop_profile，我采集到了profiling，但kernel_details里面看不到通信算子。 ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Usage]: 为什么在采集的profiling中看不到通信算子？ usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` 通过llm.start_profile和stop_profile，我采集到了profiling，但kernel_details里面看不到通信算子。 ### How would you l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 子。 ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: 为什么在采集的profiling中看不到通信算子？ usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` 通过llm.start_profile和stop_profile，我采集到了profiling，但kernel_details里面看不到通信算子。 ### How would you l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
