# vllm-project/vllm#26213: [Bug]: LLamaFactory-trained GLM-4.1v-9B-Thinking is not compatible with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#26213](https://github.com/vllm-project/vllm/issues/26213) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLamaFactory-trained GLM-4.1v-9B-Thinking is not compatible with vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The original GLM-4.1v-9B-Thinking model works with vLLM nicely. After finetuning it with LLaMA Factory with the script below, ``` { "stage": "sft", "do_train": true, "model_name_or_path": "zai-org/GLM-4.1V-9B-Thinking", "dataset": "webgym_training", "dataset_dir": "llamafactory_data", "template": "glm4v", "finetuning_type": "full", "output_dir": "model.pt", "overwrite_output_dir": true, "trust_remote_code": true, "cutoff_len": 16384, "per_device_train_batch_size": 3, "gradient_accumulation_steps": 4, "learning_rate": 5e-05, "max_grad_norm": 1.0, "num_train_epochs": 1.0, "logging_steps": 10, "save_steps": 1000, "warmup_ratio": 0.1, "lr_scheduler_type": "cosine", "preprocessing_num_workers": 16, "dataloader_num_workers": 4, "bf16": true, "remove_unused_columns": false, "report_to": "wandb", "save_only_model": true, "dataloader_pin_memory": true, "gradient_checkpointing": true, "deepspeed": "ds_config_zero3.json", "plot_loss": false, "run_name": "glm_debug-update" ``` ``` { "bf16": { "enabled": true }, "train_micro_batch_size_per_gpu": "auto", "train_batch_size": "auto", "gradient_accumulation_steps": "auto", "activation_checkpointi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: LLamaFactory-trained GLM-4.1v-9B-Thinking is not compatible with vLLM bug ### Your current environment ### 🐛 Describe the bug The original GLM-4.1v-9B-Thinking model works with vLLM nicely. After finetuning it wi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: "logging_steps": 10, "save_steps": 1000, "warmup_ratio": 0.1, "lr_scheduler_type": "cosine", "preprocessing_num_workers": 16, "dataloader_num_workers": 4, "bf16": true, "remove_unused_columns": false, "report_to": "wand...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e", "preprocessing_num_workers": 16, "dataloader_num_workers": 4, "bf16": true, "remove_unused_columns": false, "report_to": "wandb", "save_only_model": true, "dataloader_pin_memory": true, "gradient_checkpointing": tru...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: dataloader_num_workers": 4, "bf16": true, "remove_unused_columns": false, "report_to": "wandb", "save_only_model": true, "dataloader_pin_memory": true, "gradient_checkpointing": true, "deepspeed": "ds_config_zero3.json"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: x_tokens=100, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([1, 2, 3, 4,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
