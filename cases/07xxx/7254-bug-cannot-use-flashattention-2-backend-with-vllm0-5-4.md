# vllm-project/vllm#7254: [Bug]: Cannot use FlashAttention-2 backend with vllm0.5.4

| 字段 | 值 |
| --- | --- |
| Issue | [#7254](https://github.com/vllm-project/vllm/issues/7254) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot use FlashAttention-2 backend with vllm0.5.4

### Issue 正文摘录

### Your current environment ```text ubuntu20.04+python3.10.14+cuda11.8+cudnn8.9.6+A100 vllm==0.5.4 torch==2.4.0+cu118 transformers==4.44.0 flash-attn == 2.6.1 vllm-flash-attn == 2.6.1 Cannot use FlashAttention-2 backend because the vllm_flash_attn package is not found. pip install vllm-flash-attn for better performance. INFO 08-07 15:31:39 selector.py:54] Using XFormers backend. import flash_attn successful ``` ### 🐛 Describe the bug INFO 08-07 16:06:47 selector.py:189] Cannot use FlashAttention-2 backend because the vllm_flash_attn package is not found. `pip install vllm-flash-attn` for better performance. INFO 08-07 16:06:47 selector.py:54] Using XFormers backend.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ttention-2 backend because the vllm_flash_attn package is not found. pip install vllm-flash-attn for better performance. INFO 08-07 15:31:39 selector.py:54] Using XFormers backend. import flash_attn successful ``` ### 🐛...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Cannot use FlashAttention-2 backend with vllm0.5.4 bug ### Your current environment ```text ubuntu20.04+python3.10.14+cuda11.8+cudnn8.9.6+A100 vllm==0.5.4 torch==2.4.0+cu118 transformers==4.44.0 flash-attn == 2.6...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .5.4 bug ### Your current environment ```text ubuntu20.04+python3.10.14+cuda11.8+cudnn8.9.6+A100 vllm==0.5.4 torch==2.4.0+cu118 transformers==4.44.0 flash-attn == 2.6.1 vllm-flash-attn == 2.6.1 Cannot use FlashAttention...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
