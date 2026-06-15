# vllm-project/vllm#2194: KV cache usage

| 字段 | 值 |
| --- | --- |
| Issue | [#2194](https://github.com/vllm-project/vllm/issues/2194) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> KV cache usage

### Issue 正文摘录

Hello! I'm a researcher and developing with this awesome project. I just wonder how I can get the memory consumption of each part (model, kvcache e.t.c). Thanks!

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: KV cache usage Hello! I'm a researcher and developing with this awesome project. I just wonder how I can get the memory consumption of each part (model, kvcache e.t.c). Thanks!
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: KV cache usage Hello! I'm a researcher and developing with this awesome project. I just wonder how I can get the memory consumption of each part (model, kvcache e.t.c). Thanks!
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: roject. I just wonder how I can get the memory consumption of each part (model, kvcache e.t.c). Thanks!

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
