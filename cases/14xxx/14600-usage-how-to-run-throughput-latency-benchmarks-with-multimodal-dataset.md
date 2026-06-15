# vllm-project/vllm#14600: [Usage]: How to run throughput/latency benchmarks with multimodal datasets offline

| 字段 | 值 |
| --- | --- |
| Issue | [#14600](https://github.com/vllm-project/vllm/issues/14600) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to run throughput/latency benchmarks with multimodal datasets offline

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` I want to run benchmarks locally to testing the performance of multimodal models, and notice that we have consolidate datasets on [#14036](https://github.com/vllm-project/vllm/pull/14036), only found mutlimodal dataset support with benchmark_serving, i wonder if there any way to get the throughput and latency result offline with multimodal input. ### How would you like to use vllm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Usage]: How to run throughput/latency benchmarks with multimodal datasets offline usage ### Your current environment ```text The output of `python collect_env.py` ``` I want to run benchmarks locally to testing the per...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to run throughput/latency benchmarks with multimodal datasets offline usage ### Your current environment ```text The output of `python collect_env.py` ``` I want to run benchmarks locally to testing the per...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
