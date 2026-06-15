# vllm-project/vllm#14483: [Bug]: trl's grpo-trainer with vllm not convergence

| 字段 | 值 |
| --- | --- |
| Issue | [#14483](https://github.com/vllm-project/vllm/issues/14483) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: trl's grpo-trainer with vllm not convergence

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/2eb58d78-d6aa-4ddb-ae3f-1c980fdf833a) Two upper curves describe GRPO process without vllm, while two lower curves describe the process with vllm, which use the same model Qwen-2.5-7B/1.5B-Instruct. related code ds = load_dataset('swulling/gsm8k_chinese', cache_dir=local_cache_dir) data = process_data(ds['train']) training_args = GRPOConfig( output_dir=output_dir, learning_rate=5e-6, adam_beta1 = 0.9, adam_beta2 = 0.99, weight_decay = 0.1, warmup_ratio = 0.1, lr_scheduler_type='cosine', logging_steps=10, # fp16=True, # not go convergence whether fp16 or fp32 per_device_train_batch_size=1, gradient_accumulation_steps=2, num_generations=3, # =4 when use_vllm=False max_prompt_length=256, max_completion_length=512, num_train_epochs=1, save_steps=500, max_grad_norm=0.1, log_on_each_node=False, use_vllm=True, report_to="tensorboard", vllm_dtype="float32", # not go convergence whether fp16 or fp32 vllm_gpu_memory_utilization=0.5 # temperature=1.2 # vllm_max_model_len=256 # save_strategy='epoch' ) trainer = GRPOTrainer( model=model, processing_class=tokenizer, reward_funcs=[ # mark_rewar...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: hile two lower curves describe the process with vllm, which use the same model Qwen-2.5-7B/1.5B-Instruct. related code ds = load_dataset('swulling/gsm8k_chinese', cache_dir=local_cache_dir) data = process_data(ds['train...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error dt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: wen-2.5-7B/1.5B-Instruct. related code ds = load_dataset('swulling/gsm8k_chinese', cache_dir=local_cache_dir) data = process_data(ds['train']) training_args = GRPOConfig( output_dir=output_dir, learning_rate=5e-6, adam_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: se, use_vllm=True, report_to="tensorboard", vllm_dtype="float32", # not go convergence whether fp16 or fp32 vllm_gpu_memory_utilization=0.5 # temperature=1.2 # vllm_max_model_len=256 # save_strategy='epoch' ) trainer =...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 0.99, weight_decay = 0.1, warmup_ratio = 0.1, lr_scheduler_type='cosine', logging_steps=10, # fp16=True, # not go convergence whether fp16 or fp32 per_device_train_batch_size=1, gradient_accumulation_steps=2, num_genera...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
