# vllm-project/vllm#21138: [ROCm]: There is too many opt-in ROCm specific flags

| 字段 | 值 |
| --- | --- |
| Issue | [#21138](https://github.com/vllm-project/vllm/issues/21138) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;frontend_api;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | activation |
| 症状 |  |
| 根因提示 | race_condition |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [ROCm]: There is too many opt-in ROCm specific flags

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It makes sense that new ROCm features are gated behind an opt-in flag but currently there no mechanism to change that opt-in flag to default on and make it an opt-out flag. +viz @qcolombet What this translates to is an explosion of opt in flags that need to be set in order to have reasonable performance. There is a lack of documentation around which flags are needed for which models. ROCm should have a baked in config file which has the best config set for each model where an user can just enable it with `VLLM_ROCM_USE_BEST_CONFIG=1` instead of end users being in an rat race figuring out the best ROCm specific flags. ROCm best_config files for popular models like LLama70B Instruct 3.3 or DeepSeek R1 would be really helpful since these are the most common used models on ROCm Many ROCm end users are not happy about the increasing amount of flags needed to be set to get reasonable performance. For instance, every ROCm documentation says to set `VLLM_USE_TRITON_FLASH_ATTN=0`, `VLLM_USE_TRITON_FLASH_ATTN` should just be set to be `0` by default without explicitly setting it. Before AMD engineer add a new ROCm specific flag, they should apply a ge...

## 现有链接修复摘要

#21366 [ROCm] Auto-Select Attention Backend | #26719 [ROCm][Tools] Add environment variable tuning package for optimized defaults

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [ROCm]: There is too many opt-in ROCm specific flags feature request;stale ### 🚀 The feature, motivation and pitch It makes sense that new ROCm features are gated behind an opt-in flag but currently there no mechanism t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: rformance. For instance, every ROCm documentation says to set `VLLM_USE_TRITON_FLASH_ATTN=0`, `VLLM_USE_TRITON_FLASH_ATTN` should just be set to be `0` by default without explicitly setting it. Before AMD engineer add a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [ROCm]: There is too many opt-in ROCm specific flags feature request;stale ### 🚀 The feature, motivation and pitch It makes sense that new ROCm features are gated behind an opt-in flag but currently there no mechanism to
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: There is a lack of documentation around which flags are needed for which models. ROCm should have a baked in config file which has the best config set for each model where an user can just enable it with `VLLM_ROCM_USE_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [ROCm]: There is too many opt-in ROCm specific flags feature request;stale ### 🚀 The feature, motivation and pitch It makes sense that new ROCm features are gated behind an opt-in flag but currently there no mechanism t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21366](https://github.com/vllm-project/vllm/pull/21366) | mentioned | 0.6 | [ROCm] Auto-Select Attention Backend | kernels on ROCm, has been a pain point for some users as mentioned in #21138. This PR introduces: - Selection of attention backends for ROCm based on priority(performance) and sup… |
| [#26719](https://github.com/vllm-project/vllm/pull/26719) | mentioned | 0.6 | [ROCm][Tools] Add environment variable tuning package for optimized defaults | ent variables and CLI arguments for vLLM on AMD ROCm GPUs. Addresses [#21138](https://github.com/vllm-project/vllm/issues/21138) by eliminating the need to manually configure mult… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
