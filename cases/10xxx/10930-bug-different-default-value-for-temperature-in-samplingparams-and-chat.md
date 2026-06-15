# vllm-project/vllm#10930: [Bug]: Different default value for temperature in SamplingParams and ChatCompletionRequest

| 字段 | 值 |
| --- | --- |
| Issue | [#10930](https://github.com/vllm-project/vllm/issues/10930) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Different default value for temperature in SamplingParams and ChatCompletionRequest

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The default value for `temperature` in `SamplingParams` is `1.0`. https://github.com/vllm-project/vllm/blob/571da8fc431ec36427ee1034a7779b23229b015e/vllm/sampling_params.py#L176 The default value for `temperature` in `ChatCompletionRequest` is `0.7`. https://github.com/vllm-project/vllm/blob/571da8fc431ec36427ee1034a7779b23229b015e/vllm/entrypoints/openai/protocol.py#L173 This can lead to inconsistencies between online and offline inference results. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 5e/vllm/entrypoints/openai/protocol.py#L173 This can lead to inconsistencies between online and offline inference results. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: arams and ChatCompletionRequest bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The default value for `temperature` in `SamplingParams` is `1.0`. https://github.com/vllm-proje...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ferent default value for temperature in SamplingParams and ChatCompletionRequest bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The default value for `temperature` in `Sampli...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
