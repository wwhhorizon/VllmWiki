# vllm-project/vllm#7635: [Misc]: TTFT profiling with respect to prompt length

| 字段 | 值 |
| --- | --- |
| Issue | [#7635](https://github.com/vllm-project/vllm/issues/7635) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: TTFT profiling with respect to prompt length

### Issue 正文摘录

### Anything you want to discuss about vllm. I am profiling TTFT and TPOT on my machine, I could not explain the behavior of TTFT thus opened this issue to seek for advice. Below figure shows the TTFTs with respect to prompt length on my machine, the test condition is as below: - model: llama3-8B - GPU type: V100, the below figure shows the result of TP=2 - dataset: ShareGPT steps taken for TTFT and TPOT profiling: 1. start the OpenAI API-compatible server using: `python -m vllm.entrypoints.openai.api_server --args` 2. iterative running `benchmark_serving.py` to get the TTFT and TPOT, each time only send a request to server to eliminate the effect of waiting time The profiled TTFT is as below: Observation 1: when the prompt length is less than 400, the TTFT seems to be a flat value ~100ms. This value is consistent across different TP settings (tried TP=1, TP=2 and TP=4). Observation 2: When prompt length is greater than 400, TTFT is linear to prompt length. This result is inline with Figure 6b this paper (https://arxiv.org/pdf/2405.06856). I don't understand the result of observation 1, can anyone provide some insight on this result? What is the reason causingTTFT a horizontal lin...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Misc]: TTFT profiling with respect to prompt length stale ### Anything you want to discuss about vllm. I am profiling TTFT and TPOT on my machine, I could not explain the behavior of TTFT thus opened this issue to seek...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Misc]: TTFT profiling with respect to prompt length stale ### Anything you want to discuss about vllm. I am profiling TTFT and TPOT on my machine, I could not explain the behavior of TTFT thus opened this issue to seek...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: espect to prompt length on my machine, the test condition is as below: - model: llama3-8B - GPU type: V100, the below figure shows the result of TP=2 - dataset: ShareGPT steps taken for TTFT and TPOT profiling: 1. start...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
