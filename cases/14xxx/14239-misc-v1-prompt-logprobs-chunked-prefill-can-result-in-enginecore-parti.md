# vllm-project/vllm#14239: [Misc]: [V1] prompt logprobs + chunked prefill can result in `EngineCore` partial prefill output

| 字段 | 值 |
| --- | --- |
| Issue | [#14239](https://github.com/vllm-project/vllm/issues/14239) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: [V1] prompt logprobs + chunked prefill can result in `EngineCore` partial prefill output

### Issue 正文摘录

See https://github.com/vllm-project/vllm/blob/4f5b059f146adeecd153fa781cf21863ed6679d8/vllm/v1/engine/output_processor.py#L277 Prompt logprobs + chunked prefill can result in engine core returning an output for a partial prefill (in order to send back partial prompt logprobs.) This breaks the invariant that process_outputs is only operating on engine core outputs associated with non-partial completions. Currently this is handled by having `is_prefilling` in `OutputProcessor` check for new decoded tokens, indicating that the completion is not partial. A follow-up PR should aggregate partial prompt logprobs in the EngineCore. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: [V1] prompt logprobs + chunked prefill can result in `EngineCore` partial prefill output See https://github.com/vllm-project/vllm/blob/4f5b059f146adeecd153fa781cf21863ed6679d8/vllm/v1/engine/output_processor.py#...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ariant that process_outputs is only operating on engine core outputs associated with non-partial completions. Currently this is handled by having `is_prefilling` in `OutputProcessor` check for new decoded tokens, indica...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: re. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
