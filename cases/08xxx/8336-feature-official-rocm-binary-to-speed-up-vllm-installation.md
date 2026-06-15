# vllm-project/vllm#8336: [Feature]: Official ROCm Binary to Speed Up vLLM Installation

| 字段 | 值 |
| --- | --- |
| Issue | [#8336](https://github.com/vllm-project/vllm/issues/8336) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Official ROCm Binary to Speed Up vLLM Installation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The current installation process for vLLM on AMD devices presents significant challenges in terms of installation time: 1. The ROCm Docker image is exceptionally large (22GB compressed), leading to download times exceeding 15 minutes. 2. Building vLLM from source takes more than 10 minutes to complete due to time consumed in compilation. In contrast, for CUDA users, a pip installation is available, streamlining the process significantly. To improve the installation experience for ROCm users, I propose introducing an official pre-built binary that can be distributed via pip. ### Alternatives Currently, to speed up deployments, we have created our own `binary` for ROCm with vLLM, which reduces the entire setup process to about `2-3 minutes`. It would be really helpful to have an official pre-built binary for ROCm to streamline this process. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature]: Official ROCm Binary to Speed Up vLLM Installation feature request;stale ### 🚀 The feature, motivation and pitch The current installation process for vLLM on AMD devices presents significant challenges in ter...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Official ROCm Binary to Speed Up vLLM Installation feature request;stale ### 🚀 The feature, motivation and pitch The current installation process for vLLM on AMD devices presents significant challenges in ter...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Official ROCm Binary to Speed Up vLLM Installation feature request;stale ### 🚀 The feature, motivation and pitch The current installation process for vLLM on AMD devices presents significant challenges in ter...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting cuda build_er...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
