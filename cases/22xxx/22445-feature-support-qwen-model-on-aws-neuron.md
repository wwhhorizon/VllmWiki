# vllm-project/vllm#22445: [Feature]: Support Qwen model on AWS Neuron

| 字段 | 值 |
| --- | --- |
| Issue | [#22445](https://github.com/vllm-project/vllm/issues/22445) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support Qwen model on AWS Neuron

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Summary With the release of **AWS Neuron SDK 2.24.0** (June 24, 2025), **beta support for Qwen 2.5 text models** has been added for inference on Neuron. However, the `vLLM` Neuron backend does not currently support these models. ## Details The following is from the Neuron 2.24 release notes: > **Model support:** Added beta support for Qwen 2.5 text models. Despite this, the `vLLM` codebase restricts model loading to only the following architectures in `neuron/model_loader.py`: ```python _NEURON_SUPPORTED_MODELS: dict[str, tuple[str, str]] = { "LlamaForCausalLM": ("...", "NeuronLlamaForCausalLM"), "MistralForCausalLM": ("...", "NeuronLlamaForCausalLM"), "DbrxForCausalLM": ("...", "NeuronDbrxForCausalLM"), "MixtralForCausalLM": ("...", "NeuronMixtralForCausalLM"), "MllamaForConditionalGeneration": ("...", "NeuronMllamaForCausalLM"), } ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequ...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Support Qwen model on AWS Neuron feature request;stale ### 🚀 The feature, motivation and pitch ## Summary With the release of **AWS Neuron SDK 2.24.0** (June 24, 2025), **beta support for Qwen 2.5 text models...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support Qwen model on AWS Neuron feature request;stale ### 🚀 The feature, motivation and pitch ## Summary With the release of **AWS Neuron SDK 2.24.0** (June 24, 2025), **beta support for Qwen 2.5 text models...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: els** has been added for inference on Neuron. However, the `vLLM` Neuron backend does not currently support these models. ## Details The following is from the Neuron 2.24 release notes: > **Model support:** Added beta s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: this, the `vLLM` codebase restricts model loading to only the following architectures in `neuron/model_loader.py`: ```python _NEURON_SUPPORTED_MODELS: dict[str, tuple[str, str]] = { "LlamaForCausalLM": ("...", "NeuronLl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
