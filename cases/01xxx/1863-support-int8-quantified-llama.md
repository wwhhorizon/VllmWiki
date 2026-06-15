# vllm-project/vllm#1863: Support Int8-quantified llama ?

| 字段 | 值 |
| --- | --- |
| Issue | [#1863](https://github.com/vllm-project/vllm/issues/1863) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support Int8-quantified llama ?

### Issue 正文摘录

Hi, dear: Are there any INT8-quantified llama model available for testing ? I want to use smoothquant and torch-int to quantify the model and then use vllm to reason, but smoothquant and torch-in are only suitable for cuda11.3. so, there are existing quantified int8 models that can be inferred directly with vllm ?? Thank you!

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: re any INT8-quantified llama model available for testing ? I want to use smoothquant and torch-int to quantify the model and then use vllm to reason, but smoothquant and torch-in are only suitable for cuda11.3. so, ther...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Support Int8-quantified llama ? Hi, dear: Are there any INT8-quantified llama model available for testing ? I want to use smoothquant and torch-int to quantify the model and then use vllm to reason, but smoothquant and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Support Int8-quantified llama ? Hi, dear: Are there any INT8-quantified llama model available for testing ? I want to use smoothquant and torch-int to quantify the model and then use vllm to reason, but smoothquant and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ama ? Hi, dear: Are there any INT8-quantified llama model available for testing ? I want to use smoothquant and torch-int to quantify the model and then use vllm to reason, but smoothquant and torch-in are only suitable...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
