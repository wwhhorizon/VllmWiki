# vllm-project/vllm#21488: [Feature]: torch >2.7.0 support

| 字段 | 值 |
| --- | --- |
| Issue | [#21488](https://github.com/vllm-project/vllm/issues/21488) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: torch >2.7.0 support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch NVIDIA GeForce RTX 5070 with CUDA capability sm_120 is not compatible with the current PyTorch installation. The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90. ”pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128“ can solve this problem,but vllm requires torch==2.7.0. This pip command will insatll torch2.9.0. How can I sovle this problem. I need run vllm on my Ubuntu22.04 with two cards of ”RTX 5070“. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: re request;stale ### 🚀 The feature, motivation and pitch NVIDIA GeForce RTX 5070 with CUDA capability sm_120 is not compatible with the current PyTorch installation. The current PyTorch install supports CUDA capabilitie...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 0 with CUDA capability sm_120 is not compatible with the current PyTorch installation. The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90. ”pip3 install --pre torch torchvis...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: torch >2.7.0 support feature request;stale ### 🚀 The feature, motivation and pitch NVIDIA GeForce RTX 5070 with CUDA capability sm_120 is not compatible with the current PyTorch installation. The current PyTo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development frontend_api cuda env_dependency 🚀 The feature, motivation and pitch

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
