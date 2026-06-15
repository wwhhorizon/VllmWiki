# vllm-project/vllm#31205: ValueError: Qwen3OmniMoeThinkerForConditionalGeneration does not support LoRA yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#31205](https://github.com/vllm-project/vllm/issues/31205) |
| 状态 | open |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: Qwen3OmniMoeThinkerForConditionalGeneration does not support LoRA yet.

### Issue 正文摘录

hi, I have trained qwen3-omni thinker via ms-swift. However, when I tried to infer qwen3-omni with lora ckpt, an error occurred: ``` ValueError: Qwen3OmniMoeThinkerForConditionalGeneration does not support LoRA yet. ``` I have tried many verions of vllm including 0.9.2, 0.11.0 and 0.12.0 here is my script: ``` CUDA_VISIBLE_DEVICES=0,1 \ MAX_PIXELS=1003520 \ swift infer \ --model models/omni/Qwen3-Omni/Qwen3-Omni-30B-A3B-Instruct \ --adapters ckpt/Qwen3-Omni/v4-20251212-163234/checkpoint-3 \ --merge_lora false \ --stream true \ --infer_backend vllm \ --val_dataset ms-swift/data/train_test.jsonl \ --vllm_gpu_memory_utilization 0.9 \ --vllm_tensor_parallel_size 2 \ --vllm_max_model_len 32768 \ --max_new_tokens 2048 \ --vllm_limit_mm_per_prompt '{'image': 3, 'video': 3, 'audio': 3}' ``` how can I solved this problem?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ValueError: Qwen3OmniMoeThinkerForConditionalGeneration does not support LoRA yet. usage;stale hi, I have trained qwen3-omni thinker via ms-swift. However, when I tried to infer qwen3-omni with lora ckpt, an error occur...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: /checkpoint-3 \ --merge_lora false \ --stream true \ --infer_backend vllm \ --val_dataset ms-swift/data/train_test.jsonl \ --vllm_gpu_memory_utilization 0.9 \ --vllm_tensor_parallel_size 2 \ --vllm_max_model_len 32768 \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ions of vllm including 0.9.2, 0.11.0 and 0.12.0 here is my script: ``` CUDA_VISIBLE_DEVICES=0,1 \ MAX_PIXELS=1003520 \ swift infer \ --model models/omni/Qwen3-Omni/Qwen3-Omni-30B-A3B-Instruct \ --adapters ckpt/Qwen3-Omn...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rs ckpt/Qwen3-Omni/v4-20251212-163234/checkpoint-3 \ --merge_lora false \ --stream true \ --infer_backend vllm \ --val_dataset ms-swift/data/train_test.jsonl \ --vllm_gpu_memory_utilization 0.9 \ --vllm_tensor_parallel_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ValueError: Qwen3OmniMoeThinkerForConditionalGeneration does not support LoRA yet. usage;stale hi, I have trained qwen3-omni thinker via ms-swift. However, when I tried to infer qwen3-omni with lora ckpt, an error occur...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
