# vllm-project/vllm#17942: [Bug]: Token usage is unavailable in Qwen3 streaming thought mode.

| 字段 | 值 |
| --- | --- |
| Issue | [#17942](https://github.com/vllm-project/vllm/issues/17942) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Token usage is unavailable in Qwen3 streaming thought mode.

### Issue 正文摘录

### Your current environment vLLM API server version 0.8.5 Qwen3-4B ### 🐛 Describe the bug When using VLLM to serve Qwen3 with streaming responses, VLLM is configured to return token usage details (--enable_prompt_tokens_details --enable-reasoning --reasoning-parser deepseek_r1). With the same request method, if /no_think is appended at the end of the prompt to disable thinking mode, the stream ends with two empty content chunks—the last one containing token usage (usage). However, if /no_think is omitted or /think is used to enable thinking mode, the stream only ends with a single empty content chunk, which does not include usage. Since the only difference between these scenarios is the presence of /no_think at the prompt's end, this is preliminarily judged to be a bug. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Token usage is unavailable in Qwen3 streaming thought mode. bug;stale ### Your current environment vLLM API server version 0.8.5 Qwen3-4B ### 🐛 Describe the bug When using VLLM to serve Qwen3 with streaming respo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Token usage is unavailable in Qwen3 streaming thought mode. bug;stale ### Your current environment vLLM API server version 0.8.5 Qwen3-4B ### 🐛 Describe the bug When using VLLM to serve Qwen3 with streaming respo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng thought mode. bug;stale ### Your current environment vLLM API server version 0.8.5 Qwen3-4B ### 🐛 Describe the bug When using VLLM to serve Qwen3 with streaming responses, VLLM is configured to return token usage det...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ug. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
