# vllm-project/vllm#1451: Benchmarking vs TGI

| 字段 | 值 |
| --- | --- |
| Issue | [#1451](https://github.com/vllm-project/vllm/issues/1451) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Benchmarking vs TGI

### Issue 正文摘录

I've been comparing the performance of TGI and vLLM recently; using `Mistral`, on my setup it seems like TGI now massively outperforms vLLM in this case. I'm running on a g5.xlarge (1x NVIDIA A10G), both vLLM and TGI in respective docker containers. Is this performance difference expected? I also noticed the TGI launch script in the benchmarks uses v0.8, this should probably be updated to the newest version (or the newest pre-license change version, at least).

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: running on a g5.xlarge (1x NVIDIA A10G), both vLLM and TGI in respective docker containers. Is this performance difference expected? I also noticed the TGI launch script in the benchmarks uses v0.8, this should probably...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Benchmarking vs TGI I've been comparing the performance of TGI and vLLM recently; using `Mistral`, on my setup it seems like TGI now massively outperforms vLLM in this case. I'm running on a g5.xlarge (1x NVIDIA A10G),

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
