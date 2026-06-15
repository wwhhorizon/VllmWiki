# vllm-project/vllm#15096: [Bug]: The vllm 0.8.0 deployed using Docker does not support gemma3

| 字段 | 值 |
| --- | --- |
| Issue | [#15096](https://github.com/vllm-project/vllm/issues/15096) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The vllm 0.8.0 deployed using Docker does not support gemma3

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/e801a5e4-aab6-4e5c-b77d-5db8aa3ec093) ### 🐛 Describe the bug The vllm 0.8.0 deployed by Docker does not support gemma3 as shown in the figure. ![Image](https://github.com/user-attachments/assets/1aba26b6-d7ab-4a98-88a9-9fa8dbf5f91a) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: The vllm 0.8.0 deployed using Docker does not support gemma3 bug ### Your current environment ![Image](https://github.com/user-attachments/assets/e801a5e4-aab6-4e5c-b77d-5db8aa3ec093) ### 🐛 Describe the bug The v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 1a) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: The vllm 0.8.0 deployed using Docker does not support gemma3 bug ### Your current environment ![Image](https://github.com/user-attachments/assets/e801a5e4-aab6-4e5c-b77d-5db8aa3ec093) ### 🐛 Describe the bug The v...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: The vllm 0.8.0 deployed using Docker does not support gemma3 bug ### Your current environment ![Image](https://github.com/user-attachments/assets/e801a5e4-aab6-4e5c-b77d-5db8aa3ec093) ### 🐛 Describe the bug The v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
