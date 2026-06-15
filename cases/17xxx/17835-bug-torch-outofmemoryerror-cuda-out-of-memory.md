# vllm-project/vllm#17835: [Bug]: torch.OutOfMemoryError: CUDA out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#17835](https://github.com/vllm-project/vllm/issues/17835) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.OutOfMemoryError: CUDA out of memory

### Issue 正文摘录

### Your current environment 貌似是 troch 吧正在使用的显存值 赋给了可用显存值，导致无法分配现存报错。 ### 🐛 Describe the bug torch.OutOfMemoryError: CUDA out of memory ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory cuda;triton build_error;oom dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: torch.OutOfMemoryError: CUDA out of memory bug;stale ### Your current environment 貌似是 troch 吧正在使用的显存值 赋给了可用显存值，导致无法分配现存报错。 ### 🐛 Describe the bug torch.OutOfMemoryError: CUDA out of memory ### Before submitting a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: torch.OutOfMemoryError: CUDA out of memory bug;stale ### Your current environment 貌似是 troch 吧正在使用的显存值 赋给了可用显存值，导致无法分配现存报错。 ### 🐛 Describe the bug torch.OutOfMemoryError: CUDA out of memory ### Before submitting a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ld;distributed_parallel;frontend_api;model_support;scheduler_memory cuda;triton build_error;oom dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ;frontend_api;model_support;scheduler_memory cuda;triton build_error;oom dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
