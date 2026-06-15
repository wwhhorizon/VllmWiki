# vllm-project/vllm#27485: [Bug]: `vllm bench serve` incorrectly calculates ITL for openai-chat with reasoning, tool calling, or harmony models

| 字段 | 值 |
| --- | --- |
| Issue | [#27485](https://github.com/vllm-project/vllm/issues/27485) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `vllm bench serve` incorrectly calculates ITL for openai-chat with reasoning, tool calling, or harmony models

### Issue 正文摘录

### Your current environment Testing `vllm bench serve` from main as of opening this bug - Oct 24, 2025. The issue is agnostic of hardware in use. ### 🐛 Describe the bug When using `vllm bench serve` with the `openai-chat` backend against a vLLM server, the inter-token latency (ITL) is incorrectly calculated for any situation where the server chunks streamed back do not map 1:1 with tokens generated. This regularly happens when reasoning parsers, tool call parsers, or harmony models are in use as all of these have special tokens and parsing logic that can cause responses to get temporarily buffered and/or special tokens removed from the final output. The logic in `vllm.benchmarks.lib.endpoint_request_func.async_request_openai_chat_completions` assumes every chunk is one token and calculates ITL as the simple timestamp difference between the last chunk and this chunk. This is misleading, and will lead to reporting higher ITL values than reality because this is actually calculating the latency between streaming chunks as opposed to the latency between generated tokens. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbo...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: tool calling, or harmony models bug;stale ### Your current environment Testing `vllm bench serve` from main as of opening this bug - Oct 24, 2025. The issue is agnostic of hardware in use. ### 🐛 Describe the bug When us...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ITL for openai-chat with reasoning, tool calling, or harmony models bug;stale ### Your current environment Testing `vllm bench serve` from main as of opening this bug - Oct 24, 2025. The issue is agnostic of hardware in...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 🐛 Describe the bug When using `vllm bench serve` with the `openai-chat` backend against a vLLM server, the inter-token latency (ITL) is incorrectly calculated for any situation where the server chunks streamed back do n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tool call parsers, or harmony models are in use as all of these have special tokens and parsing logic that can cause responses to get temporarily buffered and/or special tokens removed from the final output. The logic i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
