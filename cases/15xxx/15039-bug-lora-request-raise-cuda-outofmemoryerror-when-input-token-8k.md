# vllm-project/vllm#15039: [Bug]: LoRA request raise CUDA OutOfMemoryError when input token > 8k

| 字段 | 值 |
| --- | --- |
| Issue | [#15039](https://github.com/vllm-project/vllm/issues/15039) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRA request raise CUDA OutOfMemoryError when input token > 8k

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to deploy a [Llama 3.3](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) server with single LoRA adapter loaded. The particular LoRA adapter has the following `adapter_config.json`, if it is of any help: ```json { "alpha_pattern": {}, "auto_mapping": null, "base_model_name_or_path": "/mnt/shared-models/meta-llama/Llama-3.3-70B-Instruct", "bias": "none", "eva_config": null, "exclude_modules": null, "fan_in_fan_out": false, "inference_mode": true, "init_lora_weights": true, "layer_replication": null, "layers_pattern": null, "layers_to_transform": null, "loftq_config": {}, "lora_alpha": 16, "lora_bias": false, "lora_dropout": 0.1, "megatron_config": null, "megatron_core": "megatron.core", "modules_to_save": null, "peft_type": "LORA", "r": 8, "rank_pattern": {}, "revision": null, "target_modules": [ "k_proj", "o_proj", "q_proj", "v_proj", "up_proj", "down_proj", "gate_proj" ], "task_type": "CAUSAL_LM", "use_dora": false, "use_rslora": false } ``` The llama 3.3 model I am using is the huggingface vanilla one. No other customization made. Within a H100 4GPU node, I was able to launch a model server with the followin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: current environment ### 🐛 Describe the bug I'm trying to deploy a [Llama 3.3](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) server with single LoRA adapter loaded. The particular LoRA adapter has the followi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: context test I'm using a sample script like this, copied here for reproducibility: ```python import json import os import uuid from transformers import AutoTokenizer from openai import OpenAI client = OpenAI(base_url=os...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: LoRA request raise CUDA OutOfMemoryError when input token > 8k bug ### Your current environment ### 🐛 Describe the bug I'm trying to deploy a [Llama 3.3](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: LoRA request raise CUDA OutOfMemoryError when input token > 8k bug ### Your current environment ### 🐛 Describe the bug I'm trying to deploy a [Llama 3.3](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: g.json`, if it is of any help: ```json { "alpha_pattern": {}, "auto_mapping": null, "base_model_name_or_path": "/mnt/shared-models/meta-llama/Llama-3.3-70B-Instruct", "bias": "none", "eva_config": null, "exclude_modules...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
