# vllm-project/vllm#37659: [Bug]: RuntimeError: 基于megatron grpo Qwen3-Omni模型时，出现RuntimeError: Event device index  does not match recording stream's device index

| 字段 | 值 |
| --- | --- |
| Issue | [#37659](https://github.com/vllm-project/vllm/issues/37659) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: 基于megatron grpo Qwen3-Omni模型时，出现RuntimeError: Event device index  does not match recording stream's device index

### Issue 正文摘录

### Your current environment torch 2.10.0 vllm 0.17.1 flash-attn 2.8.3 cuda 12.9 基于megatron grpo Qwen3-Omni模型时，出现此错误，请问这是什么原因呢？ ```text export MEGATRON_LM_PATH="ms-swift/swift/megatron/Megatron-LM" export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5 export NPROC_PER_NODE=6 export PYTORCH_CUDA_ALLOC_CONF='expandable_segments:True' export WANDB_MODE=disabled export MASTER_PORT=29510 megatron rlhf \ --rlhf_type grpo \ --model /data/model/Qwen/Qwen3-Omni-30B-A3B-Instruct \ --dataset data_shuffle_train_grpo.jsonl \ --output_dir megatron_Qwen-Omni \ --num_train_epochs 1 \ --global_batch_size 6 \ --micro_batch_size 1 \ --steps_per_generation 1 \ --num_generations 2 \ --reward_funcs accuracy format \ --use_vllm true \ --vllm_mode colocate \ --vllm_tensor_parallel_size 2 \ --vllm_gpu_memory_utilization 0.60 \ --vllm_max_model_len 1024 \ --max_length 1024 \ --max_completion_length 512 \ --tensor_model_parallel_size 2 \ --pipeline_model_parallel_size 3 \ --context_parallel_size 1 \ --expert_model_parallel_size 1 \ --tuner_type lora \ --lr 5e-5 \ --bf16 true \ --beta 0.00 \ --importance_sampling_level sequence \ --epsilon 3e-4 \ --epsilon_high 4e-4 \ --dynamic_sample false \ --overlong_filter true \ --lo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: RuntimeError: 基于megatron grpo Qwen3-Omni模型时，出现RuntimeError: Event device index does not match recording stream's device index bug ### Your current environment torch 2.10.0 vllm 0.17.1 flash-attn 2.8.3 cuda 12.9 基...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: er_type lora \ --lr 5e-5 \ --bf16 true \ --beta 0.00 \ --importance_sampling_level sequence \ --epsilon 3e-4 \ --epsilon_high 4e-4 \ --dynamic_sample false \ --overlong_filter true \ --loss_type grpo \ --sleep_level 1 \...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: verlong_filter true \ --loss_type grpo \ --sleep_level 1 \ --offload_model true \ --offload_bridge true \ --offload_optimizer true \ --logging_steps 1 \ --recompute_granularity selective \ --finetune \ --dataloader_num_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: t_num_proc 4 \ --no_save_optim \ --no_save_rng \ --attention_backend flash \ --temperature 1.0 \ --padding_free false \ --sequence_parallel true \ --log_completions true ``` ### 🐛 Describe the bug 基于megatron grpo Qwen3-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rt_model_parallel_size 1 \ --tuner_type lora \ --lr 5e-5 \ --bf16 true \ --beta 0.00 \ --importance_sampling_level sequence \ --epsilon 3e-4 \ --epsilon_high 4e-4 \ --dynamic_sample false \ --overlong_filter true \ --lo...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
