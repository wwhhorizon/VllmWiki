# vllm-project/vllm#1008: error when running bloom model

| 字段 | 值 |
| --- | --- |
| Issue | [#1008](https://github.com/vllm-project/vllm/issues/1008) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> error when running bloom model

### Issue 正文摘录

``` RuntimeError: invalid dtype for bias - should match query's dtype ``` it works well when I load llama model, but I get that error when I tried to run bloom

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: error when running bloom model ``` RuntimeError: invalid dtype for bias - should match query's dtype ``` it works well when I load llama model, but I get that error when I tried to run bloom
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: error when running bloom model ``` RuntimeError: invalid dtype for bias - should match query's dtype ``` it works well when I load llama model, but I get that error when I tried to run bloom
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: error when running bloom model ``` RuntimeError: invalid dtype for bias - should match query's dtype ``` it works well when I load llama model, but I get that error when I tried to run bloom

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
