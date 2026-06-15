# vllm-project/vllm#10937: [Usage]: Inquiry about AsyncLLMEngine's generate method and multi-modal input support

| 字段 | 值 |
| --- | --- |
| Issue | [#10937](https://github.com/vllm-project/vllm/issues/10937) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Inquiry about AsyncLLMEngine's generate method and multi-modal input support

### Issue 正文摘录

### Your current environment ```text vllm 0.6.0 vllm-flash-attn 2.6.1 ``` ### How would you like to use vllm I would like to ask whether the generate method of AsyncLLMEngine supports multi-modal input, including both text and images. I have noticed that in the source code, the input type is specified as inputs: PromptInputs, and PromptInputs only supports: A text prompt (:class:stror:class:TextPrompt) A tokenized prompt (:class:TokensPrompt`) A single data structure containing both an encoder and a decoder prompt (:class:ExplicitEncoderDecoderPrompt`) If I am using a multi-modal model, how can I input images? Thank you! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: out AsyncLLMEngine's generate method and multi-modal input support usage;stale ### Your current environment ```text vllm 0.6.0 vllm-flash-attn 2.6.1 ``` ### How would you like to use vllm I would like to ask whether the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and images. I have noticed that in the source code, the input type is specified as inputs: PromptInputs, and PromptInputs only supports: A text prompt (:class:stror:class:TextPrompt) A tokenized prompt (:class:TokensPro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ou! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rompt (:class:ExplicitEncoderDecoderPrompt`) If I am using a multi-modal model, how can I input images? Thank you! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
