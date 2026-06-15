# vllm-project/vllm#16267: [Bug]: Not supporting CUDA12.8

| 字段 | 值 |
| --- | --- |
| Issue | [#16267](https://github.com/vllm-project/vllm/issues/16267) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Not supporting CUDA12.8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 目前5090d、5070ti显卡的驱动最低都是cuda12.8，但是vllm主要是12.4，vllm使用cuda12.8报错 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Not supporting CUDA12.8 bug ### Your current environment ### 🐛 Describe the bug 目前5090d、5070ti显卡的驱动最低都是cuda12.8，但是vllm主要是12.4，vllm使用cuda12.8报错 ### Before submitting a new issue... - [x] Make sure you already sear...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: an answer lots of frequently asked questions. development cuda crash env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development cuda crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
