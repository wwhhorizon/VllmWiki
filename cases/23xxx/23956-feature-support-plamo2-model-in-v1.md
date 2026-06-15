# vllm-project/vllm#23956: [Feature]: Support `Plamo2` Model in V1

| 字段 | 值 |
| --- | --- |
| Issue | [#23956](https://github.com/vllm-project/vllm/issues/23956) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support `Plamo2` Model in V1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We will drop support for V0 in the very near future, and if we want to continue supporting this model in vLLM, it needs to be ported to V1. The main work here is in adapting the custom Mamba layer to match how V1 manages the mamba state. The MambaMixer, MambaMixer2, MinimaxLinearAttention and ShortConv can all be used as a reference for how to do this. ### Alternatives Drop model support in vLLM. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support `Plamo2` Model in V1 feature request ### 🚀 The feature, motivation and pitch We will drop support for V0 in the very near future, and if we want to continue supporting this model in vLLM, it needs to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support `Plamo2` Model in V1 feature request ### 🚀 The feature, motivation and pitch We will drop support for V0 in the very near future, and if we want to continue supporting this model in vLLM, it needs to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
