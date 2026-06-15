# vllm-project/vllm#39609: [Bug]: ImportError: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found

| 字段 | 值 |
| --- | --- |
| Issue | [#39609](https://github.com/vllm-project/vllm/issues/39609) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ImportError: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I meet this error using the latest nightly wheel. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: ImportError: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found bug ### Your current environment ### 🐛 Describe the bug I meet this error using the latest nightly wheel. ### Before submitting a new is
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: l. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nt environment ### 🐛 Describe the bug I meet this error using the latest nightly wheel. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
