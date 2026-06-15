# vllm-project/vllm#13390: [Usage]: Does vLLM support multi-task

| 字段 | 值 |
| --- | --- |
| Issue | [#13390](https://github.com/vllm-project/vllm/issues/13390) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vLLM support multi-task

### Issue 正文摘录

### Your current environment The env works fine. ### How would you like to use vllm I want to implement multi-task for Whisper, e.g. language detection and transcription. The source code already supports whisper transcription (forward + compute_logits + sample). I wonder if it's possible to add detect_language or add an extra parameters in parameters. Any docs or issues I can learn about how vllm support multi-task. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: sk. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
