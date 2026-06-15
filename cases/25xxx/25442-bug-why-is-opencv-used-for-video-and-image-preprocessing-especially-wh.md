# vllm-project/vllm#25442: [Bug]: Why is OpenCV used for video and image preprocessing? Especially when it comes to processing videos, the efficiency is too low. I want to modify this part to torchvision parallel computing. Where should I start?

| 字段 | 值 |
| --- | --- |
| Issue | [#25442](https://github.com/vllm-project/vllm/issues/25442) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Why is OpenCV used for video and image preprocessing? Especially when it comes to processing videos, the efficiency is too low. I want to modify this part to torchvision parallel computing. Where should I start?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Why is OpenCV used for video and image preprocessing? Especially when it comes to processing videos, the efficiency is too low. I want to modify this part to torchvision parallel computing. Where should I start? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Why is OpenCV used for video and image preprocessing? Especially when it comes to processing videos, the efficiency is too low. I want to modify this part to torchvision parallel computing. Where should I start?...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rt? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
