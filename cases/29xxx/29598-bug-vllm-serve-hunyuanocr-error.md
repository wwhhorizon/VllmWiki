# vllm-project/vllm#29598: [Bug]: vllm serve HunYuanOCR error

| 字段 | 值 |
| --- | --- |
| Issue | [#29598](https://github.com/vllm-project/vllm/issues/29598) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve HunYuanOCR error

### Issue 正文摘录

### Your current environment docker：vllm/vllm-openai:nightly vllm version：0.11.2.dev296+gd9d342d21.cu129 GPU：2080Ti * 4 cuda：13.0 ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: vllm serve HunYuanOCR error bug ### Your current environment docker：vllm/vllm-openai:nightly vllm version：0.11.2.dev296+gd9d342d21.cu129 GPU：2080Ti * 4 cuda：13.0 ### 🐛 Describe the bug ### Before submitting a new...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: penai:nightly vllm version：0.11.2.dev296+gd9d342d21.cu129 GPU：2080Ti * 4 cuda：13.0 ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
