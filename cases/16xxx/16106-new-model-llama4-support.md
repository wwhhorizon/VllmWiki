# vllm-project/vllm#16106: [New Model]: Llama4 Support

| 字段 | 值 |
| --- | --- |
| Issue | [#16106](https://github.com/vllm-project/vllm/issues/16106) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Llama4 Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Meta released 2 Variants: Llama 4 Scout: A high-performing small model with 17B activated parameters across 16 experts. Extremely fast, natively multimodal, supports a 10M+ token context window, and runs on a single GPU. Llama 4 Maverick: A top-tier multimodal model outperforming GPT-4o and Gemini 2.0 Flash, with performance on par with DeepSeek V3 at half the active parameters. ELO 1417 on LMArena and runs on a single host. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Llama4 Support new-model ### 🚀 The feature, motivation and pitch Meta released 2 Variants: Llama 4 Scout: A high-performing small model with 17B activated parameters across 16 experts. Extremely fast, nativ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n and pitch Meta released 2 Variants: Llama 4 Scout: A high-performing small model with 17B activated parameters across 16 experts. Extremely fast, natively multimodal, supports a 10M+ token context window, and runs on...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: t: A high-performing small model with 17B activated parameters across 16 experts. Extremely fast, natively multimodal, supports a 10M+ token context window, and runs on a single GPU. Llama 4 Maverick: A top-tier multimo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
