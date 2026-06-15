# vllm-project/vllm#9009: [Usage]: Default input and output sequence length for ShareGPT dataset

| 字段 | 值 |
| --- | --- |
| Issue | [#9009](https://github.com/vllm-project/vllm/issues/9009) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Default input and output sequence length for ShareGPT dataset

### Issue 正文摘录

### Your current environment benchmark_serving.py specify input-len and output-len for sonnet and random datasets but this value is not provided for shareGPT. Does anybody knows what is the default value for this dataset? ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ce length for ShareGPT dataset usage;stale ### Your current environment benchmark_serving.py specify input-len and output-len for sonnet and random datasets but this value is not provided for shareGPT. Does anybody know...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ataset usage;stale ### Your current environment benchmark_serving.py specify input-len and output-len for sonnet and random datasets but this value is not provided for shareGPT. Does anybody knows what is the default va...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ge]: Default input and output sequence length for ShareGPT dataset usage;stale ### Your current environment benchmark_serving.py specify input-len and output-len for sonnet and random datasets but this value is not prov...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
