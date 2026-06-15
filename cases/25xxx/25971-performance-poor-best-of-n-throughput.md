# vllm-project/vllm#25971: [Performance]: poor "best of N" throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#25971](https://github.com/vllm-project/vllm/issues/25971) |
| 状态 | closed |
| 标签 | performance;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: poor "best of N" throughput

### Issue 正文摘录

### Proposal to improve performance We see vLLM do well on best of 1, we see that it degrades very poorly with "best of N". The above plot contains a lot of confusing details but the key thing is this: H100 -> bo1 has 6.64 r/s throughput whereas bo8 has 0.83 (reduced by a factor of 8) Mi300X -> bo1 has 20.8 r/s throughput whereas bo8 has 2.69 (reduced by a factor of 7.7) On alternative frameworks we see more like a 2x reduction from bo1 to bo8. It appears to me that either best of N is not optimised for vLLM or there is some issue in the way I am using vLLM. And since "best of N" is pretty standard now I think its an important issue to optimise. Any help or discussion is appreciated.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Performance]: poor "best of N" throughput performance;rocm ### Proposal to improve performance We see vLLM do well on best of 1, we see that it degrades very poorly with "best of N". The above plot contains a lot of co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: using vLLM. And since "best of N" is pretty standard now I think its an important issue to optimise. Any help or discussion is appreciated.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Performance]: poor "best of N" throughput performance;rocm ### Proposal to improve performance We see vLLM do well on best of 1, we see that it degrades very poorly with "best of N". The above plot contains a lot of co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
