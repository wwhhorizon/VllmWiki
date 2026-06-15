# vllm-project/vllm#20551: [Usage]: Want profiler for PD disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#20551](https://github.com/vllm-project/vllm/issues/20551) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Want profiler for PD disaggregation

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I found that `benchmark_serving.py` does not support `--profile` for PD disaggregation. Currently in `benchmark_serving.py`, the profiler can only access the proxy port, but sending a `/start_profile` request to the proxy port only results in `404 Not Found`. Is there a way to implement profile for PD disaggregation in the current version of vllm? Or will the relevant functions be updated in subsequent versions? I am looking forward to it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Usage]: Want profiler for PD disaggregation usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I found that `benchmark_serving.py` does not support `...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Is there a way to implement profile for PD disaggregation in the current version of vllm? Or will the relevant functions be updated in subsequent versions? I am looking forward to it. ### Before submitting a new issue.....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: profiler can only access the proxy port, but sending a `/start_profile` request to the proxy port only results in `404 Not Found`. Is there a way to implement profile for PD disaggregation in the current version of vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
