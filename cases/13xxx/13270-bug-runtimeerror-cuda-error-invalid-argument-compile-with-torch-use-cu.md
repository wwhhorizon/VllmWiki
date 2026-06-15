# vllm-project/vllm#13270: [Bug]: RuntimeError: CUDA error: invalid argument [ Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

| 字段 | 值 |
| --- | --- |
| Issue | [#13270](https://github.com/vllm-project/vllm/issues/13270) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: invalid argument [ Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

### Issue 正文摘录

### Your current environment An error occurs when finetuning Qwen2.5-3b ### 🐛 Describe the bug An error occurs when finetuning Qwen2.5-3b ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: RuntimeError: CUDA error: invalid argument [ Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. bug;stale ### Your current environment An error occurs when finetuning Qwen2.5-3b ### 🐛 Describe th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: RuntimeError: CUDA error: invalid argument [ Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. bug;stale ### Your current environment An error occurs when finetuning Qwen2.5-3b ### 🐛 Describe th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: bug;stale ### Your current environment An error occurs when finetuning Qwen2.5-3b ### 🐛 Describe the bug An error occurs when finetuning Qwen2.5-3b ### Before submitting a new issue... - [x] Make sure you already search...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. bug;stale ### Your current environment An error occurs when finetuning Qwen2.5-3b ### 🐛 Describe the bug An error occurs when finetuning Qwen2.5-3b ###...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
