# vllm-project/vllm#35573: [Doc]: Speculative decoding --speculative-config option lacks clear documentation of accepted keys and values

| 字段 | 值 |
| --- | --- |
| Issue | [#35573](https://github.com/vllm-project/vllm/issues/35573) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Speculative decoding --speculative-config option lacks clear documentation of accepted keys and values

### Issue 正文摘录

### 📚 The doc issue The `--speculative-config` flag in vLLM’s CLI is referenced in the documentation, but the list of supported configuration keys, their expected data types, and permissible values is missing. Users are forced to guess the syntax (e.g., `draft_model=...`, `max_draft_len=...`, `num_speculative_tokens=...`) and often encounter parsing errors or silent failures on local hardware. This undocumented ambiguity hampers adoption of speculative decoding and leads to wasted troubleshooting time. **Relevant documentation:** - - ### Suggest a potential alternative/fix 1. Add a dedicated “Speculative Config” section to the spec‑decode docs that enumerates all supported keys (e.g., `draft_model`, `max_draft_len`, `num_speculative_tokens`, `temperature`, `top_p`, etc.), their data types, default values, and allowed ranges. 2. Update the argument parser in the codebase to emit a clear error message when an unknown key or invalid value is supplied, and include a `--speculative-config-help` flag that prints the supported schema. Implementing these changes will make the feature discoverable, reduce user friction, and ensure consistent behavior across environments. ### Before submitt...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Doc]: Speculative decoding --speculative-config option lacks clear documentation of accepted keys and values documentation ### 📚 The doc issue The `--speculative-config` flag in vLLM’s CLI is referenced in the document...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Doc]: Speculative decoding --speculative-config option lacks clear documentation of accepted keys and values documentation ### 📚 The doc issue The `--speculative-config` flag in vLLM’s CLI is referenced in the document...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
