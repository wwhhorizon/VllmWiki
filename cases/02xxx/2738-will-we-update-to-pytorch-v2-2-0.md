# vllm-project/vllm#2738: Will we update to pytorch v2.2.0 ?

| 字段 | 值 |
| --- | --- |
| Issue | [#2738](https://github.com/vllm-project/vllm/issues/2738) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Will we update to pytorch v2.2.0 ?

### Issue 正文摘录

pytorch v2.2.0 has already release, will we update the next version? the version v2.1.2 has a bug which will cause oom while the newest version has already fixed. https://github.com/pytorch/pytorch/issues/106294

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rch v2.2.0 ? pytorch v2.2.0 has already release, will we update the next version? the version v2.1.2 has a bug which will cause oom while the newest version has already fixed. https://github.com/pytorch/pytorch/issues/1...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: e update the next version? the version v2.1.2 has a bug which will cause oom while the newest version has already fixed. https://github.com/pytorch/pytorch/issues/106294

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
