# vllm-project/vllm#4433: [Usage]:  Is fused_moe/fused_moe.py only support num_expert= 8 and 16?

| 字段 | 值 |
| --- | --- |
| Issue | [#4433](https://github.com/vllm-project/vllm/issues/4433) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  Is fused_moe/fused_moe.py only support num_expert= 8 and 16?

### Issue 正文摘录

### Your current environment ```text version：V0.4.1 ``` ### How would you like to use vllm I want to run inference of a MoE model with num_expert=64. I don't know how to integrate it with vllm. https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/layers/fused_moe/configs In this directory, I only see configuration files that support E=8 and 16. Can we support other sizes, such as 32 and 64?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a MoE model with num_expert=64. I don't know how to integrate it with vllm. https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/layers/fuse...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Usage]: Is fused_moe/fused_moe.py only support num_expert= 8 and 16? usage;stale ### Your current environment ```text version：V0.4.1 ``` ### How would you like to use vllm I want to run inference of a MoE model with nu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: num_expert= 8 and 16? usage;stale ### Your current environment ```text version：V0.4.1 ``` ### How would you like to use vllm I want to run inference of a MoE model with num_expert=64. I don't know how to integrate it wi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ge]: Is fused_moe/fused_moe.py only support num_expert= 8 and 16? usage;stale ### Your current environment ```text version：V0.4.1 ``` ### How would you like to use vllm I want to run inference of a MoE model with num_ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
