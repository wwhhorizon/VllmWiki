# vllm-project/vllm#25022: [Feature]: Request support for AWQ quantization on GPUs with CUDA Compute Capability < 8.0 using Compressed Tensors Quantization.

| 字段 | 值 |
| --- | --- |
| Issue | [#25022](https://github.com/vllm-project/vllm/issues/25022) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Request support for AWQ quantization on GPUs with CUDA Compute Capability < 8.0 using Compressed Tensors Quantization.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Request support for AWQ quantization on GPUs with CUDA Compute Capability < 8.0 using Compressed Tensors Quantization. ```error RuntimeError: ('Quantization scheme is not supported for ', 'the current GPU. Min capability: 80. ', 'Current capability: 75.') ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Request support for AWQ quantization on GPUs with CUDA Compute Capability < 8.0 using Compressed Tensors Quantization. feature request;stale ### 🚀 The feature, motivation and pitch Request support for AWQ qua...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Request support for AWQ quantization on GPUs with CUDA Compute Capability < 8.0 using Compressed Tensors Quantization. feature request;stale ### 🚀 The feature, motivation and pitch Request support for AWQ qua...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Request support for AWQ quantization on GPUs with CUDA Compute Capability < 8.0 using Compressed Tensors Quantization. feature request;stale ### 🚀 The feature, motivation and pitch Request support for AWQ qua...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development frontend_api;quantization cuda;quantization 🚀 The feature, motivation and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
