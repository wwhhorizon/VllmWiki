# vllm-project/vllm#26387: [Feature]: vllm-flash-attn cutlass support for blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#26387](https://github.com/vllm-project/vllm/issues/26387) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;gemm_linear;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel |
| 症状 |  |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: vllm-flash-attn cutlass support for blackwell

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi team, The main flash-attention repository recently introduced a CUTLASS-based implementation optimized for NVIDIA B200 GPUs (see issue [#1741](https://github.com/Dao-AILab/flash-attention/issues/1741) and the interface in [flash_attn/cute/interface.py](https://github.com/Dao-AILab/flash-attention/blob/main/flash_attn/cute/interface.py)). From my experience, the CUTLASS attention kernel runs about 3.6× faster than the standard implementation on B200 for large-sequence workloads. This is a significant improvement that could greatly benefit vLLM users if integrated into vllm-flash-attn. I’d like to ask: - Are there any plans to bring the CUTLASS backend into vllm-flash-attn for B200 support? - What’s the recommended way to track version alignment between vllm-flash-attn and the upstream flash-attn (e.g., specific commit reference, release tag, or changelog)? Having this information would make it easier for users to verify which kernel optimizations are available in their vLLM builds and avoid confusion about performance differences. Thanks for all your great work — both flash-attn and vllm-flash-attn have been essential for efficient LLM inf...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Feature]: vllm-flash-attn cutlass support for blackwell feature request;stale ### 🚀 The feature, motivation and pitch Hi team, The main flash-attention repository recently introduced a CUTLASS-based implementation opti...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vllm-flash-attn for B200 support? - What’s the recommended way to track version alignment between vllm-flash-attn and the upstream flash-attn (e.g., specific commit reference, release tag, or changelog)? Having this inf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: vllm-flash-attn cutlass support for blackwell feature request;stale ### 🚀 The feature, motivation and pitch Hi team, The main flash-attention repository recently introduced a CUTLASS-based implementation opti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: vllm-flash-attn cutlass support for blackwell feature request;stale ### 🚀 The feature, motivation and pitch Hi team, The main flash-attention repository recently introduced a CUTLASS-based implementation opti...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e;frontend_api;gemm_linear;hardware_porting attention;cuda;kernel memory_layout 🚀 The feature, motivation and pitch

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
