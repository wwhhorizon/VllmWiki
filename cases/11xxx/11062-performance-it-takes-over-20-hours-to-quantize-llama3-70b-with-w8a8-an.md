# vllm-project/vllm#11062: [Performance]: It takes over 20 hours to quantize llama3-70B with w8a8 and I wonder does it meet expectations?

| 字段 | 值 |
| --- | --- |
| Issue | [#11062](https://github.com/vllm-project/vllm/issues/11062) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: It takes over 20 hours to quantize llama3-70B with w8a8 and I wonder does it meet expectations?

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ``` llmcompressor==0.2.0 compressed-tensors==0.7.1 4 NVIDIA A100 80GB PCIe ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: necessary) ``` llmcompressor==0.2.0 compressed-tensors==0.7.1 4 NVIDIA A100 80GB PCIe ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ``` llmcompres...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ``` llmcompressor==0.2.0 compressed-tensors==0.7.1 4 NVIDIA A100 80GB PCIe ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom ri...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Performance]: It takes over 20 hours to quantize llama3-70B with w8a8 and I wonder does it meet expectations? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Performance]: It takes over 20 hours to quantize llama3-70B with w8a8 and I wonder does it meet expectations? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
