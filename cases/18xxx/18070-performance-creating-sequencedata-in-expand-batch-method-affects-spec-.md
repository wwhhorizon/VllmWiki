# vllm-project/vllm#18070: [Performance]: Creating SequenceData in `expand_batch` method affects spec_decoding performance

| 字段 | 值 |
| --- | --- |
| Issue | [#18070](https://github.com/vllm-project/vllm/issues/18070) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Creating SequenceData in `expand_batch` method affects spec_decoding performance

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hello, I am working on improve performance of spec_decode. I found that runtime overhead is mainly at creating SequenceData. ![Image](https://github.com/user-attachments/assets/271fa188-48bc-480b-8897-069fe92df6ba) I want to know if it is possible to avoid creating so many SequenceData in spec_decode and be able to dispatch scorer decoding at the same time. ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance Hello, I am working on improve performance of spec_decode. I found that runtime overhead...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ble to avoid creating so many SequenceData in spec_decode and be able to dispatch scorer decoding at the same time. ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ssion on performance Hello, I am working on improve performance of spec_decode. I found that runtime overhead is mainly at creating SequenceData. ![Image](https://github.com/user-attachments/assets/271fa188-48bc-480b-88...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
