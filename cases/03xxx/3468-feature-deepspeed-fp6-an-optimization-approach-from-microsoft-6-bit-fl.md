# vllm-project/vllm#3468: [Feature]: DeepSpeed-FP6: An Optimization Approach from Microsoft，6-bit Floating Point (FP6)

| 字段 | 值 |
| --- | --- |
| Issue | [#3468](https://github.com/vllm-project/vllm/issues/3468) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: DeepSpeed-FP6: An Optimization Approach from Microsoft，6-bit Floating Point (FP6)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch DeepSpeed-FP6: An Optimization Approach from Microsoft ### Alternatives Microsoft recently proposed an optimization approach called DeepSpeed-FP6. While it currently only supports a subset of models, it appears to offer some unique advantages. I am curious if the vLLM team has looked into it. Inference Acceleration: FP6 quantization can significantly improve inference speed while maintaining model accuracy. Facilitating on-the-fly, weight-only quantization: DeepSpeed-FP6 allows users to quantize their models on-the-fly with simple configuration options. ### Additional context https://github.com/microsoft/DeepSpeed/tree/master/blogs/deepspeed-fp6/03-05-2024 https://github.com/usyd-fsalab/fp6_llm

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: roach called DeepSpeed-FP6. While it currently only supports a subset of models, it appears to offer some unique advantages. I am curious if the vLLM team has looked into it. Inference Acceleration: FP6 quantization can...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Optimization Approach from Microsoft，6-bit Floating Point (FP6) feature request;stale ### 🚀 The feature, motivation and pitch DeepSpeed-FP6: An Optimization Approach from Microsoft ### Alternatives Microsoft recently pr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: zation can significantly improve inference speed while maintaining model accuracy. Facilitating on-the-fly, weight-only quantization: DeepSpeed-FP6 allows users to quantize their models on-the-fly with simple configurat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: gnificantly improve inference speed while maintaining model accuracy. Facilitating on-the-fly, weight-only quantization: DeepSpeed-FP6 allows users to quantize their models on-the-fly with simple configuration options....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: urious if the vLLM team has looked into it. Inference Acceleration: FP6 quantization can significantly improve inference speed while maintaining model accuracy. Facilitating on-the-fly, weight-only quantization: DeepSpe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
