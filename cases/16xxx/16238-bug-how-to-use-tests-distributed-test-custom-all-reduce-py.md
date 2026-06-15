# vllm-project/vllm#16238: [Bug]: how to use tests/distributed/test_custom_all_reduce.py

| 字段 | 值 |
| --- | --- |
| Issue | [#16238](https://github.com/vllm-project/vllm/issues/16238) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: how to use tests/distributed/test_custom_all_reduce.py

### Issue 正文摘录

### Your current environment When I execute python3.10 -m tests.distributed.test_custom_all_reduce, no data is printed. Will it call the all_reduce function in the csrc/custom_all_reduce.cu file? ### 🐛 Describe the bug When I execute python3.10 -m tests.distributed.test_custom_all_reduce, no data is printed. Will it call the all_reduce function in the csrc/custom_all_reduce.cu file? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: how to use tests/distributed/test_custom_all_reduce.py bug;stale ### Your current environment When I execute python3.10 -m tests.distributed.test_custom_all_reduce, no data is printed. Will it call the all_reduce...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: how to use tests/distributed/test_custom_all_reduce.py bug;stale ### Your current environment When I execute python3.10 -m tests.distributed.test_custom_all_reduce, no data is printed. Will it call the all_reduce...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
