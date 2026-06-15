# vllm-project/vllm#6067: [New Model]: Lora for Qwen/Qwen2-57B-A14B

| 字段 | 值 |
| --- | --- |
| Issue | [#6067](https://github.com/vllm-project/vllm/issues/6067) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Lora for Qwen/Qwen2-57B-A14B

### Issue 正文摘录

### The model to consider. Lora support for Qwen/Qwen2-57B-A14B (Qwen2MoeForCausalLM) ### The closest model vllm already supports. Qwen/Qwen2-72B ### What's your difficulty of supporting the model you want? When running vllm with a lora module for the Qwen2 MoE model the server fails with the following error message: `ValueError: Model Qwen2MoeForCausalLM does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github.`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Lora for Qwen/Qwen2-57B-A14B new-model;stale ### The model to consider. Lora support for Qwen/Qwen2-57B-A14B (Qwen2MoeForCausalLM) ### The closest model vllm already supports. Qwen/Qwen2-72B ### What's your...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github.`
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e ### The model to consider. Lora support for Qwen/Qwen2-57B-A14B (Qwen2MoeForCausalLM) ### The closest model vllm already supports. Qwen/Qwen2-72B ### What's your difficulty of supporting the model you want? When runni...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Lora for Qwen/Qwen2-57B-A14B new-model;stale ### The model to consider. Lora support for Qwen/Qwen2-57B-A14B (Qwen2MoeForCausalLM) ### The closest model vllm already supports. Qwen/Qwen2-72B ### What's your...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
