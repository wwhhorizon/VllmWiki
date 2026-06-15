# vllm-project/vllm#25970: [Bug]: Model Executor for Qwen2.5Omni incorrectly handles cached prompts with multimodal data.

| 字段 | 值 |
| --- | --- |
| Issue | [#25970](https://github.com/vllm-project/vllm/issues/25970) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model Executor for Qwen2.5Omni incorrectly handles cached prompts with multimodal data.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Qwen2_5_omni_thinker model executor crashes with cached prompt. It seems to be because the maybe_apply_prompt_updates override for qwen2.5 omni indexes into the per_item mm_kwargs, and the multimodal cache logic intentionally returns None objects for the multimodal items. ```python prompt = (" ") empty_image = Image.new("RGB", (224, 224), (0, 0, 0)) model = LLM(model="Qwen/Qwen2.5-Omni-7B", enforce_eager=True) inputs = [ { "prompt": prompt, "multi_modal_data": { "video": [empty_image], } } ] generation = model.generate(inputs) generation = model.generate(inputs) ``` ``` (EngineCore_DP0 pid=265514) INFO 09-30 17:23:14 [default_loader.py:268] Loading weights took 5.44 seconds (EngineCore_DP0 pid=265514) INFO 09-30 17:23:14 [gpu_model_runner.py:2392] Model loading took 16.7371 GiB and 6.042051 seconds (EngineCore_DP0 pid=265514) INFO 09-30 17:23:15 [gpu_model_runner.py:3000] Encoder cache will be initialized with a budget of 32768 tokens, and profiled with 1 video items of the maximum feature size. (EngineCore_DP0 pid=265514) INFO 09-30 17:23:19 [gpu_worker.py:298] Available KV cache memory: 17.33 GiB (EngineCore_DP0 pid=265514) INF...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Model Executor for Qwen2.5Omni incorrectly handles cached prompts with multimodal data. bug ### Your current environment ### 🐛 Describe the bug Qwen2_5_omni_thinker model executor crashes with cached prompt. It s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cache;cuda;operator;...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: neCore_DP0 pid=265514) INFO 09-30 17:23:19 [gpu_worker.py:298] Available KV cache memory: 17.33 GiB (EngineCore_DP0 pid=265514) INFO 09-30 17:23:19 [kv_cache_utils.py:864] GPU KV cache size: 324,496 tokens (EngineCore_D...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: :23:19 [kv_cache_utils.py:868] Maximum concurrency for 32,768 tokens per request: 9.90x (EngineCore_DP0 pid=265514) INFO 09-30 17:23:19 [gpu_worker.py:391] Free memory on device (39.0/39.49 GiB) on startup. Desired GPU...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: GiB for peak activation, 0.02 GiB for non-torch memory, and 0.0 GiB for CUDAGraph memory. Replace gpu_memory_utilization config with `--kv-cache-memory=18451204915` to fit into requested memory, or `--kv-cache-memory=22...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
