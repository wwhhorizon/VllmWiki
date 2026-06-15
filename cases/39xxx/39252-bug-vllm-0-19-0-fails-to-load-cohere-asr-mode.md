# vllm-project/vllm#39252: [Bug]: vLLM 0.19.0 fails to load Cohere ASR mode

| 字段 | 值 |
| --- | --- |
| Issue | [#39252](https://github.com/vllm-project/vllm/issues/39252) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.19.0 fails to load Cohere ASR mode

### Issue 正文摘录

### 🐛 Describe the bug I installed vllm==0.19.0 in my environment and attempted to run the CohereLabs/cohere-transcribe-03-2026 model. However, an error occurs during initialization/serving, preventing the model from running successfully. - To Reproduce Steps to reproduce the behavior: 1. Install vLLM: `pip install vllm==0.19.0` 2. Run the model: `vllm serve CohereLabs/cohere-transcribe-03-2026` 3. Observe the error in logs ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: alization/serving, preventing the model from running successfully. - To Reproduce Steps to reproduce the behavior: 1. Install vLLM: `pip install vllm==0.19.0` 2. Run the model: `vllm serve CohereLabs/cohere-transcribe-0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: vLLM 0.19.0 fails to load Cohere ASR mode bug ### 🐛 Describe the bug I installed vllm==0.19.0 in my environment and attempted to run the CohereLabs/cohere-transcribe-03-2026 model. However, an error occurs during initia...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nvironment and attempted to run the CohereLabs/cohere-transcribe-03-2026 model. However, an error occurs during initialization/serving, preventing the model from running successfully. - To Reproduce Steps to reproduce t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
