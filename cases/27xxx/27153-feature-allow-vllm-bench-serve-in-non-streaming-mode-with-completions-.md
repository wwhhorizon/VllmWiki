# vllm-project/vllm#27153: [Feature]: Allow vllm bench serve in non-streaming mode with /completions API

| 字段 | 值 |
| --- | --- |
| Issue | [#27153](https://github.com/vllm-project/vllm/issues/27153) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow vllm bench serve in non-streaming mode with /completions API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM’s bench serve currently supports recording benchmark results only in the streaming mode - recording metrics like TTFT, TPOT, ITL etc. For my use case benchmarking [llm-d ](https://github.com/llm-d/llm-d)which uses vLLM, I would like to enable vllm bench serve in non-streaming mode for the openai backend, recording only non-streaming latency metrics like E2E Latency. Overall, the changes required would be as follows: * Add a new Async Request Function - `async_request_openai_completions_non_streaming()` function in [`vllm/vllm/benchmarks/lib/endpoint_request_func.py`](https://github.com/vllm-project/vllm/blob/main/vllm/benchmarks/lib/endpoint_request_func.py) to support parsing of non-streaming vllm outputs. * Add a new benchmark argument: `benchmark_streaming`. If `benchmark_streaming` is set to False for the `openai` backend, then the above function `async_request_openai_completions_non_streaming()` is called instead of `async_request_openai_completions`. * Either modify [`vllm/benchmarks/serve.py`](https://github.com/vllm-project/vllm/blob/main/vllm/benchmarks/serve.py) or design a new benchmark script to calculate and save metrics, e...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: e, motivation and pitch vLLM’s bench serve currently supports recording benchmark results only in the streaming mode - recording metrics like TTFT, TPOT, ITL etc. For my use case benchmarking [llm-d ](https://github.com...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: low vllm bench serve in non-streaming mode with /completions API feature request;stale ### 🚀 The feature, motivation and pitch vLLM’s bench serve currently supports recording benchmark results only in the streaming mode...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uld like to enable vllm bench serve in non-streaming mode for the openai backend, recording only non-streaming latency metrics like E2E Latency. Overall, the changes required would be as follows: * Add a new Async Reque...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rk argument: `benchmark_streaming`. If `benchmark_streaming` is set to False for the `openai` backend, then the above function `async_request_openai_completions_non_streaming()` is called instead of `async_request_opena...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
