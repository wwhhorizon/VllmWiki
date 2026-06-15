# vllm-project/vllm#17442: [Bug]: V1 + FLASH_ATTN V3 + FP8 kv-cache randomly crashes w/qwen3 (and other models)

| 字段 | 值 |
| --- | --- |
| Issue | [#17442](https://github.com/vllm-project/vllm/issues/17442) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 + FLASH_ATTN V3 + FP8 kv-cache randomly crashes w/qwen3 (and other models)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Title. FLASHINFER does not seem to have the same issues, but that also means I can't use an FP8 kv cache. My current arguments: Here's the log: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: V1 + FLASH_ATTN V3 + FP8 kv-cache randomly crashes w/qwen3 (and other models) bug ### Your current environment ### 🐛 Describe the bug Title. FLASHINFER does not seem to have the same issues, but that also means I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: V1 + FLASH_ATTN V3 + FP8 kv-cache randomly crashes w/qwen3 (and other models) bug ### Your current environment ### 🐛 Describe the bug Title. FLASHINFER does not seem to have the same issues, but that also means I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: V1 + FLASH_ATTN V3 + FP8 kv-cache randomly crashes w/qwen3 (and other models) bug ### Your current environment ### 🐛 Describe the bug Title. FLASHINFER does not seem to have the same issues, but that also means I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: els) bug ### Your current environment ### 🐛 Describe the bug Title. FLASHINFER does not seem to have the same issues, but that also means I can't use an FP8 kv cache. My current arguments: Here's the log: ### Before sub...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
