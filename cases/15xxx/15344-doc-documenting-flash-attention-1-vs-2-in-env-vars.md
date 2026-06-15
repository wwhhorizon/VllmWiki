# vllm-project/vllm#15344: [Doc]: documenting flash attention 1 vs 2 in env vars

| 字段 | 值 |
| --- | --- |
| Issue | [#15344](https://github.com/vllm-project/vllm/issues/15344) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: documenting flash attention 1 vs 2 in env vars

### Issue 正文摘录

### 📚 The doc issue Looking at https://docs.vllm.ai/en/latest/serving/env_vars.html for `VLLM_ATTENTION_BACKEND`: > - "FLASH_ATTN": use FlashAttention This leaves me wondering if it's flash attention 1 or 2. ### Suggest a potential alternative/fix Appending this description with a 1 or 2, such as: > - "FLASH_ATTN": use FlashAttention-2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Doc]: documenting flash attention 1 vs 2 in env vars documentation ### 📚 The doc issue Looking at https://docs.vllm.ai/en/latest/serving/env_vars.html for `VLLM_ATTENTION_BACKEND`: > - "FLASH_ATTN": use FlashAttention...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n-2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: documentation ### 📚 The doc issue Looking at https://docs.vllm.ai/en/latest/serving/env_vars.html for `VLLM_ATTENTION_BACKEND`: > - "FLASH_ATTN": use FlashAttention This leaves me wondering if it's flash attention 1 or...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
