# vllm-project/vllm#18367: [Feature]: Consolidate AITER env flags

| 字段 | 值 |
| --- | --- |
| Issue | [#18367](https://github.com/vllm-project/vllm/issues/18367) |
| 状态 | closed |
| 标签 | feature request;rocm;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Consolidate AITER env flags

### Issue 正文摘录

### 🚀 The feature, motivation and pitch There is really no need to maintain extensive number of flags for activating AITER kernels from various purpose (usage will become super tedious). Instead of all flags below, we can simply use one `VLLM_ROCM_USE_AITER`, for specific functional kernel, we will always pick its fastest one from AITER. This will simplify usage and testing. VLLM_ROCM_USE_AITER: bool = False VLLM_ROCM_USE_AITER_PAGED_ATTN: bool = False VLLM_ROCM_USE_AITER_LINEAR: bool = True VLLM_ROCM_USE_AITER_MOE: bool = True VLLM_ROCM_USE_AITER_RMSNORM: bool = True VLLM_ROCM_USE_AITER_MLA: bool = True ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Consolidate AITER env flags feature request;rocm;stale ### 🚀 The feature, motivation and pitch There is really no need to maintain extensive number of flags for activating AITER kernels from various purpose (...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Consolidate AITER env flags feature request;rocm;stale ### 🚀 The feature, motivation and pitch There is really no need to maintain extensive number of flags for activating AITER kernels from various purpose (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Consolidate AITER env flags feature request;rocm;stale ### 🚀 The feature, motivation and pitch There is really no need to maintain extensive number of flags for activating AITER kernels from various purpose (...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: of all flags below, we can simply use one `VLLM_ROCM_USE_AITER`, for specific functional kernel, we will always pick its fastest one from AITER. This will simplify usage and testing. VLLM_ROCM_USE_AITER: bool = False VL...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: This will simplify usage and testing. VLLM_ROCM_USE_AITER: bool = False VLLM_ROCM_USE_AITER_PAGED_ATTN: bool = False VLLM_ROCM_USE_AITER_LINEAR: bool = True VLLM_ROCM_USE_AITER_MOE: bool = True VLLM_ROCM_USE_AITER_RMSNO...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
