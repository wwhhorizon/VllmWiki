# vllm-project/vllm#19252: [Bug]: Support Qwen3 Reranker

| 字段 | 值 |
| --- | --- |
| Issue | [#19252](https://github.com/vllm-project/vllm/issues/19252) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Support Qwen3 Reranker

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/2006ab4d-b9c2-4f60-8814-f02ea41ba9be) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: be) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Support Qwen3 Reranker bug ### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/2006ab4d-b9c2-4f60-8814-f02ea41ba9be) ### Before submitting a new issue... - [x]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
