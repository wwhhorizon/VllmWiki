# vllm-project/vllm#10423: [Feature]: Add Support for Specifying Local CUTLASS Source Directory via Environment Variable

| 字段 | 值 |
| --- | --- |
| Issue | [#10423](https://github.com/vllm-project/vllm/issues/10423) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add Support for Specifying Local CUTLASS Source Directory via Environment Variable

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In certain environments where network conditions are poor, or when users wish to compile vllm using a custom version of the CUTLASS code (e.g., with modifications or enhancements), it is currently inconvenient to do so. To address this, we propose introducing a `CUTLASS_SRC_DIR `environment variable, allowing users to configure the local source directory for CUTLASS during the vllm build process, similar to the existing `VLLM_FLASH_ATTN_SRC_DIR`. This enhancement would provide more flexibility and improve usability in diverse development environments. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature]: Add Support for Specifying Local CUTLASS Source Directory via Environment Variable feature request;stale ### 🚀 The feature, motivation and pitch In certain environments where network conditions are poor, or w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ecifying Local CUTLASS Source Directory via Environment Variable feature request;stale ### 🚀 The feature, motivation and pitch In certain environments where network conditions are poor, or when users wish to compile vll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Add Support for Specifying Local CUTLASS Source Directory via Environment Variable feature request;stale ### 🚀 The feature, motivation and pitch In certain environments where network conditions are poor, or w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: introducing a `CUTLASS_SRC_DIR `environment variable, allowing users to configure the local source directory for CUTLASS during the vllm build process, similar to the existing `VLLM_FLASH_ATTN_SRC_DIR`. This enhancement...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
