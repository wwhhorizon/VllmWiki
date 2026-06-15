# vllm-project/vllm#36856: [Usage]: 'LLMEngine' object has no attribute 'collective_rpc'

| 字段 | 值 |
| --- | --- |
| Issue | [#36856](https://github.com/vllm-project/vllm/issues/36856) |
| 状态 | open |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 'LLMEngine' object has no attribute 'collective_rpc'

### Issue 正文摘录

### Your current environment I try to run the demo for GKD training. while I met a question: -----vllm server------------- export PYTHONPATH='/mnt/bn/miniconda3/envs/opd/lib/python3.10/site-packages' CUDA_VISIBLE_DEVICES=0 swift rollout --model '/Qwen/Qwen3-8B' --torch_dtype bfloat16 --vllm_tensor_parallel_size 1 --vllm_gpu_memory_utilization 0.9 --max_model_len 8192 --vllm_enable_prefix_caching true --host 127.0.0.1 --port 8000 -----gkd ------------- NPROC_PER_NODE=1 PYTORCH_CUDA_ALLOC_CONF='expandable_segments:True' CUDA_VISIBLE_DEVICES=1 export PYTHONPATH='/mnt/bn/miniconda3/envs/opd/lib/python3.10/site-packages' swift rlhf --rlhf_type gkd --model 'Qwen/Qwen3-0___6B' --teacher_model 'Qwen/Qwen3-8B' --tuner_type full --dataset 'openr1/train-00000-of-00001.parquet' --seq_kd false --lmbda 1 --beta 1 --torch_dtype float16 --num_train_epochs 1 --per_device_train_batch_size 1 --learning_rate 1e-5 --gradient_accumulation_steps 1 --save_steps 1000 --save_total_limit 2 --logging_steps 1 --max_length 16000 --max_completion_length 8192 --output_dir output --warmup_ratio 0.05 --save_only_model true --dataloader_num_workers 64 --dataset_num_proc 4 --deepspeed zero2 --teacher_deepspeed zero3...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: s' CUDA_VISIBLE_DEVICES=0 swift rollout --model '/Qwen/Qwen3-8B' --torch_dtype bfloat16 --vllm_tensor_parallel_size 1 --vllm_gpu_memory_utilization 0.9 --max_model_len 8192 --vllm_enable_prefix_caching true --host 127.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: opd/lib/python3.10/site-packages' CUDA_VISIBLE_DEVICES=0 swift rollout --model '/Qwen/Qwen3-8B' --torch_dtype bfloat16 --vllm_tensor_parallel_size 1 --vllm_gpu_memory_utilization 0.9 --max_model_len 8192 --vllm_enable_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ): ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rt PYTHONPATH='/mnt/bn/miniconda3/envs/opd/lib/python3.10/site-packages' CUDA_VISIBLE_DEVICES=0 swift rollout --model '/Qwen/Qwen3-8B' --torch_dtype bfloat16 --vllm_tensor_parallel_size 1 --vllm_gpu_memory_utilization 0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ner_type full --dataset 'openr1/train-00000-of-00001.parquet' --seq_kd false --lmbda 1 --beta 1 --torch_dtype float16 --num_train_epochs 1 --per_device_train_batch_size 1 --learning_rate 1e-5 --gradient_accumulation_ste...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
