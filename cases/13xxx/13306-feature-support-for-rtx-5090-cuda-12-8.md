# vllm-project/vllm#13306: [Feature]: Support for RTX 5090 (CUDA 12.8)

| 字段 | 值 |
| --- | --- |
| Issue | [#13306](https://github.com/vllm-project/vllm/issues/13306) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;hardware_porting |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support for RTX 5090 (CUDA 12.8)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently only nightlies from torch targeting 12.8 support blackwell such as the rtx 5090. I tried using VLLM with a rtx 5090 and no dice. Vanilla vllm installation ends in: ``` NVIDIA GeForce RTX 5090 with CUDA capability sm_120 is not compatible with the current PyTorch installation. The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90. If you want to use the NVIDIA GeForce RTX 5090 GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/ RuntimeError: CUDA error: no kernel image is available for execution on the device ``` Thanks ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Feature]: Support for RTX 5090 (CUDA 12.8) feature request ### 🚀 The feature, motivation and pitch Currently only nightlies from torch targeting 12.8 support blackwell such as the rtx 5090. I tried using VLLM with a rt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e rtx 5090. I tried using VLLM with a rtx 5090 and no dice. Vanilla vllm installation ends in: ``` NVIDIA GeForce RTX 5090 with CUDA capability sm_120 is not compatible with the current PyTorch installation. The current...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support for RTX 5090 (CUDA 12.8) feature request ### 🚀 The feature, motivation and pitch Currently only nightlies from torch targeting 12.8 support blackwell such as the rtx 5090. I tried using VLLM with a rt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development frontend_api;hardware_porting cuda;kernel env_dependency 🚀 The feature, m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
