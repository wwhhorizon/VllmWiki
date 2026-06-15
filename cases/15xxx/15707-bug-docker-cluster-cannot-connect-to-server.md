# vllm-project/vllm#15707: [Bug]: docker cluster cannot connect to server

| 字段 | 值 |
| --- | --- |
| Issue | [#15707](https://github.com/vllm-project/vllm/issues/15707) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: docker cluster cannot connect to server

### Issue 正文摘录

### Your current environment ubuntu 24.04, cuda 12.4, docker 28.04, vllm/vllm-openai:latest ### 🐛 Describe the bug Following instructions from https://docs.vllm.ai/en/latest/serving/distributed_serving.html ray status ![Image](https://github.com/user-attachments/assets/3a9e0d87-1d01-47f6-87f0-c60c28393d27) docker ps -a ![Image](https://github.com/user-attachments/assets/2b2c183b-e3d3-4c8f-b68c-f45f92a4e581) Got error failed to connect, ufw already opened 8000 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: docker cluster cannot connect to server bug ### Your current environment ubuntu 24.04, cuda 12.4, docker 28.04, vllm/vllm-openai:latest ### 🐛 Describe the bug Following instructions from https://docs.vllm.ai/en/l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cannot connect to server bug ### Your current environment ubuntu 24.04, cuda 12.4, docker 28.04, vllm/vllm-openai:latest ### 🐛 Describe the bug Following instructions from https://docs.vllm.ai/en/latest/serving/distribu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: t environment ubuntu 24.04, cuda 12.4, docker 28.04, vllm/vllm-openai:latest ### 🐛 Describe the bug Following instructions from https://docs.vllm.ai/en/latest/serving/distributed_serving.html ray status ![Image](https:/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
