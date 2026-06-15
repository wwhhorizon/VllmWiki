# vllm-project/vllm#7977: [Bug]: When enabling LoRA, greedy search got different answers.

| 字段 | 值 |
| --- | --- |
| Issue | [#7977](https://github.com/vllm-project/vllm/issues/7977) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: When enabling LoRA, greedy search got different answers.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using a lora adapter based on the llama-65b. I have started vllm v0.5.5 openai entrypoint with the following settings. ``` - args: - --model - /data/models/llama-65b-instruct/base - --tensor-parallel-size - "4" - --load-format - "auto" - --max-model-len - "8192" - --enable-lora - --max-loras - "8" - --max-cpu-loras - "30" - --max-lora-rank - "64" - --lora-dtype - bfloat16 - --uvicorn-log-level - warning - --lora-modules - 'lora1=/data/models/llama-65b-instruct/adapter/lora1' - 'lora2=/data/models/llama-65b-instruct/adapter/lora2' ``` adapter_config.json ``` { "alpha_pattern": {}, "auto_mapping": null, "base_model_name_or_path": "/data/models/llama-65b-instruct/base", "bias": "none", "fan_in_fan_out": false, "inference_mode": true, "init_lora_weights": true, "layer_replication": null, "layers_pattern": null, "layers_to_transform": null, "loftq_config": {}, "lora_alpha": 32, "lora_dropout": 0.05, "megatron_config": null, "megatron_core": "megatron.core", "modules_to_save": null, "peft_type": "LORA", "r": 16, "rank_pattern": {}, "revision": null, "target_modules": [ "q_proj", "k_proj", "v_proj", "o_proj" ], "task_type": "CAUSAL...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nment ### 🐛 Describe the bug I am using a lora adapter based on the llama-65b. I have started vllm v0.5.5 openai entrypoint with the following settings. ``` - args: - --model - /data/models/llama-65b-instruct/base - --t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: or each condition. What makes the difference in the answer? development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;triton build_error dty...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: u-loras - "30" - --max-lora-rank - "64" - --lora-dtype - bfloat16 - --uvicorn-log-level - warning - --lora-modules - 'lora1=/data/models/llama-65b-instruct/adapter/lora1' - 'lora2=/data/models/llama-65b-instruct/adapter...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: When enabling LoRA, greedy search got different answers. bug;stale ### Your current environment ### 🐛 Describe the bug I am using a lora adapter based on the llama-65b. I have started vllm v0.5.5 openai entrypoin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: When enabling LoRA, greedy search got different answers. bug;stale ### Your current environment ### 🐛 Describe the bug I am using a lora adapter based on the llama-65b. I have started vllm v0.5.5 openai entrypoin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
