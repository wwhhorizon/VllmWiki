# vllm-project/vllm#14637: [Feature]: replace current_platform.has_device_capability() with specific feature APIs

| 字段 | 值 |
| --- | --- |
| Issue | [#14637](https://github.com/vllm-project/vllm/issues/14637) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: replace current_platform.has_device_capability() with specific feature APIs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch There should be an audit of all call sites of `current_platform.has_device_capability()` to replace them with feature-specific query APIs. `has_device_capability` is CUDA-centric. There is some support for ROCm but the version numbers have different semantics. Often you want to check device capability because you want to conditionally enable a new feature such as bfloat16 or fp8. If we replaced `has_device_capability` with a feature check, e.g., `current_platform.supports_fp8()`, then this would be self-documenting and allow other platforms to implement them. For example, in gpu_worker.py it's used to check for bfloat16 support. The code would improve if there was a current_platform.supports_bfloat16(). ### Alternatives _No response_ ### Additional context This request was inspired by the recent PR #14245 that added new APIs to `current_platform` for fp8 support. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Feature]: replace current_platform.has_device_capability() with specific feature APIs feature request;stale ### 🚀 The feature, motivation and pitch There should be an audit of all call sites of `current_platform.has_de...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: apability because you want to conditionally enable a new feature such as bfloat16 or fp8. If we replaced `has_device_capability` with a feature check, e.g., `current_platform.supports_fp8()`, then this would be self-doc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: replace current_platform.has_device_capability() with specific feature APIs feature request;stale ### 🚀 The feature, motivation and pitch There should be an audit of all call sites of `current_platform.has_de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rent_platform.has_device_capability() with specific feature APIs feature request;stale ### 🚀 The feature, motivation and pitch There should be an audit of all call sites of `current_platform.has_device_capability()` to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
