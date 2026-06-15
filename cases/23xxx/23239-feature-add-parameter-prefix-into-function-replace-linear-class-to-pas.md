# vllm-project/vllm#23239: [Feature]: add parameter 'prefix' into function replace_linear_class to pass the layer name

| 字段 | 值 |
| --- | --- |
| Issue | [#23239](https://github.com/vllm-project/vllm/issues/23239) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: add parameter 'prefix' into function replace_linear_class to pass the layer name

### Issue 正文摘录

### 🚀 The feature, motivation and pitch add parameter 'prefix' into function replace_linear_class (in vllm/model_executor/models) in order to pass the layer name to QuantConfig. I was trying to load a quantized model with --model_ impl transformers. But I met a bug that the unquantized Linear was replaced with ReplicatedLinear or RowParallelLinear. I found the reason is that replace_linear_class will replace all linear and the LinearBase judging it the linear is quantized by quant_config is None or not. Unquantized layers are not correctly identified. I thought add parameter 'prefix' into function replace_linear_class maybe a solution. The layer name will pass to QuantConfig.get_quant_method，therefore, user can make some additional jugements in get_quant_method. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: itch add parameter 'prefix' into function replace_linear_class (in vllm/model_executor/models) in order to pass the layer name to QuantConfig. I was trying to load a quantized model with --model_ impl transformers. But...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: class (in vllm/model_executor/models) in order to pass the layer name to QuantConfig. I was trying to load a quantized model with --model_ impl transformers. But I met a bug that the unquantized Linear was replaced with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: refix' into function replace_linear_class to pass the layer name feature request ### 🚀 The feature, motivation and pitch add parameter 'prefix' into function replace_linear_class (in vllm/model_executor/models) in order...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
