# vllm-project/vllm#13120: [Usage]: How to use breakpoints with VLLM to debug

| 字段 | 值 |
| --- | --- |
| Issue | [#13120](https://github.com/vllm-project/vllm/issues/13120) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use breakpoints with VLLM to debug

### Issue 正文摘录

### Your current environment None ### How would you like to use vllm It seems like the execution of vllm is managed through a compiled engine, which makes it challenging to directly debug within an IDE using breakpoints. When debugging some custom funcs to the vllm, is there any way that we could disable compilation and just set breakpoints like normal python scripts? Thank you for your help! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ke to use vllm It seems like the execution of vllm is managed through a compiled engine, which makes it challenging to directly debug within an IDE using breakpoints. When debugging some custom funcs to the vllm, is the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lp! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
