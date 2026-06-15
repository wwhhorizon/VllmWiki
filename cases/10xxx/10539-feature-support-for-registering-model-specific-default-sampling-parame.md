# vllm-project/vllm#10539: [Feature]: Support for Registering Model-Specific Default Sampling Parameters

| 字段 | 值 |
| --- | --- |
| Issue | [#10539](https://github.com/vllm-project/vllm/issues/10539) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Registering Model-Specific Default Sampling Parameters

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When starting an OpenAI-compatible server, provide a specific set of sampling parameters to override the default parameters provided by vLLM. Some model publishers (e.g., Qwen2.5) provide a set of parameters optimized for their model. Setting these parameters manually in the client for every request can be cumbersome, and forgetting to do so may result in incoherent outputs. Do the maintainers of vLLM consider it necessary to allow registering such parameters along with the model, so they can override the default sampling parameters? If deemed necessary, I am open to developing this feature and submitting a pull request. ### Alternatives _No response_ ### Additional context https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/generation_config.json ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support for Registering Model-Specific Default Sampling Parameters feature request ### 🚀 The feature, motivation and pitch When starting an OpenAI-compatible server, provide a specific set of sampling paramet...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Support for Registering Model-Specific Default Sampling Parameters feature request ### 🚀 The feature, motivation and pitch When starting an OpenAI-compatible server, provide a specific set of sampling paramet...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: son ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pport for Registering Model-Specific Default Sampling Parameters feature request ### 🚀 The feature, motivation and pitch When starting an OpenAI-compatible server, provide a specific set of sampling parameters to overri...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
