# vllm-project/vllm#14197: [Bug]: Port is still open after crashing vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#14197](https://github.com/vllm-project/vllm/issues/14197) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Port is still open after crashing vllm

### Issue 正文摘录

### Your current environment . ### 🐛 Describe the bug I ran my code using vllm and after it has crashed and even if it is correct and I terminate it by ctrl+c, on second launch of same code I got an error: `OSError: [Errno 98] Address already in use` even after 10-15 minutes of crash. I've seen this commit [#10012](https://github.com/vllm-project/vllm/pull/10012) with adding socket closing line but seems like it doesn't help. How to fix it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
