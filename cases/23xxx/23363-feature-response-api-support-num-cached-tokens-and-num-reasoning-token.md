# vllm-project/vllm#23363: [Feature][Response API] Support `num_cached_tokens` and `num_reasoning_tokens` in ResponseUsage

| 字段 | 值 |
| --- | --- |
| Issue | [#23363](https://github.com/vllm-project/vllm/issues/23363) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Response API] Support `num_cached_tokens` and `num_reasoning_tokens` in ResponseUsage

### Issue 正文摘录

### 🚀 The feature, motivation and pitch These attributes are important for monitoring model behavior. But both variables are set to 0 now. https://github.com/vllm-project/vllm/blob/8a19303173881e4197c7656727c6f2b296faa7fc/vllm/entrypoints/context.py#L70-L74 https://github.com/vllm-project/vllm/pull/22667 implements `num_prompt_tokens` and `num_output_tokens`, but we still need help for `num_cached_tokens` and `num_reasoning_tokens`. When implementing this, please note that 1. gpt-oss has built-in tool calls so one request can trigger multiple rounds of generation https://github.com/vllm-project/vllm/blob/8a19303173881e4197c7656727c6f2b296faa7fc/vllm/entrypoints/openai/serving_engine.py#L954 2. For non_streaming case, Context.append_output is called for each round of generation, while for streaming case, append_output is called for each output token. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ure, motivation and pitch These attributes are important for monitoring model behavior. But both variables are set to 0 now. https://github.com/vllm-project/vllm/blob/8a19303173881e4197c7656727c6f2b296faa7fc/vllm/entryp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: re request ### 🚀 The feature, motivation and pitch These attributes are important for monitoring model behavior. But both variables are set to 0 now. https://github.com/vllm-project/vllm/blob/8a19303173881e4197c7656727c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: `num_cached_tokens` and `num_reasoning_tokens` in ResponseUsage feature request ### 🚀 The feature, motivation and pitch These attributes are important for monitoring model behavior. But both variables are set to 0 now....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
