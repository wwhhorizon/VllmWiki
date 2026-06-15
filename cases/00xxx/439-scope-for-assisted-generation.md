# vllm-project/vllm#439: Scope for assisted generation?

| 字段 | 值 |
| --- | --- |
| Issue | [#439](https://github.com/vllm-project/vllm/issues/439) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Scope for assisted generation?

### Issue 正文摘录

It seems that assisted generation can further reduce sampling latency. Is there scope for adding support for that in vllm? Assisted generation [docs](https://huggingface.co/blog/assisted-generation)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: for adding support for that in vllm? Assisted generation [docs](https://huggingface.co/blog/assisted-generation)
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Scope for assisted generation? feature request It seems that assisted generation can further reduce sampling latency. Is there scope for adding support for that in vllm? Assisted generation [docs](https://huggingface.co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: re request It seems that assisted generation can further reduce sampling latency. Is there scope for adding support for that in vllm? Assisted generation [docs](https://huggingface.co/blog/assisted-generation)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
