# vllm-project/vllm#41827: [Feature]: Support Deepseek v4 on triton fallback

| 字段 | 值 |
| --- | --- |
| Issue | [#41827](https://github.com/vllm-project/vllm/issues/41827) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | kernel;triton |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support Deepseek v4 on triton fallback

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Ideally, vLLM could provide a generic Triton-based fallback implementation for DeepSeek V4. This would allow unsupported architectures such as SM89/SM120 to run DeepSeek V4 even when highly optimized vendor-specific kernels like DeepGEMM or FlashMLA are unavailable. The goal is not necessarily to match the peak performance of DeepGEMM / FlashMLA, but to provide a portable and compatible execution path across more NVIDIA GPU architectures. I am not sure whether there is broader demand in the community for a generic Triton-based implementation, but I think it could be useful as a compatibility fallback for newer or less commonly supported NVIDIA architectures. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature]: Support Deepseek v4 on triton fallback feature request ### 🚀 The feature, motivation and pitch Ideally, vLLM could provide a generic Triton-based fallback implementation for DeepSeek V4. This would allow unsu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed fallback implementation for DeepSeek V4. This would allow unsupported architectures such as SM89/SM120 to run DeepSeek V4 even when highly optimized vendor-specific kernels like DeepGEMM or FlashMLA are unavailable....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ch as SM89/SM120 to run DeepSeek V4 even when highly optimized vendor-specific kernels like DeepGEMM or FlashMLA are unavailable. The goal is not necessarily to match the peak performance of DeepGEMM / FlashMLA, but to...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: DeepSeek V4 even when highly optimized vendor-specific kernels like DeepGEMM or FlashMLA are unavailable. The goal is not necessarily to match the peak performance of DeepGEMM / FlashMLA, but to provide a portable and c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support Deepseek v4 on triton fallback feature request ### 🚀 The feature, motivation and pitch Ideally, vLLM could provide a generic Triton-based fallback implementation for DeepSeek V4. This would allow unsu...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
