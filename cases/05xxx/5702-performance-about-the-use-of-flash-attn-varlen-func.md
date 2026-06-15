# vllm-project/vllm#5702: [Performance]: About the use of flash_attn_varlen_func()

| 字段 | 值 |
| --- | --- |
| Issue | [#5702](https://github.com/vllm-project/vllm/issues/5702) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: About the use of flash_attn_varlen_func()

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hi, vllm developers, I read the code and found the use of flash attention. This algorithm used in vllm likely for the sake of conducting the pre-filling stage more quickly. Am i right in thinking so? BTW, the vllm code used flash_attn_varlen_func(), instead of other implementations of FA, e.g., lash_attn_func, flash_attn_kvpacked_func, flash_attn_qkvpacked_func, flash_attn_varlen_kvpacked_func, flash_attn_varlen_qkvpacked_func, and flash_attn_with_kvcache. Could you share with me the consideration made for this selection? Is it selected for its speed better than other implementations as well? Is there a remarked difference between it and other implementations in the situation of vllm? Thanks. ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ```

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: performance Hi, vllm developers, I read the code and found the use of flash attention. This algorithm used in vllm likely for the sake of conducting the pre-filling stage more quickly. Am i right in thinking so? BTW, th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: About the use of flash_attn_varlen_func() performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hi, vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hi, vllm developers, I read the code and found the use of flash attention. This algorith...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
