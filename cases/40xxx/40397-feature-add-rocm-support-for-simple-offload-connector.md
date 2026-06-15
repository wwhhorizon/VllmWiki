# vllm-project/vllm#40397: [Feature]: Add ROCm support for simple offload connector

| 字段 | 值 |
| --- | --- |
| Issue | [#40397](https://github.com/vllm-project/vllm/issues/40397) |
| 状态 | closed |
| 标签 | feature request;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;hardware_porting |
| 子分类 | debug |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Add ROCm support for simple offload connector

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, `SimpleCPUOffloadConnector` path requires CUDA. Support should be added for ROCm as well. ### Alternatives _No response_ ### Additional context Stack trace when launching with simple offload connector w/ ROCm (MI355X): [error.txt](https://github.com/user-attachments/files/26908929/error.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Add ROCm support for simple offload connector feature request;rocm ### 🚀 The feature, motivation and pitch Currently, `SimpleCPUOffloadConnector` path requires CUDA. Support should be added for ROCm as well....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Add ROCm support for simple offload connector feature request;rocm ### 🚀 The feature, motivation and pitch Currently, `SimpleCPUOffloadConnector` path requires CUDA. Support should be added for ROCm as well....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add ROCm support for simple offload connector feature request;rocm ### 🚀 The feature, motivation and pitch Currently, `SimpleCPUOffloadConnector` path requires CUDA. Support should be added for ROCm as well....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development frontend_api;hardware_porting cuda 🚀 The feature, motivation and pitch

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
