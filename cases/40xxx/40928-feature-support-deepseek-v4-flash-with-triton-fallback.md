# vllm-project/vllm#40928: [Feature]: Support DeepSeek V4 flash with Triton fallback

| 字段 | 值 |
| --- | --- |
| Issue | [#40928](https://github.com/vllm-project/vllm/issues/40928) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | kernel;triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support DeepSeek V4 flash with Triton fallback

### Issue 正文摘录

### 🚀 The feature, motivation and pitch # Support DeepSeek V4 on SM120 ## 🚀 The feature, motivation and pitch I am trying to run DeepSeek V4 / DeepSeek-V4-Flash on NVIDIA SM120 GPUs. Currently, the DeepSeek V4 path depends on optimized kernels such as DeepGEMM and FlashMLA, but these kernels do not appear to support SM120 yet. Because of this, DeepSeek V4 cannot run on SM120 even though the GPUs have enough memory and compute capability for the model. It would be very helpful if vLLM could support DeepSeek V4 on SM120, or provide a compatible execution path when DeepGEMM / FlashMLA are unavailable for this architecture. SM120 GPUs are becoming available in workstation and server environments, so supporting this architecture would make DeepSeek V4 usable on newer NVIDIA hardware. ## Alternatives The current alternatives seem to be: - Use GPU architectures already supported by DeepGEMM / FlashMLA. - Wait for DeepGEMM / FlashMLA to add SM120 support. - Maintain a local patch to bypass unsupported kernel paths. I am not sure whether SM120 support is currently planned for DeepSeek V4 in vLLM. ## Additional context Environment: - GPU: NVIDIA RTX PRO 6000 96GB x 2 - GPU architecture: SM1...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: equest ### 🚀 The feature, motivation and pitch # Support DeepSeek V4 on SM120 ## 🚀 The feature, motivation and pitch I am trying to run DeepSeek V4 / DeepSeek-V4-Flash on NVIDIA SM120 GPUs. Currently, the DeepSeek V4 pa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Feature]: Support DeepSeek V4 flash with Triton fallback feature request ### 🚀 The feature, motivation and pitch # Support DeepSeek V4 on SM120 ## 🚀 The feature, motivation and pitch I am trying to run DeepSeek V4 / De...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 0 even though the GPUs have enough memory and compute capability for the model. It would be very helpful if vLLM could support DeepSeek V4 on SM120, or provide a compatible execution path when DeepGEMM / FlashMLA are un...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Currently, the DeepSeek V4 path depends on optimized kernels such as DeepGEMM and FlashMLA, but these kernels do not appear to support SM120 yet. Because of this, DeepSeek V4 cannot run on SM120 even though the GPUs hav...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support DeepSeek V4 flash with Triton fallback feature request ### 🚀 The feature, motivation and pitch # Support DeepSeek V4 on SM120 ## 🚀 The feature, motivation and pitch I am trying to run DeepSeek V4 / De...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
