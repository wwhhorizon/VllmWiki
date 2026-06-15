# vllm-project/vllm#13154: [Usage]: How to optimize long text input token？

| 字段 | 值 |
| --- | --- |
| Issue | [#13154](https://github.com/vllm-project/vllm/issues/13154) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to optimize long text input token？

### Issue 正文摘录

### Your current environment The content of each group of conversations is stored as historical information, and the historical information + new questions are used as new input to ask questions. However, a problem will arise. As historical information accumulates, the time required for the first token increases. Is there any optimization solution for this? for example: ``` history: [{'role': 'user', 'content': '介绍下爱因斯坦'}] history: [{'role': 'user', 'content': '介绍下爱因斯坦'}, {'role': 'assistant', 'content': '爱因斯坦是著名的理论物理学家，最著名的是他的相对论.'}] history: [{'role': 'user', 'content': '介绍下爱因斯坦'}, {'role': 'assistant', 'content': '爱因斯坦是著名的理论物理学家，最著名的是他的相对论.'}, {'role': 'user', 'content': '你是谁?'}] ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt The content of each group of conversations is stored as historical information, and the historical information + new questions are used as new input to ask questions. However, a problem will arise. As historical info...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
