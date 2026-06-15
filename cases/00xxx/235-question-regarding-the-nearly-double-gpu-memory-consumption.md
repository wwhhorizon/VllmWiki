# vllm-project/vllm#235:  Question regarding the nearly double GPU memory consumption.

| 字段 | 值 |
| --- | --- |
| Issue | [#235](https://github.com/vllm-project/vllm/issues/235) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

>  Question regarding the nearly double GPU memory consumption.

### Issue 正文摘录

when i loaded vicuna7b_v1.3 with default config ,i found that gpu memory cost around 23G, but in fastchat's readme says > 'requires around 14GB of GPU memory for Vicuna-7B ' anyway, the throughput is much more faster. I just want to confirm if the GPU memory usage in this scenario is normal. If it is normal, I would like to know why there is almost twice the consumption. thanks a lot

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Question regarding the nearly double GPU memory consumption. when i loaded vicuna7b_v1.3 with default config ,i found that gpu memory cost around 23G, but in fastchat's readme says > 'requires around 14GB of GPU memory...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: double GPU memory consumption. when i loaded vicuna7b_v1.3 with default config ,i found that gpu memory cost around 23G, but in fastchat's readme says > 'requires around 14GB of GPU memory for Vicuna-7B ' anyway, the th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ays > 'requires around 14GB of GPU memory for Vicuna-7B ' anyway, the throughput is much more faster. I just want to confirm if the GPU memory usage in this scenario is normal. If it is normal, I would like to know why...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
