# vllm-project/vllm#37988: [Bug]: minimax-m2.5, reasoning token result in negative values

| 字段 | 值 |
| --- | --- |
| Issue | [#37988](https://github.com/vllm-project/vllm/issues/37988) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: minimax-m2.5, reasoning token result in negative values

### Issue 正文摘录

### Your current environment vllm version: v0.17.0 model name: MiniMax-M2.5 I followed the reasoning tokens in the CompletionTokensDetails fixed by vllm on the official website, but minimax-m2.5 calculation always yielded negative values ### 🐛 Describe the bug Using reasoning_parser to show reasoning_token of MiniMax-M2.5 and receive results like -12 or 0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g token result in negative values bug ### Your current environment vllm version: v0.17.0 model name: MiniMax-M2.5 I followed the reasoning tokens in the CompletionTokensDetails fixed by vllm on the official website, but...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: negative values bug ### Your current environment vllm version: v0.17.0 model name: MiniMax-M2.5 I followed the reasoning tokens in the CompletionTokensDetails fixed by vllm on the official website, but minimax-m2.5 calc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
