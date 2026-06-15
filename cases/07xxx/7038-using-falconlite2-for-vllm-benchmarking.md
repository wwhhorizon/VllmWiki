# vllm-project/vllm#7038: using Falconlite2 for vllm benchmarking

| 字段 | 值 |
| --- | --- |
| Issue | [#7038](https://github.com/vllm-project/vllm/issues/7038) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> using Falconlite2 for vllm benchmarking

### Issue 正文摘录

### The model to consider. the model that I am thinking is Falconlite2:https://huggingface.co/amazon/FalconLite2 I am not sure how to use vllm and falconlite2 together for benchmarking purposes ### The closest model vllm already supports. falcon7 ### What's your difficulty of supporting the model you want? I want to use falconlite2 and vllm for benchmarking and get some latency and throughput results. However, falconlite2 is not supported by vllm

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: using Falconlite2 for vllm benchmarking new-model;stale ### The model to consider. the model that I am thinking is Falconlite2:https://huggingface.co/amazon/FalconLite2 I am not sure how to use vllm and falconlite2 toge...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: using Falconlite2 for vllm benchmarking new-model;stale ### The model to consider. the model that I am thinking is Falconlite2:https://huggingface.co/amazon/FalconLite2 I am not sure how to use vllm and falconlite2 toge...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: using Falconlite2 for vllm benchmarking new-model;stale ### The model to consider. the model that I am thinking is Falconlite2:https://huggingface.co/amazon/FalconLite2 I am not sure how to use vllm and falconlite2 toge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
