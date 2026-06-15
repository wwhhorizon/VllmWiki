# vllm-project/vllm#4502: [New Model]: how to debug the values of tensor while adding a new model

| 字段 | 值 |
| --- | --- |
| Issue | [#4502](https://github.com/vllm-project/vllm/issues/4502) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [New Model]: how to debug the values of tensor while adding a new model

### Issue 正文摘录

### The model to consider. If I do print(torch), the following error is coming, so how can I debug my torch's value `CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.` ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? _No response_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ch), the following error is coming, so how can I debug my torch's value `CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.` ### The closest model vll...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: want? _No response_ correctness frontend_api;model_support cuda;kernel mismatch env_dependency The model to consider.
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: esponse_ correctness frontend_api;model_support cuda;kernel mismatch env_dependency The model to consider.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: how to debug the values of tensor while adding a new model new-model ### The model to consider. If I do print(torch), the following error is coming, so how can I debug my torch's value `CUDA kernel errors m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
