# vllm-project/vllm#949: Why vLLM can't support CUDA 12?

| 字段 | 值 |
| --- | --- |
| Issue | [#949](https://github.com/vllm-project/vllm/issues/949) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why vLLM can't support CUDA 12?

### Issue 正文摘录

I see vLLM can't support CUDA 12 in [https://vllm.readthedocs.io/en/latest/getting_started/installation.html](url), but why it cannot in detail? Like the tensor parallelism or pipeline parallelism algorithm it uses can't support CUDA 12? Thanks for help.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Why vLLM can't support CUDA 12? I see vLLM can't support CUDA 12 in [https://vllm.readthedocs.io/en/latest/getting_started/installation.html](url), but why it cannot in detail? Like the tensor parallelism or pipeline pa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: upport CUDA 12 in [https://vllm.readthedocs.io/en/latest/getting_started/installation.html](url), but why it cannot in detail? Like the tensor parallelism or pipeline parallelism algorithm it uses can't support CUDA 12?...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 2? I see vLLM can't support CUDA 12 in [https://vllm.readthedocs.io/en/latest/getting_started/installation.html](url), but why it cannot in detail? Like the tensor parallelism or pipeline parallelism algorithm it uses c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
