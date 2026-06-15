# vllm-project/vllm#18702: [Usage]: can data_parallel_size or --data-parallel-size be used with v0 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#18702](https://github.com/vllm-project/vllm/issues/18702) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: can data_parallel_size or --data-parallel-size be used with v0 engine

### Issue 正文摘录

### Your current environment vLLM:v0.8.3 ### How would you like to use vllm i find the config param of data_parallel_size can be only used with v1 engine. i wonder if i can run muitl instances with v0 engine by using dp and these instances can be organized in the torch distributed group to support collective communications ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ons ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: environment vLLM:v0.8.3 ### How would you like to use vllm i find the config param of data_parallel_size can be only used with v1 engine. i wonder if i can run muitl instances with v0 engine by using dp and these instan...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
