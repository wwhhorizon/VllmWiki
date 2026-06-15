# vllm-project/vllm#2326: Load awq models in CPU ?

| 字段 | 值 |
| --- | --- |
| Issue | [#2326](https://github.com/vllm-project/vllm/issues/2326) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Load awq models in CPU ?

### Issue 正文摘录

is it possible to load the awq qunatized models into CPU memory instead of GPU memory ? similar issue : #999

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: it possible to load the awq qunatized models into CPU memory instead of GPU memory ? similar issue : #999
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Load awq models in CPU ? is it possible to load the awq qunatized models into CPU memory instead of GPU memory ? similar issue : #999

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
