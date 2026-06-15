# vllm-project/vllm#253: Why does loading the vicuna-13b-v1.1 model in FastChat require 26GB of GPU memory, while VLLM requires 37GB of GPU memory?

| 字段 | 值 |
| --- | --- |
| Issue | [#253](https://github.com/vllm-project/vllm/issues/253) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why does loading the vicuna-13b-v1.1 model in FastChat require 26GB of GPU memory, while VLLM requires 37GB of GPU memory?

### Issue 正文摘录

_本地原始数据中没有 issue 正文。_

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Why does loading the vicuna-13b-v1.1 model in FastChat require 26GB of GPU memory, while VLLM requires 37GB of GPU memory?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Why does loading the vicuna-13b-v1.1 model in FastChat require 26GB of GPU memory, while VLLM requires 37GB of GPU memory?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
