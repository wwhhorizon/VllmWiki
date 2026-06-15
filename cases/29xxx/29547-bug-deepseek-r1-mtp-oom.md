# vllm-project/vllm#29547: [Bug]: DeepSeek R1 + MTP OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#29547](https://github.com/vllm-project/vllm/issues/29547) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek R1 + MTP OOM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Attempting to load DeepSeek R1 with MTP causes an OOM on 8xH200 (which should be able to run this without issue). I was able to reproduce this on two different machines. ``` vllm serve deepseek-ai/DeepSeek-R1 \ --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}' \ -dp 8 \ --enable-expert-parallel ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: n 8xH200 (which should be able to run this without issue). I was able to reproduce this on two different machines. ``` vllm serve deepseek-ai/DeepSeek-R1 \ --speculative-config '{"method": "mtp", "num_speculative_tokens...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: DeepSeek R1 + MTP OOM bug ### Your current environment ### 🐛 Describe the bug Attempting to load DeepSeek R1 with MTP causes an OOM on 8xH200 (which should be able to run this without issue). I was able to reprod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nt machines. ``` vllm serve deepseek-ai/DeepSeek-R1 \ --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}' \ -dp 8 \ --enable-expert-parallel ``` ### Before submitting a new issue... - [x] Make sure you...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: method": "mtp", "num_speculative_tokens": 1}' \ -dp 8 \ --enable-expert-parallel ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
