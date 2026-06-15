# vllm-project/vllm#9280: [Bug]: VLLM doesn't support LoRa with config `modules_to_save`

| 字段 | 值 |
| --- | --- |
| Issue | [#9280](https://github.com/vllm-project/vllm/issues/9280) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM doesn't support LoRa with config `modules_to_save`

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have a lora for Qwen with this adapter config: ```json { "alpha_pattern": {}, "auto_mapping": { "base_model_class": "Qwen2ForCausalLM" }, "base_model_name_or_path": "/models/Qwen2.5-3B-Instruct", "bias": "none", "fan_in_fan_out": false, "inference_mode": true, "init_lora_weights": true, "layer_replication": null, "layers_pattern": null, "layers_to_transform": null, "loftq_config": {}, "lora_alpha": 32, "lora_dropout": 0.05, "megatron_config": null, "megatron_core": "megatron.core", "modules_to_save": [ "embed_tokens", "lm_head" ], "peft_type": "LORA", "r": 32, "rank_pattern": {}, "revision": null, "target_modules": [ "gate_proj", "up_proj", "o_proj", "k_proj", "q_proj", "down_proj", "v_proj" ], "task_type": null, "use_dora": false, "use_rslora": false } ``` There is clearly a parameter called `modules_to_save` which means that module is not frozen in peft when trained and saved inside `adapter_model.safetensors` as `base_model.model.lm_head.weight` and `base_model.model.model.embed_tokens`. But, vllm is not support it yet and I got this error when serving the model and lora ```bash ERROR 10-1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: VLLM doesn't support LoRa with config `modules_to_save` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have a lora for Qwen with this adapter config: ```json {...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: VLLM doesn't support LoRa with config `modules_to_save` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I have a lora for Qwen with this adapter config: ```json {...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Qwen with this adapter config: ```json { "alpha_pattern": {}, "auto_mapping": { "base_model_class": "Qwen2ForCausalLM" }, "base_model_name_or_path": "/models/Qwen2.5-3B-Instruct", "bias": "none", "fan_in_fan_out": false...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
