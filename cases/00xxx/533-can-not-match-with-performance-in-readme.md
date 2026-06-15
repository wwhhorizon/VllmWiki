# vllm-project/vllm#533: can not match with performance in readme

| 字段 | 值 |
| --- | --- |
| Issue | [#533](https://github.com/vllm-project/vllm/issues/533) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> can not match with performance in readme

### Issue 正文摘录

I test a 13b model on a A100-80G with `benchmark_throughput.py`. The hf result is 0.2 requests/s, 85.25 tokens/s. The vllm result is 4.94 requests/s, 2153.77 tokens/s. The acceleration effect is obvious, but the gap with the readme(154.2 requests/s) is huge. Is this result correct? Or am I doing something wrong? Besides, the vllm use `_add_request` to load all input and use `_run_engine` to do the inference. A bit strange why not use `generate` directly? If there is a lot of data, we can not use `_add_request` to load whole data at once.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: can not match with performance in readme I test a 13b model on a A100-80G with `benchmark_throughput.py`. The hf result is 0.2 requests/s, 85.25 tokens/s. The vllm result is 4.94 requests/s, 2153.77 tokens/s. The accele...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: can not match with performance in readme I test a 13b model on a A100-80G with `benchmark_throughput.py`. The hf result is 0.2 requests/s, 85.25 tokens/s. The vllm result is 4.94 requests/s, 2153.77 tokens/s. The accele...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: can not match with performance in readme I test a 13b model on a A100-80G with `benchmark_throughput.py`. The hf result is 0.2 requests/s, 85.25 tokens/s. The vllm result is 4.94 requests/s, 2153.77 tokens/s. The accele...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: model on a A100-80G with `benchmark_throughput.py`. The hf result is 0.2 requests/s, 85.25 tokens/s. The vllm result is 4.94 requests/s, 2153.77 tokens/s. The acceleration effect is obvious, but the gap with the readme(...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
