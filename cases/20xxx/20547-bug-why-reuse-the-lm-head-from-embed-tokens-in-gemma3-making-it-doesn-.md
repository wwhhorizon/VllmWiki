# vllm-project/vllm#20547: [Bug]: why reuse the lm_head from embed_tokens in gemma3? Making it doesn't work for GRPO Training.

| 字段 | 值 |
| --- | --- |
| Issue | [#20547](https://github.com/vllm-project/vllm/issues/20547) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: why reuse the lm_head from embed_tokens in gemma3? Making it doesn't work for GRPO Training.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I try to use VLLM and GRPOTrainer to train the medgemma model. But my checkpoint only output correctly in VLLM inference, failed to infer in normal transformers' code without VLLM. After I check the code in VLLM, I found that the lm_head is reused by gemma3ForCausalLM model. So the final lm_head isn't used in vllm inference but used in transformers' code. That a inconsistant between transformers and vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: why reuse the lm_head from embed_tokens in gemma3? Making it doesn't work for GRPO Training. bug ### Your current environment ### 🐛 Describe the bug I try to use VLLM and GRPOTrainer to train the medgemma model....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: why reuse the lm_head from embed_tokens in gemma3? Making it doesn't work for GRPO Training. bug ### Your current environment ### 🐛 Describe the bug I try to use VLLM and GRPOTrainer to train the medgemma model....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
