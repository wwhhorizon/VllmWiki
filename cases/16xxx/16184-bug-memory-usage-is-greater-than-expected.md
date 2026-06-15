# vllm-project/vllm#16184: [Bug]: memory usage is greater than expected

| 字段 | 值 |
| --- | --- |
| Issue | [#16184](https://github.com/vllm-project/vllm/issues/16184) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: memory usage is greater than expected

### Issue 正文摘录

### Your current environment cuda out of memory ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/ed31241a-8bee-4a87-a357-fe45ca0d6f48) I encapsulated a vllm image, and when enabled locally, everything is normal memory occupies as expected in the figure, but when I deployed the image on a Driver Version: 525 cuda 12.0 server, the memory occupancy was three GB larger than expected, and the GPUS of both servers were exactly the same. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ies as expected in the figure, but when I deployed the image on a Driver Version: 525 cuda 12.0 server, the memory occupancy was three GB larger than expected, and the GPUS of both servers were exactly the same. ### Bef...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y usage is greater than expected bug;stale ### Your current environment cuda out of memory ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/ed31241a-8bee-4a87-a357-fe45ca0d6f48) I encapsulated...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: answer lots of frequently asked questions. performance frontend_api cuda oom env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: memory usage is greater than expected bug;stale ### Your current environment cuda out of memory ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/ed31241a-8bee-4a87-a357-fe45ca0d6f48) I e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance frontend_api cuda oom env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
