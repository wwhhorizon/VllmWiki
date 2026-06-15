# vllm-project/vllm#13209: [Bug]: WARNING 02-13 07:19:11 scheduler.py:949] Input prompt (32889 tokens) is too long and exceeds limit of 2048

| 字段 | 值 |
| --- | --- |
| Issue | [#13209](https://github.com/vllm-project/vllm/issues/13209) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: WARNING 02-13 07:19:11 scheduler.py:949] Input prompt (32889 tokens) is too long and exceeds limit of 2048

### Issue 正文摘录

### Your current environment vllm:0.7.2 it's a problem! ### 🐛 Describe the bug INFO 02-13 07:19:11 async_llm_engine.py:211] Added request chatcmpl-59c408fd038b4931bcaa80f61817574b. WARNING 02-13 07:19:11 scheduler.py:949] Input prompt (32889 tokens) is too long and exceeds limit of 2048 INFO 02-13 07:19:11 async_llm_engine.py:179] Finished request chatcmpl-59c408fd038b4931bcaa80f61817574b. And there is no output. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: WARNING 02-13 07:19:11 scheduler.py:949] Input prompt (32889 tokens) is too long and exceeds limit of 2048 bug;stale ### Your current environment vllm:0.7.2 it's a problem! ### 🐛 Describe the bug INFO 02-13 07:19...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ut. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
