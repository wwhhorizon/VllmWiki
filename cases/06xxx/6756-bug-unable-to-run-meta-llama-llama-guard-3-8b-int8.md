# vllm-project/vllm#6756: [Bug]: Unable to run meta-llama/Llama-Guard-3-8B-INT8

| 字段 | 值 |
| --- | --- |
| Issue | [#6756](https://github.com/vllm-project/vllm/issues/6756) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unable to run meta-llama/Llama-Guard-3-8B-INT8

### Issue 正文摘录

### Your current environment Latest Docker image, RTX 4090 ### 🐛 Describe the bug ``` docker run --gpus all vllm/vllm-openai:latest --model meta-llama/Llama-Guard-3-8B-INT8 ... [rank0]: raise ValueError(f"Cannot find any of {keys} in the model's " [rank0]: ValueError: Cannot find any of ['adapter_name_or_path'] in the model's quantization config. ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Unable to run meta-llama/Llama-Guard-3-8B-INT8 bug ### Your current environment Latest Docker image, RTX 4090 ### 🐛 Describe the bug ``` docker run --gpus all vllm/vllm-openai:latest --model meta-llama/Llama-Guar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eta-llama/Llama-Guard-3-8B-INT8 bug ### Your current environment Latest Docker image, RTX 4090 ### 🐛 Describe the bug ``` docker run --gpus all vllm/vllm-openai:latest --model meta-llama/Llama-Guard-3-8B-INT8 ... [rank0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: : ValueError: Cannot find any of ['adapter_name_or_path'] in the model's quantization config. ```
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: a-Guard-3-8B-INT8 bug ### Your current environment Latest Docker image, RTX 4090 ### 🐛 Describe the bug ``` docker run --gpus all vllm/vllm-openai:latest --model meta-llama/Llama-Guard-3-8B-INT8 ... [rank0]: raise Value...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: run meta-llama/Llama-Guard-3-8B-INT8 bug ### Your current environment Latest Docker image, RTX 4090 ### 🐛 Describe the bug ``` docker run --gpus all vllm/vllm-openai:latest --model meta-llama/Llama-Guard-3-8B-INT8 ... [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
