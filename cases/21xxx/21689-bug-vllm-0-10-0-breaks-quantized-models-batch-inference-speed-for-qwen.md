# vllm-project/vllm#21689: [Bug]: VLLM 0.10.0 breaks quantized models batch inference speed for Qwen2.5-VL-7B (tested multiple quantization types)

| 字段 | 值 |
| --- | --- |
| Issue | [#21689](https://github.com/vllm-project/vllm/issues/21689) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM 0.10.0 breaks quantized models batch inference speed for Qwen2.5-VL-7B (tested multiple quantization types)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### EXPLANATION Was testing my script few days ago and it was working fine and can process batch with bnb and awq quantizations well. However when i installed in a new environment i was wondering why suddenly my script ran so slowly and i could not get the output? So i did some digging up. From the logs we can see after the update the batching took `2025-07-27 18:34:55,000 - INFO - Chunk 0s-30s processed in 92.11s` whereas in the previous 0.9.2 version it was `2025-07-27 18:18:16,564 - INFO - Chunk 0s-30s processed in 8.58s`. Some other dependencies that changed due to the update based on my observation was torch 2.7.0 -> 2.7.1 and transformers 4.53.3 -> 4.54.0 I really hope there will be a fix to this as I would want to benefit from the other optimizations in the update but i cannot continue with my project with this inference speed when using quantized batch qwen2.5vl. I highly suspect its something to do with multimodal models. as i tried vanilla qwen2.5 and it works well still ### **_OUTPUT BEFORE UPDATE_** ```logs (main) root@C.24242602:/workspace$ python scripts/core/video_analysis_vllm_native.py INFO 07-27 18:14:36 [__init...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nd can process batch with bnb and awq quantizations well. However when i installed in a new environment i was wondering why suddenly my script ran so slowly and i could not get the output? So i did some digging up. From...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: VLLM 0.10.0 breaks quantized models batch inference speed for Qwen2.5-VL-7B (tested multiple quantization types) bug;stale ### Your current environment ### 🐛 Describe the bug ### EXPLANATION Was testing my script...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ference speed for Qwen2.5-VL-7B (tested multiple quantization types) bug;stale ### Your current environment ### 🐛 Describe the bug ### EXPLANATION Was testing my script few days ago and it was working fine and can proce...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: VLLM 0.10.0 breaks quantized models batch inference speed for Qwen2.5-VL-7B (tested multiple quantization types) bug;stale ### Your current environment ### 🐛 Describe the bug ### EXPLANATION Was testing my script...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
