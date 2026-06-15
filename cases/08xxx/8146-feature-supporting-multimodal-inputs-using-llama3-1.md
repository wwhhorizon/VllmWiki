# vllm-project/vllm#8146: [Feature]: Supporting MultiModal inputs using Llama3.1

| 字段 | 值 |
| --- | --- |
| Issue | [#8146](https://github.com/vllm-project/vllm/issues/8146) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Supporting MultiModal inputs using Llama3.1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We have a deployment of Llama3.1-8B-Instruct and Llama3.1-70B-Instruct models through vLLM hosted in our OnPremise GPU infra. While testing different use-cases, we realized that the current version of vLLM does not support MultiModal input for Llama3.1 as per this document: https://docs.vllm.ai/en/latest/models/supported_models.html#supported-vlms Is it possible to enable llama3.1 as a VLM? Or if it can be enabled through any different route, is there any documentation or guide around it? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Supporting MultiModal inputs using Llama3.1 feature request ### 🚀 The feature, motivation and pitch We have a deployment of Llama3.1-8B-Instruct and Llama3.1-70B-Instruct models through vLLM hosted in our OnP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: infra. While testing different use-cases, we realized that the current version of vLLM does not support MultiModal input for Llama3.1 as per this document: https://docs.vllm.ai/en/latest/models/supported_models.html#sup...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Supporting MultiModal inputs using Llama3.1 feature request ### 🚀 The feature, motivation and pitch We have a deployment of Llama3.1-8B-Instruct and Llama3.1-70B-Instruct models through vLLM hosted in our OnP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: B-Instruct models through vLLM hosted in our OnPremise GPU infra. While testing different use-cases, we realized that the current version of vLLM does not support MultiModal input for Llama3.1 as per this document: http...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
