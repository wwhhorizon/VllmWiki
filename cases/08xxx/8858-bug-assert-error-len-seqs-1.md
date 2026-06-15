# vllm-project/vllm#8858: [Bug]: Assert Error: len(seqs) == 1

| 字段 | 值 |
| --- | --- |
| Issue | [#8858](https://github.com/vllm-project/vllm/issues/8858) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Assert Error: len(seqs) == 1

### Issue 正文摘录

### Your current environment vllm == 0.6.2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug /home/linli/anaconda3/envs/LLM/lib/python3.11/site-packages/vllm/core/scheduler.py line 1247 assert len(seqs) == 1 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Assert Error: len(seqs) == 1 bug;stale ### Your current environment vllm == 0.6.2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug /home/linli/anaconda3/envs/LLM/lib/python3.11/site-packages/vllm/core/s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: = 1 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: en(seqs) == 1 bug;stale ### Your current environment vllm == 0.6.2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug /home/linli/anaconda3/envs/LLM/lib/python3.11/site-packages/vllm/core/scheduler.py line 1247...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
