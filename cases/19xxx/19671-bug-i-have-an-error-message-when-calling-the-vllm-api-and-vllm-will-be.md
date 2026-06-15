# vllm-project/vllm#19671: [Bug]: I have an error message when calling the vllm api, and vllm will be closed.vllm:0.91.graphics card:5060TI

| 字段 | 值 |
| --- | --- |
| Issue | [#19671](https://github.com/vllm-project/vllm/issues/19671) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: I have an error message when calling the vllm api, and vllm will be closed.vllm:0.91.graphics card:5060TI

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug RuntimeError: CUDA error: no kernel image is available for execution on the device 2025-06-12 20:49:44 CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. 2025-06-12 20:49:44 For debugging consider passing CUDA_LAUNCH_BLOCKING=1 2025-06-12 20:49:44 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: or debugging consider passing CUDA_LAUNCH_BLOCKING=1 2025-06-12 20:49:44 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ### Before submitting a new issue... - [x] Make sure you already searched for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e ### Your current environment ### 🐛 Describe the bug RuntimeError: CUDA error: no kernel image is available for execution on the device 2025-06-12 20:49:44 CUDA kernel errors might be asynchronously reported at some ot...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ked questions. correctness ci_build;frontend_api cuda;kernel build_error;mismatch env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ncorrect. 2025-06-12 20:49:44 For debugging consider passing CUDA_LAUNCH_BLOCKING=1 2025-06-12 20:49:44 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ### Before submitting a new issue... - [x] Make...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: the vllm api, and vllm will be closed.vllm:0.91.graphics card:5060TI bug;stale ### Your current environment ### 🐛 Describe the bug RuntimeError: CUDA error: no kernel image is available for execution on the device 2025-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
