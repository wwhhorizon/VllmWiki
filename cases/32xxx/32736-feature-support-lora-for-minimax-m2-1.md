# vllm-project/vllm#32736: [Feature]: support lora for minimax m2.1

| 字段 | 值 |
| --- | --- |
| Issue | [#32736](https://github.com/vllm-project/vllm/issues/32736) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support lora for minimax m2.1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now (Worker_TP5_EP5 pid=1744619) ERROR 01-20 23:03:49 [multiproc_executor.py:749] ValueError: MiniMaxM2ForCausalLM does not support LoRA yet. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: support lora for minimax m2.1 feature request ### 🚀 The feature, motivation and pitch Now (Worker_TP5_EP5 pid=1744619) ERROR 01-20 23:03:49 [multiproc_executor.py:749] ValueError: MiniMaxM2ForCausalLM does no...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
