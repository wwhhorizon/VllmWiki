# vllm-project/vllm#7593: [Bug]: Gemma 2 9b errors

| 字段 | 值 |
| --- | --- |
| Issue | [#7593](https://github.com/vllm-project/vllm/issues/7593) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 2 9b errors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Cannot run gemma 2 9b it with rope scaling. ``` NotImplementedError: Disabling sliding window is not supported for models with rope_scaling. Please raise an issue so we can investigate. ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: raise an issue so we can investigate. ``` correctness attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma 2 9b errors bug;stale ### Your current environment ### 🐛 Describe the bug Cannot run gemma 2 9b it with rope scaling. ``` NotImplementedError: Disabling sliding window is not supported for models with rope_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Gemma 2 9b errors bug;stale ### Your current environment ### 🐛 Describe the bug Cannot run gemma 2 9b it with rope scaling. ``` NotImplementedError: Disabling sliding window is not supported for models with rope_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
