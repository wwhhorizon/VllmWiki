# vllm-project/vllm#1954: Why does the 8-GPUs experience a longer concurrent delay compared to the 2-GPUs?

| 字段 | 值 |
| --- | --- |
| Issue | [#1954](https://github.com/vllm-project/vllm/issues/1954) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why does the 8-GPUs experience a longer concurrent delay compared to the 2-GPUs?

### Issue 正文摘录

I conducted concurrent processing tests on an RTX 3090 and the results showed that it takes longer for the 8-GPUs to process the same concurrent requests than 2-GPUs, and the performance of 4 Gpus is similar to that of 2 Gpus. Reducing max-num-seqs on the 2-GPUs system can accelerate inference, but adjusting max-num-seqs and max-num-batched-tokens on the 8-GPU has little effect, and the speed is still slower than that of the 2-GPUs system. What could be the reason for this? Is it that the scheduling takes more time than the computation? Are there any methods that I can try?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 2-GPUs, and the performance of 4 Gpus is similar to that of 2 Gpus. Reducing max-num-seqs on the 2-GPUs system can accelerate inference, but adjusting max-num-seqs and max-num-batched-tokens on the 8-GPU has little effe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ay compared to the 2-GPUs? I conducted concurrent processing tests on an RTX 3090 and the results showed that it takes longer for the 8-GPUs to process the same concurrent requests than 2-GPUs, and the performance of 4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: howed that it takes longer for the 8-GPUs to process the same concurrent requests than 2-GPUs, and the performance of 4 Gpus is similar to that of 2 Gpus. Reducing max-num-seqs on the 2-GPUs system can accelerate infere...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ncurrent delay compared to the 2-GPUs? I conducted concurrent processing tests on an RTX 3090 and the results showed that it takes longer for the 8-GPUs to process the same concurrent requests than 2-GPUs, and the perfo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
