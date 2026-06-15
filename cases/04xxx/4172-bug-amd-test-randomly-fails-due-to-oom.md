# vllm-project/vllm#4172: [Bug]: AMD test randomly fails due to OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#4172](https://github.com/vllm-project/vllm/issues/4172) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AMD test randomly fails due to OOM

### Issue 正文摘录

### Your current environment CI environment ### 🐛 Describe the bug A lot of CI runs are getting stuck/failing at the AMD part. Seems that OOM occurs during the AMD test which causes port 8000 to be unreachable. Due to the long timeout, the duration of CI runs has gone up dramatically.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g]: AMD test randomly fails due to OOM bug ### Your current environment CI environment ### 🐛 Describe the bug A lot of CI runs are getting stuck/failing at the AMD part. Seems that OOM occurs during the AMD test which c...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: AMD test randomly fails due to OOM bug ### Your current environment CI environment ### 🐛 Describe the bug A lot of CI runs are getting stuck/failing at the AMD part. Seems that OOM occurs during the AMD test whic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: AMD test randomly fails due to OOM bug ### Your current environment CI environment ### 🐛 Describe the bug A lot of CI runs are getting stuck/failing at the AMD part. Seems that OOM occurs during the AMD test whic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
