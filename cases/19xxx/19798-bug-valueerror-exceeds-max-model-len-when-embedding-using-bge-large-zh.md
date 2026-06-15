# vllm-project/vllm#19798: [Bug]:ValueError: Exceeds max model len when embedding using bge-large-zh-v1.5

| 字段 | 值 |
| --- | --- |
| Issue | [#19798](https://github.com/vllm-project/vllm/issues/19798) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:ValueError: Exceeds max model len when embedding using bge-large-zh-v1.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm now using vllm to do embedding task on RAGFlow. `vllm serve BAAI/bge-large-zh-v1.5 --task embed --trust-remote-code ` My chunk size is 512, but I met **ValueError: This model's maximum context length is 512 tokens. However, you requested 1451 tokens in the input for embedding generation. Please reduce the length of the input.** I can embed all my files using Ollama with the same model. Does anybody know why this happen and how to fix it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]:ValueError: Exceeds max model len when embedding using bge-large-zh-v1.5 bug ### Your current environment ### 🐛 Describe the bug I'm now using vllm to do embedding task on RAGFlow. `vllm serve BAAI/bge-large-zh-v1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ueError: This model's maximum context length is 512 tokens. However, you requested 1451 tokens in the input for embedding generation. Please reduce the length of the input.** I can embed all my files using Ollama with t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
