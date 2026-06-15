# vllm-project/vllm#23869: [Renderer]: Move `Processor` out of `AsyncLLM` and `LLMEngine`

| 字段 | 值 |
| --- | --- |
| Issue | [#23869](https://github.com/vllm-project/vllm/issues/23869) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Renderer]: Move `Processor` out of `AsyncLLM` and `LLMEngine`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Refer to [#22880](https://github.com/vllm-project/vllm/issues/22880) Currently last-mile input processing happens inside `AsyncLLM` but we should consolidate it with other processing workload (such as chat formatting and tokenization). In order to achieve this goal, the following requirements should be met 1. Have `Processor` live at the layer of API server / `LLM` class instead of `AsyncLLM` and become part of the default path 2. Add new contract between API Server and `AsyncLLM` accordingly. 3. Do not remove `Processor` from `AsyncLLM` yet, but it should be only used when the the old contract (a.k.a `PromptType`) is used, and a deprecation warning should be given to the user. 4. Documentation. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ut we should consolidate it with other processing workload (such as chat formatting and tokenization). In order to achieve this goal, the following requirements should be met 1. Have `Processor` live at the layer of API...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Renderer]: Move `Processor` out of `AsyncLLM` and `LLMEngine` feature request ### 🚀 The feature, motivation and pitch Refer to [#22880](https://github.com/vllm-project/vllm/issues/22880) Currently last-mile input proce...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
