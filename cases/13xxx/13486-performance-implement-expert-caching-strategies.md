# vllm-project/vllm#13486: [Performance]: Implement expert caching strategies

| 字段 | 值 |
| --- | --- |
| Issue | [#13486](https://github.com/vllm-project/vllm/issues/13486) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Implement expert caching strategies

### Issue 正文摘录

### Proposal to improve performance There have been successful efforts in being able to offload weights to system memory for later retrieval ([vLLM PR #6496](https://github.com/vllm-project/vllm/pull/6496)), but there has been some recent development in JIT fetching/Speculative caching that justify a more complex approach to this for MoE models. This has particular application in systems like the GH200 where a chip-to-chip interface removes the PCIe bottleneck, as well as in very large models like DeepSeek's 671B class of MoE models, as expert fetching per layer seems to be entirely hideable using the [ProMOE](https://arxiv.org/pdf/2410.22134v2) approach. I've started some of this implementation work against a GH200 system with @drikster80's help, but now with robust research showing the performance benefits, I wanted to bring it up in this forum as I'm hitting a bit of a wall in getting this working with FusedMOE's behavior and underlying kernel. --- ### Back-of-the-Napkin Math Using GH200 Bus Factors and DeepSeekV3 class of MoE models For each token, the number of expert invocations is calculated as follows: $$ \text{Total Experts} = 8 \, (\text{experts per layer}) \times 58 \,...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: efforts in being able to offload weights to system memory for later retrieval ([vLLM PR #6496](https://github.com/vllm-project/vllm/pull/6496)), but there has been some recent development in JIT fetching/Speculative cac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: els. This has particular application in systems like the GH200 where a chip-to-chip interface removes the PCIe bottleneck, as well as in very large models like DeepSeek's 671B class of MoE models, as expert fetching per...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Performance]: Implement expert caching strategies performance;stale ### Proposal to improve performance There have been successful efforts in being able to offload weights to system memory for later retrieval ([vLLM PR...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Implement expert caching strategies performance;stale ### Proposal to improve performance There have been successful efforts in being able to offload weights to system memory for later retrieval ([vLLM PR...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t{experts per layer}) \times 58 \, (\text{layers}) = 464. $$ Assuming a cache hit ratio of 20%, the number of experts already in cache is: $$ \text{Cached Experts} = 0.2 \times 464 \approx 93. $$ Thus, the number of exp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
