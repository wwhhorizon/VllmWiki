# vllm-project/vllm#69: Decrease the default size of swap space

| 字段 | 值 |
| --- | --- |
| Issue | [#69](https://github.com/vllm-project/vllm/issues/69) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Decrease the default size of swap space

### Issue 正文摘录

The current default swap space size (20 GiB per GPU) is a bit too large. It can lead to OOM especially for the machine with multiple GPUs.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: p space size (20 GiB per GPU) is a bit too large. It can lead to OOM especially for the machine with multiple GPUs.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ault swap space size (20 GiB per GPU) is a bit too large. It can lead to OOM especially for the machine with multiple GPUs.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
