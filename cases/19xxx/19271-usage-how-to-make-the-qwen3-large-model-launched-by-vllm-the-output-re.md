# vllm-project/vllm#19271: [Usage]：How to make the Qwen3 large model launched by vllm, the output RequestOutput's metrics is not empty

| 字段 | 值 |
| --- | --- |
| Issue | [#19271](https://github.com/vllm-project/vllm/issues/19271) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]：How to make the Qwen3 large model launched by vllm, the output RequestOutput's metrics is not empty

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. i use 'vllm sever' run Qwen3 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. i use 'vllm sever' run Qwen3 ### Before submitting a new issue... - [x] Mak...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]：How to make the Qwen3 large model launched by vllm, the output RequestOutput's metrics is not empty usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: en3 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]：How to make the Qwen3 large model launched by vllm, the output RequestOutput's metrics is not empty usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
