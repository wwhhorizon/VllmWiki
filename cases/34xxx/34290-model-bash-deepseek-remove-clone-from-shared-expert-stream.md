# vllm-project/vllm#34290: [Model Bash][DeepSeek]: Remove Clone From Shared Expert Stream

| 字段 | 值 |
| --- | --- |
| Issue | [#34290](https://github.com/vllm-project/vllm/issues/34290) |
| 状态 | closed |
| 标签 | model-bash |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Model Bash][DeepSeek]: Remove Clone From Shared Expert Stream

### Issue 正文摘录

### 🚀 The feature, motivation and pitch - investigate why we need the clone - remove it when we can ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Model Bash][DeepSeek]: Remove Clone From Shared Expert Stream model-bash ### 🚀 The feature, motivation and pitch - investigate why we need the clone - remove it when we can ### Alternatives _No response_ ### Addition
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Model Bash][DeepSeek]: Remove Clone From Shared Expert Stream model-bash ### 🚀 The feature, motivation and pitch - investigate why we need the clone - remove it when we can ### Alternatives _No response_ ### Additional...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
