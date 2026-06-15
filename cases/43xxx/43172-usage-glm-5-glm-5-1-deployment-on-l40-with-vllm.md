# vllm-project/vllm#43172: [Usage]: GLM-5/GLM-5.1 deployment on L40 with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#43172](https://github.com/vllm-project/vllm/issues/43172) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;kernel;operator |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: GLM-5/GLM-5.1 deployment on L40 with vLLM

### Issue 正文摘录

### Your current environment Hi, I'm trying to evaluate the deployment of GLM-5/GLM-5.1 on an NVIDIA L40 (48GB VRAM). but I'm hitting an "Operator Unsupported" error. ``` ValueError: No valid attention backend found for cuda... Reasons: {FLASH_ATTN_MLA: [compute capability not supported], FLASHMLA: [compute capability not supported... only supported on Hopper and Blackwell devices.]} ``` Is this model fully compatible with L40 currently? If so, are there any known workarounds or specific setup steps for this GPU architecture to fix the kernel issue? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nsupported" error. ``` ValueError: No valid attention backend found for cuda... Reasons: {FLASH_ATTN_MLA: [compute capability not supported], FLASHMLA: [compute capability not supported... only supported on Hopper and B...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: patible with L40 currently? If so, are there any known workarounds or specific setup steps for this GPU architecture to fix the kernel issue? ### How would you like to use vllm I want to run inference of a [specific mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: on L40 with vLLM usage ### Your current environment Hi, I'm trying to evaluate the deployment of GLM-5/GLM-5.1 on an NVIDIA L40 (48GB VRAM). but I'm hitting an "Operator Unsupported" error. ``` ValueError: No valid atte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ing an "Operator Unsupported" error. ``` ValueError: No valid attention backend found for cuda... Reasons: {FLASH_ATTN_MLA: [compute capability not supported], FLASHMLA: [compute capability not supported... only support...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ported... only supported on Hopper and Blackwell devices.]} ``` Is this model fully compatible with L40 currently? If so, are there any known workarounds or specific setup steps for this GPU architecture to fix the kern...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
