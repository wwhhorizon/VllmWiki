# vllm-project/vllm#2890: Integration of X-LoRA 

| 字段 | 值 |
| --- | --- |
| Issue | [#2890](https://github.com/vllm-project/vllm/issues/2890) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Integration of X-LoRA 

### Issue 正文摘录

Hello vLLM team, Thank you for your great work here! We have just released [X-LoRA](https://github.com/EricLBuehler/xlora), a flexible framework for large language models that allows efficient MoE over LoRA experts. We notice that vLLM enables LoRA and implements Mixtral. However, unlike other MoE models, X-LoRA would require 2 KV caches. This is because we employ a dual forward pass approach for a "single" forward pass of the model. How complicated would it be to implement this in vLLM? Thank you!

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: a), a flexible framework for large language models that allows efficient MoE over LoRA experts. We notice that vLLM enables LoRA and implements Mixtral. However, unlike other MoE models, X-LoRA would require 2 KV caches...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r/xlora), a flexible framework for large language models that allows efficient MoE over LoRA experts. We notice that vLLM enables LoRA and implements Mixtral. However, unlike other MoE models, X-LoRA would require 2 KV...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ements Mixtral. However, unlike other MoE models, X-LoRA would require 2 KV caches. This is because we employ a dual forward pass approach for a "single" forward pass of the model. How complicated would it be to impleme...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /github.com/EricLBuehler/xlora), a flexible framework for large language models that allows efficient MoE over LoRA experts. We notice that vLLM enables LoRA and implements Mixtral. However, unlike other MoE models, X-L...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
