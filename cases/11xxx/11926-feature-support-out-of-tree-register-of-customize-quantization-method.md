# vllm-project/vllm#11926: [Feature]: Support out-of-tree register of customize quantization method

| 字段 | 值 |
| --- | --- |
| Issue | [#11926](https://github.com/vllm-project/vllm/issues/11926) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support out-of-tree register of customize quantization method

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Thanks for such excellent work! We hope to leverage the fast inference capabilities of vllm to evaluate the accuracy of the quantized models. However, vllm currently does not support custom quantization schemes, and we would appreciate it if the functionality to register custom quantization schemes could be provided. The usage would be as follows: ```python from vllm.model_executor.layers.quantization import QuantizationConfig from vllm.model_executor.layers.quantization import register_quantization_config @register_quantization_config("customize") class CustomizeQuantizationConfig(QuantizationConfig): """Customize quantization config.""" ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: t work! We hope to leverage the fast inference capabilities of vllm to evaluate the accuracy of the quantized models. However, vllm currently does not support custom quantization schemes, and we would appreciate it if t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: urrently does not support custom quantization schemes, and we would appreciate it if the functionality to register custom quantization schemes could be provided. The usage would be as follows: ```python from vllm.model_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: inference capabilities of vllm to evaluate the accuracy of the quantized models. However, vllm currently does not support custom quantization schemes, and we would appreciate it if the functionality to register custom q...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: hope to leverage the fast inference capabilities of vllm to evaluate the accuracy of the quantized models. However, vllm currently does not support custom quantization schemes, and we would appreciate it if the function...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Support out-of-tree register of customize quantization method feature request ### 🚀 The feature, motivation and pitch Thanks for such excellent work! We hope to leverage the fast inference capabilities of vll...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
