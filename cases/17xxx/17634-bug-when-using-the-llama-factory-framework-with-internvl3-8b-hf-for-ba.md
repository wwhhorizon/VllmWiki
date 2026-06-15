# vllm-project/vllm#17634: [Bug]: When using the LLaMA-Factory framework with InternVL3-8B-hf for batch inference, vLLM throws an error: ValueError: limit_mm_per_prompt is only supported for multimodal models.

| 字段 | 值 |
| --- | --- |
| Issue | [#17634](https://github.com/vllm-project/vllm/issues/17634) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;model_support;multimodal_vlm |
| 子分类 | memory |
| Operator 关键词 | activation |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using the LLaMA-Factory framework with InternVL3-8B-hf for batch inference, vLLM throws an error: ValueError: limit_mm_per_prompt is only supported for multimodal models.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Debug Report** ```text raceback (most recent call last): File "/nfs/home/1016_yangdong/meaning-map/LLaMA-Factory-main/scripts/vllm_infer.py", line 164, in fire.Fire(vllm_infer) File "/nfs/home/1016_yangdong/.conda/envs/meaning_map/lib/python3.11/site-packages/fire/core.py", line 135, in Fire component_trace = _Fire(component, args, parsed_flag_args, context, name) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/nfs/home/1016_yangdong/.conda/envs/meaning_map/lib/python3.11/site-packages/fire/core.py", line 468, in _Fire component, remaining_args = _CallAndUpdateTrace( ^^^^^^^^^^^^^^^^^^^^ File "/nfs/home/1016_yangdong/.conda/envs/meaning_map/lib/python3.11/site-packages/fire/core.py", line 684, in _CallAndUpdateTrace component = fn(*varargs, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^ File "/nfs/home/1016_yangdong/meaning-map/LLaMA-Factory-main/scripts/vllm_infer.py", line 152, in vllm_infer results = LLM(**engine_args).generate(inputs, sampling_params, lora_request=lora_request) ^^^^^^^^^^^^^^^^^^ File "/nfs/home/1016_yangdong/.conda/envs/meaning_map/lib/python3.11/site-packages/vllm/utils.py", line 1161, in inner return fn...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: When using the LLaMA-Factory framework with InternVL3-8B-hf for batch inference, vLLM throws an error: ValueError: limit_mm_per_prompt is only supported for multimodal models. bug;stale ### Your current environme...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: } ``` **Question:** When invoking the InternVL3-8B-hf model (including versions fine-tuned with LoRA), vLLM fails to recognize the model as a multimodal model. **Model config InternVLConfig** { "architectures": [ "Inter...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: }, "rope_theta": 1000000.0, "sliding_window": null, "torch_dtype": "bfloat16", "use_cache": true, "use_sliding_window": false, "vocab_size": 151674 }, "torch_dtype": "bfloat16", "transformers_version": "4.52.0.dev0", "v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eError: limit_mm_per_prompt is only supported for multimodal models. bug;stale ### Your current environment ### 🐛 Describe the bug **Debug Report** ```text raceback (most recent call last): File "/nfs/home/1016_yangdong...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: the model as a multimodal model. **Model config InternVLConfig** { "architectures": [ "InternVLForConditionalGeneration" ], "downsample_ratio": 0.5, "image_seq_length": 256, "image_token_id": 151667, "model_type": "inte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
