# vllm-project/vllm#17439: [Usage]: Resource requirement of large MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#17439](https://github.com/vllm-project/vllm/issues/17439) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;moe |
| 子分类 |  |
| Operator 关键词 | moe |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Resource requirement of large MoE models

### Issue 正文摘录

### Your current environment This question should apply to the latest GPUs, such as `A100/A800/H100/H800/H200` x 8 x N. ### How would you like to use vllm I want to run local inference of these large models during RL. How many gpus should I use for a large MoE model (e.g. Qwen3 235B-A22B)? More specifically, 1. how to set `tensor_parallel_size`? 2. will `vllm` offload experts that are not activated? - This would eat a lot of CPU memory. I would rather use EP or just split the model across N GPUs among >1 physical nodes. cc. @andrew @tmm1 @markmc ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ent environment This question should apply to the latest GPUs, such as `A100/A800/H100/H800/H200` x 8 x N. ### How would you like to use vllm I want to run local inference of these large models during RL. How many gpus...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Resource requirement of large MoE models usage ### Your current environment This question should apply to the latest GPUs, such as `A100/A800/H100/H800/H200` x 8 x N. ### How would you like to use vllm I want t...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Usage]: Resource requirement of large MoE models usage ### Your current environment This question should apply to the latest GPUs, such as `A100/A800/H100/H800/H200` x 8 x N. ### How would you like to use vllm I want t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pus should I use for a large MoE model (e.g. Qwen3 235B-A22B)? More specifically, 1. how to set `tensor_parallel_size`? 2. will `vllm` offload experts that are not activated? - This would eat a lot of CPU memory. I woul...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: More specifically, 1. how to set `tensor_parallel_size`? 2. will `vllm` offload experts that are not activated? - This would eat a lot of CPU memory. I would rather use EP or just split the model across N GPUs among >1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
