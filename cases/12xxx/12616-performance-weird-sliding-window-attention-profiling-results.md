# vllm-project/vllm#12616: [Performance]: Weird Sliding Window Attention Profiling Results

| 字段 | 值 |
| --- | --- |
| Issue | [#12616](https://github.com/vllm-project/vllm/issues/12616) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Weird Sliding Window Attention Profiling Results

### Issue 正文摘录

### Proposal to improve performance Hi, I profiled the end2end latency of a Llama model with all attention layers set to **sliding window attention (SWA)**. I experimented with different input and output sequence lengths, expecting that for a fixed large output length (e.g., 8k), increasing the input sequence length would result in comparable overall latency. This expectation arises because decoding is the bottleneck at an 8k output length, and SWA ensures a constant decoding time under a fixed output length. I found that this assumption holds when batch_size=1. However, when I increase the batch size, latency increases significantly, as shown in the attached figure (batch_size=64). ![Image](https://github.com/user-attachments/assets/0ff159d1-4fd5-4bf1-b32a-9fe80759c647) I have attached my profiling script below. I'm not sure whether I missed anything in the profiling setup, or the support for SWA is still limited. ``` python3 benchmarks/benchmark_latency.py --model $my_llama_model_with_swa --load-format dummy --trust-remote-code \ --input-len 8192 \ --output-len 8192 \ --batch-size 64 \ --num-iters-warmup 3 \ --num-iters 5 \ --output-json ``` ### Report of performance regression...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Performance]: Weird Sliding Window Attention Profiling Results performance;stale ### Proposal to improve performance Hi, I profiled the end2end latency of a Llama model with all attention layers set to **sliding window...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: roposal to improve performance Hi, I profiled the end2end latency of a Llama model with all attention layers set to **sliding window attention (SWA)**. I experimented with different input and output sequence lengths, ex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rformance]: Weird Sliding Window Attention Profiling Results performance;stale ### Proposal to improve performance Hi, I profiled the end2end latency of a Llama model with all attention layers set to **sliding window at...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
