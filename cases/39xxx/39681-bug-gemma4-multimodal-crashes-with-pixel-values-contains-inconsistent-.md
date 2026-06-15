# vllm-project/vllm#39681: [Bug]: Gemma4 multimodal crashes with "pixel_values contains inconsistent shapes" when concurrent image requests have different resolutions

| 字段 | 值 |
| --- | --- |
| Issue | [#39681](https://github.com/vllm-project/vllm/issues/39681) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4 multimodal crashes with "pixel_values contains inconsistent shapes" when concurrent image requests have different resolutions

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When two or more concurrent chat-completion requests containing images of **different resolutions** land in the same scheduler step, Gemma4's multimodal encoder co-batches them and crashes during input validation. The error takes down all TP workers and the engine core; the server stops serving requests. ValueError: pixel_values contains inconsistent shapes: torch.Size([10080, 768]) (index 0) vs torch.Size([2520, 768]) (index 1) ### Root cause (brief) The Gemma4 HF image processor sizes `pixel_values` per image as `(max_patches, patch_pixels)` where `max_patches = max_soft_tokens × pooling_kernel_size²`, and `max_soft_tokens` depends on image resolution. Different images therefore get different `max_patches` (e.g. 10080 vs 2520). `Gemma4ImagePixelInputs` declares `pixel_values` with a uniform `("bn", "np", "pp")` shape (https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma4_mm.py#L92-L112), so when `_execute_mm_encoder` stacks images from different requests, the `TensorSchema` validator rejects the mismatched `np` dim. Note that [`_process_image_input`](https://github.com/vllm-project/vllm/blob/main/vllm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Gemma4 multimodal crashes with "pixel_values contains inconsistent shapes" when concurrent image requests have different resolutions bug ### Your current environment ### 🐛 Describe the bug When two or more concur...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: the schema/stacking layer enforces uniformity (the TODO at line 1049 anticipates this). ### Reproduction Server (the exact `docker run` I used): ```bash docker run -itd --gpus '"device=4,5,6,7"' --name vllm-gemma-4-31b-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: s with "pixel_values contains inconsistent shapes" when concurrent image requests have different resolutions bug ### Your current environment ### 🐛 Describe the bug When two or more concurrent chat-completion requests c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ages from different requests, the `TensorSchema` validator rejects the mismatched `np` dim. Note that [`_process_image_input`](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma4_mm.py#L1063...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: images from different requests, the `TensorSchema` validator rejects the mismatched `np` dim. Note that [`_process_image_input`](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma4_mm.py#L10...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
