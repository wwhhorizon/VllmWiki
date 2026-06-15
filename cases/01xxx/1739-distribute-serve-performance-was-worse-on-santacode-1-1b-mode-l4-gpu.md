# vllm-project/vllm#1739: distribute serve performance was worse on santacode 1.1B mode, L4 GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#1739](https://github.com/vllm-project/vllm/issues/1739) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> distribute serve performance was worse on santacode 1.1B mode, L4 GPU

### Issue 正文摘录

Hi **GPU**: Google Cloud L4 GPU, 24GB memory **model**: SantaCoder, https://huggingface.co/bigcode/gpt_bigcode-santacoder **Issue**: I tried to serve Santacoder model on L4 GPU, found that distributed serve performance is worse. We can see from below result that 2 L4 GPU was worse than 1 L4 GPU, 4 L4 GPU was worse than 2 L4 GPU. I tried another 1.1B model(TinyLlama-1.1B-Chat-v0.3), the result was actually same. I also tried TensorRT LLM, it does not have this problem and the performance is better in distributed serve. benchmark_serving.py result: 1 L4 GPU Total time: 98.36 s Throughput: 10.17 requests/s Average latency: 47.96 s Average latency per token: 0.15 s Average latency per output token: 0.80 s 2 L4 GPU Total time: 148.03 s Throughput: 6.76 requests/s Average latency: 62.97 s Average latency per token: 0.21 s Average latency per output token: 1.04 s 4 L4 GPU Total time: 157.14 s Throughput: 6.36 requests/s Average latency: 71.33 s Average latency per token: 0.24 s Average latency per output token: 1.28 s

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tacode 1.1B mode, L4 GPU Hi **GPU**: Google Cloud L4 GPU, 24GB memory **model**: SantaCoder, https://huggingface.co/bigcode/gpt_bigcode-santacoder **Issue**: I tried to serve Santacoder model on L4 GPU, found that distr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: t have this problem and the performance is better in distributed serve. benchmark_serving.py result: 1 L4 GPU Total time: 98.36 s Throughput: 10.17 requests/s Average latency: 47.96 s Average latency per token: 0.15 s A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: chmark_serving.py result: 1 L4 GPU Total time: 98.36 s Throughput: 10.17 requests/s Average latency: 47.96 s Average latency per token: 0.15 s Average latency per output token: 0.80 s 2 L4 GPU Total time: 148.03 s Throu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
