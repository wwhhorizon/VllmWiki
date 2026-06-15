# vllm-project/vllm#7378: [Bug]: prefill/prefix FP8 triton kernel for opt-125m - an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#7378](https://github.com/vllm-project/vllm/issues/7378) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;kernel;triton |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: prefill/prefix FP8 triton kernel for opt-125m - an illegal memory access was encountered

### Issue 正文摘录

### Your current environment As of merging https://github.com/vllm-project/vllm/pull/7208 ### 🐛 Describe the bug Illegal memory access for facebook/opt-125m. Does not affect e.g. `llama-2-7b` Specifically one of these errors: ``` RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered RuntimeError: CUDA error: an illegal memory access was encountered ```

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: prefill/prefix FP8 triton kernel for opt-125m - an illegal memory access was encountered bug;stale ### Your current environment As of merging https://github.com/vllm-project/vllm/pull/7208 ### 🐛 Describe the bug...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: prefill/prefix FP8 triton kernel for opt-125m - an illegal memory access was encountered bug;stale ### Your current environment As of merging https://github.com/vllm-project/vllm/pull/7208 ### 🐛 Describe the bug...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: prefill/prefix FP8 triton kernel for opt-125m - an illegal memory access was encountered bug;stale ### Your current environment As of merging https://github.com/vllm-project/vllm/pull/7208 ### 🐛 Describe the bug...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: mory access for facebook/opt-125m. Does not affect e.g. `llama-2-7b` Specifically one of these errors: ``` RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered RuntimeError: CUDA error: an illegal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2-7b` Specifically one of these errors: ``` RuntimeError: Triton Error [CUDA]: an illegal memory access was encountered RuntimeError: CUDA error: an illegal memory access was encountered ``` performance quantization cud...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
