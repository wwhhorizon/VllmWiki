# vllm-project/vllm#3285: Mixtral 4x 4090 OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#3285](https://github.com/vllm-project/vllm/issues/3285) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mixtral 4x 4090 OOM

### Issue 正文摘录

Hi! TP 4, model len 1000, enforce eager, multiple gpu utilizations; Nothing helps. I am testing on a 4x 4090 rig and I always get an OOM error, no matter what I try. Thanks in advance!

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Mixtral 4x 4090 OOM Hi! TP 4, model len 1000, enforce eager, multiple gpu utilizations; Nothing helps. I am testing on a 4x 4090 rig and I always get an OOM error, no matter what I try. Thanks in advance!
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Mixtral 4x 4090 OOM Hi! TP 4, model len 1000, enforce eager, multiple gpu utilizations; Nothing helps. I am testing on a 4x 4090 rig and I always get an OOM error, no matter what I try. Thanks in advance!
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: len 1000, enforce eager, multiple gpu utilizations; Nothing helps. I am testing on a 4x 4090 rig and I always get an OOM error, no matter what I try. Thanks in advance!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
