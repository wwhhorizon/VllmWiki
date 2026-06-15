# vllm-project/vllm#20298: [RFC][PP]: Integrate Token Throttling into vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#20298](https://github.com/vllm-project/vllm/issues/20298) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][PP]: Integrate Token Throttling into vLLM

### Issue 正文摘录

## Motivation. [Token Throttling](https://arxiv.org/abs/2504.14775) is a novel scheduling policy targarted for **pipeline parallelism** and dense models. It has been integrated into [gLLM](https://github.com/gty111/gLLM). It can provide great acceleration compared to baseline scheduling policy. Token Throttling has been accepeted by [SC'25](https://sc25.conference-program.com/presentation/?id=pap444&sess=sess168). ## Reference paper/arXiv: https://arxiv.org/abs/2504.14775 Code: https://github.com/gty111/gLLM SC'25 program: https://sc25.conference-program.com/presentation/?id=pap444&sess=sess168 ## Performance Comparison - Test on 4 x 4090 GPUs and Qwen2.5-32B, 2048 reqs, 16reqs/s ``` vLLM v0.9.1 ============ Serving Benchmark Result ============ Successful requests: 2048 Benchmark duration (s): 311.16 Total input tokens: 461482 Total generated tokens: 321782 Request throughput (req/s): 6.58 Output token throughput (tok/s): 1034.15 Total Token throughput (tok/s): 2517.28 ---------------Time to First Token---------------- Mean TTFT (ms): 55010.10 Median TTFT (ms): 54147.04 P99 TTFT (ms): 127917.08 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 233.04 Median TPOT...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: m.com/presentation/?id=pap444&sess=sess168 ## Performance Comparison - Test on 4 x 4090 GPUs and Qwen2.5-32B, 2048 reqs, 16reqs/s ``` vLLM v0.9.1 ============ Serving Benchmark Result ============ Successful requests: 2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 04.14775) is a novel scheduling policy targarted for **pipeline parallelism** and dense models. It has been integrated into [gLLM](https://github.com/gty111/gLLM). It can provide great acceleration compared to baseline...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: novel scheduling policy targarted for **pipeline parallelism** and dense models. It has been integrated into [gLLM](https://github.com/gty111/gLLM). It can provide great acceleration compared to baseline scheduling poli...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC][PP]: Integrate Token Throttling into vLLM RFC;stale ## Motivation. [Token Throttling](https://arxiv.org/abs/2504.14775) is a novel scheduling policy targarted for **pipeline parallelism** and dense models. It has...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
