# vllm-project/vllm#5314: [Performance]: Is kv cache implemented globally in vllm， It can be shared by multiple concurrent inferences?

| 字段 | 值 |
| --- | --- |
| Issue | [#5314](https://github.com/vllm-project/vllm/issues/5314) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Is kv cache implemented globally in vllm， It can be shared by multiple concurrent inferences?

### Issue 正文摘录

### Proposal to improve performance Is kv cache implemented globally in vllm， It can be shared by multiple concurrent inferences? if it is not supported yet, is there any plan to support it? For example, some long prompt words have the same long prefix，whether it can be optimized? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ```

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Performance]: Is kv cache implemented globally in vllm， It can be shared by multiple concurrent inferences? performance ### Proposal to improve performance Is kv cache implemented globally in vllm， It can be shared by...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: same long prefix，whether it can be optimized? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
