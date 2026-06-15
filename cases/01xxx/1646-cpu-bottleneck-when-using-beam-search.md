# vllm-project/vllm#1646: CPU Bottleneck when using beam search

| 字段 | 值 |
| --- | --- |
| Issue | [#1646](https://github.com/vllm-project/vllm/issues/1646) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> CPU Bottleneck when using beam search

### Issue 正文摘录

I'm finding a surprising bottleneck in beam search generation in vllm 0.2.1.post1. I have one CPU process pegged at 100% CPU, and GPU utilization below 25%. When I use py-spy to inspect where the time is getting spent I see vllm/sequence.py:fork is calling deepcopy(), and that over 80% of my CPU time is getting spent there. So deepcopy() is clearly the bottleneck for this use case. FWIW this is with llama2-7b on an A100-80. I'm not yet sure whether this is a regression or if there has always been this bottleneck in vLLM. Here's a simple example which reproduces the issue: https://gist.github.com/physicsrob/f7bc0be046c01cd6f959966e24022bba

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: CPU Bottleneck when using beam search I'm finding a surprising bottleneck in beam search generation in vllm 0.2.1.post1. I have one CPU process pegged at 100% CPU, and GPU utilization below 25%. When I use py-spy to ins...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: has always been this bottleneck in vLLM. Here's a simple example which reproduces the issue: https://gist.github.com/physicsrob/f7bc0be046c01cd6f959966e24022bba
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: epcopy() is clearly the bottleneck for this use case. FWIW this is with llama2-7b on an A100-80. I'm not yet sure whether this is a regression or if there has always been this bottleneck in vLLM. Here's a simple example...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: this is with llama2-7b on an A100-80. I'm not yet sure whether this is a regression or if there has always been this bottleneck in vLLM. Here's a simple example which reproduces the issue: https://gist.github.com/physic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
