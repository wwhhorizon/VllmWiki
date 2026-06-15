# vllm-project/vllm#11874: [Performance]: Distributed Inference and Serving

| 字段 | 值 |
| --- | --- |
| Issue | [#11874](https://github.com/vllm-project/vllm/issues/11874) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Distributed Inference and Serving

### Issue 正文摘录

### Proposal to improve performance I have two nodes and two GPUs for each node, using vllm for Qwen-32B tensor parallel plus pipeline parallel inference，When I observed the monitoring, I found that the maximum bandwidth of the network was only 25Mbps，my machine has 1000Mbps of bandwidth，I doubt why only uses a little bandwidth in vllm distributed inference and distributed inference bottleneck is not bandwidth ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ributed inference bottleneck is not bandwidth ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: erformance I have two nodes and two GPUs for each node, using vllm for Qwen-32B tensor parallel plus pipeline parallel inference，When I observed the monitoring, I found that the maximum bandwidth of the network was only...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Distributed Inference and Serving performance;stale ### Proposal to improve performance I have two nodes and two GPUs for each node, using vllm for Qwen-32B tensor parallel plus pipeline parallel inferenc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
