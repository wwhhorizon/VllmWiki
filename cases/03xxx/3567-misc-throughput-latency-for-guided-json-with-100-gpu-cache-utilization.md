# vllm-project/vllm#3567: [Misc]: Throughput/Latency for guided_json with ~100% GPU cache utilization

| 字段 | 值 |
| --- | --- |
| Issue | [#3567](https://github.com/vllm-project/vllm/issues/3567) |
| 状态 | closed |
| 标签 | structured-output;stale |
| 评论 | 67; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Throughput/Latency for guided_json with ~100% GPU cache utilization

### Issue 正文摘录

### Anything you want to discuss about vllm. Hi, I am running some benchmarks on the `vllm.entrypoints.openai.api_server` measuring latency and throughput with different number of concurrent requests. Specs: - H100 80GB - qwen-1.5-14B-chat I am sending 1000 requests with random prompts of token length 512. These are the results I get (see attached image): **Guided_json** - ~100 running requests - ~70 generation tokens per second - ~1700 ms median token time **Non-guided_json** - ~100 running requests - ~800 generation tokens per second - ~75 ms median token time (TPOT) At 10 concurrent request (GPU utlization )

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Misc]: Throughput/Latency for guided_json with ~100% GPU cache utilization structured-output;stale ### Anything you want to discuss about vllm. Hi, I am running some benchmarks on the `vllm.entrypoints.openai.api_serve...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tency for guided_json with ~100% GPU cache utilization structured-output;stale ### Anything you want to discuss about vllm. Hi, I am running some benchmarks on the `vllm.entrypoints.openai.api_server` measuring latency...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: y and throughput with different number of concurrent requests. Specs: - H100 80GB - qwen-1.5-14B-chat I am sending 1000 requests with random prompts of token length 512. These are the results I get (see attached image):...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hput with different number of concurrent requests. Specs: - H100 80GB - qwen-1.5-14B-chat I am sending 1000 requests with random prompts of token length 512. These are the results I get (see attached image): **Guided_js...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
