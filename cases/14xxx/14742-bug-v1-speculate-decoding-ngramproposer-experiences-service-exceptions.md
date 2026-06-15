# vllm-project/vllm#14742: [Bug]: v1 speculate decoding NgramProposer experiences service exceptions during stress testing

| 字段 | 值 |
| --- | --- |
| Issue | [#14742](https://github.com/vllm-project/vllm/issues/14742) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v1 speculate decoding NgramProposer experiences service exceptions during stress testing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/04236ae9-b618-40b7-b42c-1800a476d80b) Force the `propose` function to always output `np.array([87, 15, 284, 16752])` upon each invocation, and under long-term stress testing, an exception occurred. ![Image](https://github.com/user-attachments/assets/50319513-c297-4777-8865-c9f5c82b179c) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 9c) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: late decoding NgramProposer experiences service exceptions during stress testing bug ### Your current environment ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/04236ae9-b618-40b7-b42c-1800a4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
