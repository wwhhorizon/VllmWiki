# vllm-project/vllm#17565: [Bug][V1] 'PixtralVisionConfig' object has no attribute 'spatial_merge_size' in 0.8.5

| 字段 | 值 |
| --- | --- |
| Issue | [#17565](https://github.com/vllm-project/vllm/issues/17565) |
| 状态 | closed |
| 标签 | bug;v1 |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][V1] 'PixtralVisionConfig' object has no attribute 'spatial_merge_size' in 0.8.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With #17270 , `pixtral-community/pixtral-12b` failed. I think what we did in #17270 and other similar places are too hacky: we insert attributes randomly ```shell python ../vllm/examples/offline_inference/vision_language.py -m pixtral_hf ``` output ```text File "~/vllm/vllm/multimodal/processing.py", line 787, in apply_token_matches token_id_seqs = _apply_matches(prompt, mm_matches, mm_item_counts) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "~/vllm/vllm/multimodal/processing.py", line 764, in _apply_matches content = origin.get_content(item_idx) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "~/vllm/vllm/multimodal/processing.py", line 491, in get_content content = content(item_idx) ^^^^^^^^^^^^^^^^^ File "~/vllm/vllm/model_executor/models/llava.py", line 367, in get_replacement ncols, nrows = encoder_info.get_patch_grid_size( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "~/vllm/vllm/model_executor/models/pixtral.py", line 940, in get_patch_grid_size patch_width = patch_height = self.get_patch_size() ^^^^^^^^^^^^^^^^^^^^^ File "~/vllm/vllm/model_executor/models/pixtral.py", line 923, in get_patch_size self.vision_config.spatial_merge_s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug][V1] 'PixtralVisionConfig' object has no attribute 'spatial_merge_size' in 0.8.5 bug;v1 ### Your current environment ### 🐛 Describe the bug With #17270 , `pixtral-community/pixtral-12b` failed. I think what we did...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: d_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
