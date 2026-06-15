# vllm-project/vllm#1435: How does `tensor_parallel_size` increase throughput?

| 字段 | 值 |
| --- | --- |
| Issue | [#1435](https://github.com/vllm-project/vllm/issues/1435) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How does `tensor_parallel_size` increase throughput?

### Issue 正文摘录

Using 8 A100s (80GB), I find that setting this to 1 or 8 doesn't change performance much, even when using large batches (1000+). Is there a bottleneck somewhere that I am not aware of? The current workaround I'm using is to run 8 different processes with a single GPU each, as you would with `accelerate`, but it's a pretty ugly solution. More context: This is using the `LLM` class, and StarCoderBase (tried other models too).

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: How does `tensor_parallel_size` increase throughput? Using 8 A100s (80GB), I find that setting this to 1 or 8 doesn't change performance much, even when using large batches (1000+). Is there a bottleneck somewhere that...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e context: This is using the `LLM` class, and StarCoderBase (tried other models too).
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: How does `tensor_parallel_size` increase throughput? Using 8 A100s (80GB), I find that setting this to 1 or 8 doesn't change performance much, even when using large batches (1000+). Is there a bottleneck somewhere that...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
