# vllm-project/vllm#29735: [Usage]:Accessing free_blocks count from LLMEngine or LLM ?

| 字段 | 值 |
| --- | --- |
| Issue | [#29735](https://github.com/vllm-project/vllm/issues/29735) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:Accessing free_blocks count from LLMEngine or LLM ?

### Issue 正文摘录

### Your current environment ```text None ``` ### How would you like to use vllm I'm doing research on key-value caching optimization. I want to know how to determine the number of free blocks during runtime. I tried manually creating the engine, but I couldn't find the method after searching through the code. AI keeps providing methods that have already been abandoned. I would be very grateful for any help, as this has been puzzling me for hours. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ent ```text None ``` ### How would you like to use vllm I'm doing research on key-value caching optimization. I want to know how to determine the number of free blocks during runtime. I tried manually creating the engin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Usage]:Accessing free_blocks count from LLMEngine or LLM ? usage ### Your current environment ```text None ``` ### How would you like to use vllm I'm doing research on key-value caching optimization. I want to know how...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
