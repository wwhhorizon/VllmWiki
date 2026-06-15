# vllm-project/vllm#26525: [Bug]: v0.11.0 New default VLLM_ALLREDUCE_USE_SYMM_MEM=1 prevent tensor-parallel on gpt-oss-120b

| 字段 | 值 |
| --- | --- |
| Issue | [#26525](https://github.com/vllm-project/vllm/issues/26525) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.11.0 New default VLLM_ALLREDUCE_USE_SYMM_MEM=1 prevent tensor-parallel on gpt-oss-120b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running the new vllm v0.11.0 and getting following issue : RuntimeError: CUDA driver error: invalid device ordinal after the update to v0.11.0 Switching --tensor_parallel_size to 1 allow start but disabled parallelisation After investigation the fix is to rollback VLLM_ALLREDUCE_USE_SYMM_MEM to 0. Defaults seems to have change since v0.10.2 release on which it used to work well. [Similar feedback here](https://discuss.vllm.ai/t/runtimeerror-cuda-driver-error-invalid-device-ordinal-after-the-update-to-v0-11-0/1703) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: running the new vllm v0.11.0 and getting following issue : RuntimeError: CUDA driver error: invalid device ordinal after the update to v0.11.0 Switching --tensor_parallel_size to 1 allow start but disabled parallelisati...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 1.0 New default VLLM_ALLREDUCE_USE_SYMM_MEM=1 prevent tensor-parallel on gpt-oss-120b bug;stale ### Your current environment ### 🐛 Describe the bug I'm running the new vllm v0.11.0 and getting following issue : RuntimeE...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: asked questions. performance distributed_parallel;model_support cuda env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: LLM_ALLREDUCE_USE_SYMM_MEM=1 prevent tensor-parallel on gpt-oss-120b bug;stale ### Your current environment ### 🐛 Describe the bug I'm running the new vllm v0.11.0 and getting following issue : RuntimeError: CUDA driver...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;model_support cuda env_dependency Your current envir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
