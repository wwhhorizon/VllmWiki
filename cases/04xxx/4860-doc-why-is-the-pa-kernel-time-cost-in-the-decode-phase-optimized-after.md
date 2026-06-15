# vllm-project/vllm#4860: [Doc]: Why is the PA kernel time cost in the decode phase optimized after turning on Prefix Caching?

| 字段 | 值 |
| --- | --- |
| Issue | [#4860](https://github.com/vllm-project/vllm/issues/4860) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Why is the PA kernel time cost in the decode phase optimized after turning on Prefix Caching?

### Issue 正文摘录

### 📚 The doc issue It is understandable that the prefill phase takes less time because the number of tokens corresponding to the query is reduced. But for the decode phase, I used nsys to check the kernel time consumption. Why did the PA time consumption in the decode phase decrease? Other kernels such as RMSNorm/gemm did not decrease. I see that the corresponding shapes are aligned, indicating that the amount of calculation is the same. Is it because the memory access is optimized after turning on Prefix Caching? I don’t really understand. Although I learned through [related issues](https://github.com/vllm-project/vllm/issues/4104) that the specific implementation will also cache the kv cache of generate, but this is only on the scheduler. Why does it affect the kernel level? Thanks ~ ### Suggest a potential alternative/fix _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Doc]: Why is the PA kernel time cost in the decode phase optimized after turning on Prefix Caching? documentation ### 📚 The doc issue It is understandable that the prefill phase takes less time because the number of to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ed issues](https://github.com/vllm-project/vllm/issues/4104) that the specific implementation will also cache the kv cache of generate, but this is only on the scheduler. Why does it affect the kernel level? Thanks ~ ##...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t/vllm/issues/4104) that the specific implementation will also cache the kv cache of generate, but this is only on the scheduler. Why does it affect the kernel level? Thanks ~ ### Suggest a potential alternative/fix _No...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: consumption in the decode phase decrease? Other kernels such as RMSNorm/gemm did not decrease. I see that the corresponding shapes are aligned, indicating that the amount of calculation is the same. Is it because the me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
