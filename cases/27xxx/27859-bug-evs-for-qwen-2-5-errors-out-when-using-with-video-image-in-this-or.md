# vllm-project/vllm#27859: [Bug]: EVS for Qwen 2_5 Errors out when using with video + image in this order

| 字段 | 值 |
| --- | --- |
| Issue | [#27859](https://github.com/vllm-project/vllm/issues/27859) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EVS for Qwen 2_5 Errors out when using with video + image in this order

### Issue 正文摘录

### 🐛 Describe the bug The new EVS pruner updates prompt place holders to pruned tokens. This is used to erroneously calculate the intial mrope positions. Example if request has 1 video followed by and image. Prompt gets rewritten with pruned video token count (say 4 instead of 8) **_vl_get_input_positions_tensor** is called First iteration: finds video, uses video_grid_thw[0] which says 8 cells Line 1015 advances: st = ed + 8 (full grid) But the prompt only has 4 video tokens, so st overshoots Second iteration: tries to find image token starting from overshot position Search fails → both ed_image and ed_video become len(input_tokens) + 1 Condition ed_image < ed_video is FALSE Goes to video branch → tries image_grid_thw[image_index] but should be looking at images! While we recompute the mrope the code fails at `_vl_get_input_positions_tensor` never reaching the recompute_mrope ### Your current environment ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: for Qwen 2_5 Errors out when using with video + image in this order bug;stale ### 🐛 Describe the bug The new EVS pruner updates prompt place holders to pruned tokens. This is used to erroneously calculate the intial mro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d iteration: tries to find image token starting from overshot position Search fails → both ed_image and ed_video become len(input_tokens) + 1 Condition ed_image < ed_video is FALSE Goes to video branch → tries image_gri...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: EVS for Qwen 2_5 Errors out when using with video + image in this order bug;stale ### 🐛 Describe the bug The new EVS pruner updates prompt place holders to pruned tokens. This is used to erroneously calculate the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency 🐛 Describe the bug

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
