# vllm-project/vllm#18383: [Usage]: vllm的不同版本

| 字段 | 值 |
| --- | --- |
| Issue | [#18383](https://github.com/vllm-project/vllm/issues/18383) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm的不同版本

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm 在使用vllm推理时，发现对于internvl2.5-8b模型，使用vllm0.7.3版本，测试并发时，可以正常请求；但是使用vllm0.8.5 版本，则总是过一会就请求不通超时，请问这是什么原因呀？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 因呀？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: collect_env.py` ``` ### How would you like to use vllm 在使用vllm推理时，发现对于internvl2.5-8b模型，使用vllm0.7.3版本，测试并发时，可以正常请求；但是使用vllm0.8.5 版本，则总是过一会就请求不通超时，请问这是什么原因呀？ ### Before submitting a new issue... - [x] Make sure you alread...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vllm的不同版本 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm 在使用vllm推理时，发现对于internvl2.5-8b模型，使用vllm0.7.3版本，测试并发时，可以正常请求；但是使用vllm0.8.5 版...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
