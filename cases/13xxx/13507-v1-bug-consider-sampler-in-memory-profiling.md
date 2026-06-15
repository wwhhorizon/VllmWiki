# vllm-project/vllm#13507: [V1][Bug]: Consider sampler in memory profiling

| 字段 | 值 |
| --- | --- |
| Issue | [#13507](https://github.com/vllm-project/vllm/issues/13507) |
| 状态 | closed |
| 标签 | bug;help wanted |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [V1][Bug]: Consider sampler in memory profiling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Currently, V1 model runner does not consider (or run) sampler during the initial memory profiling. This should be fixed 1) for more accurate memory profiling and 2) to warm up the sampler before processing any real requests. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [V1][Bug]: Consider sampler in memory profiling bug;help wanted ### Your current environment ### 🐛 Describe the bug Currently, V1 model runner does not consider (or run) sampler during the initial memory profiling. This...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d ### Your current environment ### 🐛 Describe the bug Currently, V1 model runner does not consider (or run) sampler during the initial memory profiling. This should be fixed 1) for more accurate memory profiling and 2)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: emory profiling and 2) to warm up the sampler before processing any real requests. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the botto...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
