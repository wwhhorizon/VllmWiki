# vllm-project/vllm#22161: [Performance]: TTFT

| 字段 | 值 |
| --- | --- |
| Issue | [#22161](https://github.com/vllm-project/vllm/issues/22161) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: TTFT

### Issue 正文摘录

### Proposal to improve performance ​Through my observations, I’ve found that the TTFT (Time To First Token) metric in large model inference can fluctuate due to network configuration and real-world network conditions, whereas TPOT (Time Per Output Token) is almost unaffected by the network. This means that the initial HTTP/HTTPS connection establishment process may introduce latency ranging from a few milliseconds to tens of milliseconds. My question is: Do inference serving frameworks like vLLM or SGLang support HTTP pre-connections (preconnect) or connection pooling features to reduce TTFT? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: due to network configuration and real-world network conditions, whereas TPOT (Time Per Output Token) is almost unaffected by the network. This means that the initial HTTP/HTTPS connection establishment process may intro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rvations, I’ve found that the TTFT (Time To First Token) metric in large model inference can fluctuate due to network configuration and real-world network conditions, whereas TPOT (Time Per Output Token) is almost unaff...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: TTFT performance;stale ### Proposal to improve performance ​Through my observations, I’ve found that the TTFT (Time To First Token) metric in large model inference can fluctuate due to network configurati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
