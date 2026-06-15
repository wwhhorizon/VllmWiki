# vllm-project/vllm#22077: [Bug]: GLM-4.1V lora trained model reports target_module mismatch error

| 字段 | 值 |
| --- | --- |
| Issue | [#22077](https://github.com/vllm-project/vllm/issues/22077) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.1V lora trained model reports target_module mismatch error

### Issue 正文摘录

### Your current environment root@dbc3e0868142:/data/shared/jyjang/LLaMA-Factory# CUDA_VISIBLE_DEVICES=0,1 DISABLE_VERSION_CHECK=1 python scripts/vllm_infer.py --model_name_or_path zai-org/GLM-4.1V-9B-Thinking --template glm4v --dataset mllm_eval_dataset --adapter_name_or_path /data/shared/jyjang /LLaMA-Factory/saves/glm4_1_v_9b/lora/version020/checkpoint-6000/ --vllm_config '{"max_lora_rank": 32}' ... ) - video_processor: Glm4vVideoProcessor { "crop_size": null, "data_format": "channels_first", "default_to_square": true, "device": null, "do_center_crop": null, "do_convert_rgb": true, "do_normalize": true, "do_pad": null, "do_rescale": true, "do_resize": true, "do_sample_frames": true, "fps": 2, "image_mean": [ 0.48145466, 0.4578275, 0.40821073 ], "image_std": [ 0.26862954, 0.26130258, 0.27577711 ], "input_data_format": null, "max_image_size": { "longest_edge": 47040000 }, "merge_size": 2, "num_frames": 16, "patch_size": 14, "processor_class": "Glm4vProcessor", "resample": 3, "rescale_factor": 0.00392156862745098, "size": { "longest_edge": 47040000, "shortest_edge": 12544 }, "size_divisor": null, "temporal_patch_size": 2, "video_metadata": null, "video_processor_type": "Glm4vVideo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: GLM-4.1V lora trained model reports target_module mismatch error bug ### Your current environment root@dbc3e0868142:/data/shared/jyjang/LLaMA-Factory# CUDA_VISIBLE_DEVICES=0,1 DISABLE_VERSION_CHECK=1 python scrip...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: GLM-4.1V lora trained model reports target_module mismatch error bug ### Your current environment root@dbc3e0868142:/data/shared/jyjang/LLaMA-Factory# CUDA_VISIBLE_DEVICES=0,1 DISABLE_VERSION_CHECK=1 python scrip...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 8142:/data/shared/jyjang/LLaMA-Factory# CUDA_VISIBLE_DEVICES=0,1 DISABLE_VERSION_CHECK=1 python scripts/vllm_infer.py --model_name_or_path zai-org/GLM-4.1V-9B-Thinking --template glm4v --dataset mllm_eval_dataset --adap...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: "video_metadata": null,
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ultiproc_executor.py:546] self.lora_manager.set_active_adapters(lora_requests, lora_mapping) (VllmWorker rank=0 pid=62314) ERROR 08-01 08:39:02 [multiproc_executor.py:546

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
