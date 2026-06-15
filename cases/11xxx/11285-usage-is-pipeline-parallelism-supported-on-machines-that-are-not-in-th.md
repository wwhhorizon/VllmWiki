# vllm-project/vllm#11285: [Usage]: Is pipeline parallelism supported on machines that are not in the same local network? 

| 字段 | 值 |
| --- | --- |
| Issue | [#11285](https://github.com/vllm-project/vllm/issues/11285) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is pipeline parallelism supported on machines that are not in the same local network? 

### Issue 正文摘录

### How would you like to use vllm Hi there, since the communications between nodes are done by NCCL(which typically relies on RDMA I guess), I wonder if I can setup an inference pipeline with machines from different networks, for example, one on Google Cloud and another on AWS Cloud, through vLLM's pipeline parallelism？ Thanks a lot if anyone can answer this. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Is pipeline parallelism supported on machines that are not in the same local network? usage;stale ### How would you like to use vllm Hi there, since the communications between nodes are done by NCCL(which typic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ism supported on machines that are not in the same local network? usage;stale ### How would you like to use vllm Hi there, since the communications between nodes are done by NCCL(which typically relies on RDMA I guess),...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
