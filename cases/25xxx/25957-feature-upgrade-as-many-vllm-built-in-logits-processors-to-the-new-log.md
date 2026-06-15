# vllm-project/vllm#25957: [Feature]: Upgrade as many vLLM built-in logits processors to the new logits processors programming model as possible

| 字段 | 值 |
| --- | --- |
| Issue | [#25957](https://github.com/vllm-project/vllm/issues/25957) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Upgrade as many vLLM built-in logits processors to the new logits processors programming model as possible

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM v1 is intended to handle logits processors differently than vLLM v0. Logits processors should subclass `LogitsProcessor`; built-in logits processors should be implemented in `vllm/v1/sample/logits_processor/builtin.py` and added to the `BUILTIN_LOGITS_PROCESSORS` list in `vllm/v1/sample/logits_processor/__init__.py` However, in actuality only several of the vLLM built-in logits processors (Min-P, logits bias, min tokens) have been converted to work this way; the rest are still hard-coded into the engine core and are not implemented as `LogitsProcessor` subclasses. The reason for this is that there is an open issue to revise the logits processor programming model ( #25389 ) and it makes sense to resolve this issue before converting these hard-coded logits processors to the new style. Once #25389 is resolved, it makes sense to consider which of the following hard-coded logits processors can be updated to the new style: * Allowed token IDs * Bad words * Repetition penalty * Frequency penalty * Presence penalty * Temperature * Top-K * Top-P ### Alternatives Until #25389 is resolved, incremental improvements can be made to the existing hard-...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ssors to the new logits processors programming model as possible feature request;stale ### 🚀 The feature, motivation and pitch vLLM v1 is intended to handle logits processors differently than vLLM v0. Logits processors...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vLLM built-in logits processors to the new logits processors programming model as possible feature request;stale ### 🚀 The feature, motivation and pitch vLLM v1 is intended to handle logits processors differently than v...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: epetition penalty * Frequency penalty * Presence penalty * Temperature * Top-K * Top-P ### Alternatives Until #25389 is resolved, incremental improvements can be made to the existing hard-coded logits processors without...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
