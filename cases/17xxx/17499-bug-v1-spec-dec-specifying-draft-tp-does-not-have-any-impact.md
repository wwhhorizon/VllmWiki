# vllm-project/vllm#17499: [Bug]: [v1][Spec Dec] Specifying draft TP does not have any impact.

| 字段 | 值 |
| --- | --- |
| Issue | [#17499](https://github.com/vllm-project/vllm/issues/17499) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [v1][Spec Dec] Specifying draft TP does not have any impact.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is more of a confusion than a bug. Currently, for EAGLE implementation in V1, draft TP will always be the same as target TP, no matter what value the user specifies. For V0, we currently support draft TP = 1 or target TP, where draft TP=1 was originally used for small standalone draft models. For v1, we only have EAGLE support, which probably doesn't benefit from draft TP = 1. So not sure what's the best thing to do here. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: [v1][Spec Dec] Specifying draft TP does not have any impact. bug;stale ### Your current environment ### 🐛 Describe the bug This is more of a confusion than a bug. Currently, for EAGLE implementation in V1, draft...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: port draft TP = 1 or target TP, where draft TP=1 was originally used for small standalone draft models. For v1, we only have EAGLE support, which probably doesn't benefit from draft TP = 1. So not sure what's the best t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: [v1][Spec Dec] Specifying draft TP does not have any impact. bug;stale ### Your current environment ### 🐛 Describe the bug This is more of a confusion than a bug. Currently, for EAGLE implementation in V1, draft...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current envir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
