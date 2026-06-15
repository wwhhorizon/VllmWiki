# vllm-project/vllm#42718: [Bug]: fully-sharded fused MoE W13 LoRA uses wrong slice offset after all-gather when local LoRA rank is 1

| 字段 | 值 |
| --- | --- |
| Issue | [#42718](https://github.com/vllm-project/vllm/issues/42718) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | fp8;kernel;moe;operator;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: fully-sharded fused MoE W13 LoRA uses wrong slice offset after all-gather when local LoRA rank is 1

### Issue 正文摘录

### Your current environment ### Describe the bug `fully_sharded_loras=True` with fused MoE LoRA can compute the wrong W13 slice in the expand kernel when the local LoRA rank per TP rank is 1. This is not the same as #32235. That issue was about the fused MoE LoRA launch grid size. This issue is about the post-all-gather memory layout of the W13 intermediate and the slice offset used by the expand kernel. Affected source path on current `main`: 1. `FusedMoEWithLoRA` uses two W13 slices for gated MoE: https://github.com/vllm-project/vllm/blob/75fd68c7a57a2f9560919a06863ea739ab46554c/vllm/lora/layers/fused_moe.py#L37-L40 2. `PunicaWrapperGPU.add_lora_w13` passes both slices into one combined fused MoE LoRA call: https://github.com/vllm-project/vllm/blob/75fd68c7a57a2f9560919a06863ea739ab46554c/vllm/lora/punica_wrapper/punica_gpu.py#L597-L612 3. In fully-sharded mode, the intermediate rank dimension is all-gathered before expand: https://github.com/vllm-project/vllm/blob/75fd68c7a57a2f9560919a06863ea739ab46554c/vllm/lora/ops/triton_ops/fused_moe_lora_op.py#L814-L827 4. `_fused_moe_lora_expand` flattens the tensor with `.view(-1, lastdim)` and passes `slice_a_size=a_intermediate_cache...

## 现有链接修复摘要

#42731 [Bugfix][LoRA] Dispatch fully-sharded fused MoE LoRA W13 expand per slice

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: oE LoRA launch grid size. This issue is about the post-all-gather memory layout of the W13 intermediate and the slice offset used by the expand kernel. Affected source path on current `main`: 1. `FusedMoEWithLoRA` uses...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: mption is false for local rank 1. Minimal stride reproducer: ```python import torch world = 16 num_slices = 2 tokens = 3 topk = 1 local_rank = 1 x = torch.empty(num_slices, tokens, topk, local_rank) input_size = tuple(x...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: eparate one-slice expand calls removed the local-rank-1 corruption. The FP8 fused MoE LoRA path appears to repeat the same pattern: https://github.com/vllm-project/vllm/blob/75fd68c7a57a2f9560919a06863ea739ab46554c/vllm...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: fully-sharded fused MoE W13 LoRA uses wrong slice offset after all-gather when local LoRA rank is 1 ### Your current environment ### Describe the bug `fully_sharded_loras=True` with fused MoE LoRA can compute the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: project/vllm/blob/75fd68c7a57a2f9560919a06863ea739ab46554c/vllm/lora/ops/triton_ops/fused_moe_lora_op.py#L814-L827 4. `_fused_moe_lora_expand` flattens the tensor with `.view(-1, lastdim)` and passes `slice_a_size=a_int...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42731](https://github.com/vllm-project/vllm/pull/42731) | closes_keyword | 0.95 | [Bugfix][LoRA] Dispatch fully-sharded fused MoE LoRA W13 expand per slice | Closes #42718. When `fully_sharded_loras=True` is combined with the gated W13 path of fused MoE LoRA, `tensor_model_parallel_all_gather` produces an intermediate cache whose slice |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
