# vllm-project/vllm#9966: [Misc]: What is the use of profile run?

| 字段 | 值 |
| --- | --- |
| Issue | [#9966](https://github.com/vllm-project/vllm/issues/9966) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: What is the use of profile run?

### Issue 正文摘录

### Anything you want to discuss about vllm. I don't quite understnad the use of profile run when initing the llm_engine, can anyone give me some hints? I did not discover any related discussions. Thanks. https://github.com/vllm-project/vllm/blob/3bb4befea7166850bdee3f72fe060c9c4044ba85/vllm/engine/multiprocessing/engine.py#L224-L247 https://github.com/vllm-project/vllm/blob/3bb4befea7166850bdee3f72fe060c9c4044ba85/vllm/engine/multiprocessing/engine.py#L339-L343 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Misc]: What is the use of profile run? ### Anything you want to discuss about vllm. I don't quite understnad the use of profile run when initing the llm_engine, can anyone give me some hints? I did not discover any rel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 343 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
