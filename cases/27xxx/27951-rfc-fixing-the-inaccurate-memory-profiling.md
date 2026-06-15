# vllm-project/vllm#27951: [RFC]: Fixing the inaccurate memory profiling

| 字段 | 值 |
| --- | --- |
| Issue | [#27951](https://github.com/vllm-project/vllm/issues/27951) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;model_support;moe |
| 子分类 | memory |
| Operator 关键词 | cuda;moe |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Fixing the inaccurate memory profiling

### Issue 正文摘录

### Motivation. vLLM’s Memory profiling is becoming more and more inaccurate to a point that we probably need to rethink whether this is still needed / is the correct interface. - We originally wrote this logic two years ago when the models were all dense models without CUDA graphs. And back then, the memory profiling is pretty accurate and can reflect the actual activation usage. - Now, we are dealing with models with imbalanced MoE layers and CUDA graphs. Imbalanced MoE layers means a popular expert can directly cause OOM. And CUDA graphs require a pretty significant pool of reserved memory. - In practice, because of the two factors above, people adjust gpu memory utilization to make the model not OOM. However, the original meaning of GPU memory utilization is like the following: Say we set the utilization to 70%. vLLM’s memory usage should never exceed 70% of the total GPU memory. But now, we set the utilization to 70% to use the other 30% for uncaptured CUDA Graph/Activation memory. This is a confusing and wrong interface. ### Proposed Change. I don't have a direct good fix in my mind yet. But will keep the RFC open here and see whether I or anybody else have more thoughts to...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e this logic two years ago when the models were all dense models without CUDA graphs. And back then, the memory profiling is pretty accurate and can reflect the actual activation usage. - Now, we are dealing with models...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: graphs. Imbalanced MoE layers means a popular expert can directly cause OOM. And CUDA graphs require a pretty significant pool of reserved memory. - In practice, because of the two factors above, people adjust gpu memor...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: tual activation usage. - Now, we are dealing with models with imbalanced MoE layers and CUDA graphs. Imbalanced MoE layers means a popular expert can directly cause OOM. And CUDA graphs require a pretty significant pool...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [RFC]: Fixing the inaccurate memory profiling RFC;stale ### Motivation. vLLM’s Memory profiling is becoming more and more inaccurate to a point that we probably need to rethink whether this is still needed / is the corr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: mind yet. But will keep the RFC open here and see whether I or anybody else have more thoughts to this problem. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Befor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
