# vllm-project/vllm#17007: [Bug]: ```image_grid_thw``` not set in ```CachedRequestState``` - ```Qwen2.5 VL 3B```

| 字段 | 值 |
| --- | --- |
| Issue | [#17007](https://github.com/vllm-project/vllm/issues/17007) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ```image_grid_thw``` not set in ```CachedRequestState``` - ```Qwen2.5 VL 3B```

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When initializing Qwen2.5 VL 3B, cached request does not set the ``` mm_inputs=[]``` field. Thus, in ```model_executor/layers/rotary_embedding.py", line 1079, in get_input_positions_tensor``` I got ``` ERROR 04-22 18:12:57 [core.py:390] image_grid_thw[image_index][0], ERROR 04-22 18:12:57 [core.py:390] ~~~~~~~~~~~~~~^^^^^^^^^^^^^ ERROR 04-22 18:12:57 [core.py:390] IndexError: list index out of range ``` ## Code ``` llm = LLM( model=script_args.model, revision=script_args.revision, tensor_parallel_size=script_args.tensor_parallel_size, gpu_memory_utilization=script_args.gpu_memory_utilization, dtype=script_args.dtype, # Automatic Prefix Caching caches the KV cache of existing queries, so that a new query can # directly reuse the KV cache if it shares the same prefix with one of the existing queries. # This is particularly useful here because we generate completions from the same prompts. enable_prefix_caching=script_args.enable_prefix_caching, max_model_len=script_args.max_model_len, worker_extension_cls="trl.scripts.vllm_serve.WeightSyncWorkerExtension", # for multimodal input limit_mm_per_prompt={"image": 4,"video": 0}, mm_proce...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: ```image_grid_thw``` not set in ```CachedRequestState``` - ```Qwen2.5 VL 3B``` bug;stale ### Your current environment ### 🐛 Describe the bug When initializing Qwen2.5 VL 3B, cached request does not set the ``` mm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: ```image_grid_thw``` not set in ```CachedRequestState``` - ```Qwen2.5 VL 3B``` bug;stale ### Your current environment ### 🐛 Describe the bug When initializing Qwen2.5 VL 3B, cached request does not set the ``` mm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: puts in all_outputs for output in outputs.outputs] ``` A workaround (specific to my case) is to manually override the image_grid_thw in ```gpu_model_runner.py```, line 350, in this way: ``` if self.uses_mrope: # image_g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: al_vlm;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
