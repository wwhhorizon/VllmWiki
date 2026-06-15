# vllm-project/vllm#5346: [RFC]: Refactor MoE

| 字段 | 值 |
| --- | --- |
| Issue | [#5346](https://github.com/vllm-project/vllm/issues/5346) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Refactor MoE

### Issue 正文摘录

### Motivation. Right now, we have much of the generic functionality related to MoEs (such as fp8 quantization and weight loading) are embedded into specific model definitions https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mixtral.py#L58 This means we have to re-implement much of the functionality in each model file ### Proposed Change. Create an abstract `MoELinear` that can be used by each model ### Feedback Period. Over the weekend ### CC List. @pcmoritz ### Any Other Things. _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: now, we have much of the generic functionality related to MoEs (such as fp8 quantization and weight loading) are embedded into specific model definitions https://github.com/vllm-project/vllm/blob/main/vllm/model_executo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: MoEs (such as fp8 quantization and weight loading) are embedded into specific model definitions https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mixtral.py#L58 This means we have to re-implement...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: (such as fp8 quantization and weight loading) are embedded into specific model definitions https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mixtral.py#L58 This means we have to re-implement much...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [RFC]: Refactor MoE RFC ### Motivation. Right now, we have much of the generic functionality related to MoEs (such as fp8 quantization and weight loading) are embedded into specific model definitions https://github.com/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
