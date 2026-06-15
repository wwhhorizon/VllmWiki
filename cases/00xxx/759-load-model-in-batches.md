# vllm-project/vllm#759: load model in batches

| 字段 | 值 |
| --- | --- |
| Issue | [#759](https://github.com/vllm-project/vllm/issues/759) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> load model in batches

### Issue 正文摘录

when test vllm with large model, I notice that vllm will first load the whole model into cpu memory and then move it to gpu memory, this makes the cpu memory at least be the size of the model large, if the model is 70b that could be a lot of memory required. I wonder if there's any way to load model in batches to reduce the memory usage, since cpu memory seems to be only used during initialization.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: vllm will first load the whole model into cpu memory and then move it to gpu memory, this makes the cpu memory at least be the size of the model large, if the model is 70b that could be a lot of memory required. I wonde...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: load model in batches when test vllm with large model, I notice that vllm will first load the whole model into cpu memory and then move it to gpu memory, this makes the cpu memory at least be the size of the model large...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: load model in batches when test vllm with large model, I notice that vllm will first load the whole model into cpu memory and then move it to gpu memory, this makes the cpu memory at least be the size of the model large...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
