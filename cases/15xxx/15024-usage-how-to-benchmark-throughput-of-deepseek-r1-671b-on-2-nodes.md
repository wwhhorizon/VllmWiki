# vllm-project/vllm#15024: [Usage]: How to benchmark throughput of DeepSeek-R1-671B on 2 nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#15024](https://github.com/vllm-project/vllm/issues/15024) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to benchmark throughput of DeepSeek-R1-671B on 2 nodes

### Issue 正文摘录

### Your current environment Hi, I want to use the benchmark_throughput.py to evaluate the offline performance of DeepSeek-R1-671B, and I **use more than one server (more than 16 GPUs)** to deploy the DeepSeek-R1-671B. **The question is how do I set the command line parameters of benchmark_throughput.py to evaluate the offline performance of DS on multiple nodes and GPUs ?** ### How would you like to use vllm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Usage]: How to benchmark throughput of DeepSeek-R1-671B on 2 nodes usage;stale ### Your current environment Hi, I want to use the benchmark_throughput.py to evaluate the offline performance of DeepSeek-R1-671B, and I *...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Usage]: How to benchmark throughput of DeepSeek-R1-671B on 2 nodes usage;stale ### Your current environment Hi, I want to use the benchmark_throughput.py to evaluate the offline performance of DeepSeek-R1-671B, and I **...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
