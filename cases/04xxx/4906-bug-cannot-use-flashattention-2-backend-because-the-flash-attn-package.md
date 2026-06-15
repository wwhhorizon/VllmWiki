# vllm-project/vllm#4906: [Bug]: Cannot use FlashAttention-2 backend because the flash_attn package is not found

| 字段 | 值 |
| --- | --- |
| Issue | [#4906](https://github.com/vllm-project/vllm/issues/4906) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot use FlashAttention-2 backend because the flash_attn package is not found

### Issue 正文摘录

### Your current environment Driver Version: 545.23.08 CUDA Version: 12.3 python3.9 vllm 0.4.2 flash_attn 2.4.2~2.5.8 (I have tried various versions of flash_attn) torch 2.3 ### 🐛 Describe the bug Cannot use FlashAttention-2 backend because the flash_attn package is not found. Please install it for better performance. Using XFormers backend.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: flash_attn package is not found bug ### Your current environment Driver Version: 545.23.08 CUDA Version: 12.3 python3.9 vllm 0.4.2 flash_attn 2.4.2~2.5.8 (I have tried various versions of flash_attn) torch 2.3 ### 🐛 Des...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Cannot use FlashAttention-2 backend because the flash_attn package is not found bug ### Your current environment Driver Version: 545.23.08 CUDA Version: 12.3 python3.9 vllm 0.4.2 flash_attn 2.4.2~2.5.8 (I have tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ot found bug ### Your current environment Driver Version: 545.23.08 CUDA Version: 12.3 python3.9 vllm 0.4.2 flash_attn 2.4.2~2.5.8 (I have tried various versions of flash_attn) torch 2.3 ### 🐛 Describe the bug Cannot us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
