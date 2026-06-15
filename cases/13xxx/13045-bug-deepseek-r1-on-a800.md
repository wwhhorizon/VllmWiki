# vllm-project/vllm#13045: [Bug]: deepseek-r1 on A800

| 字段 | 值 |
| --- | --- |
| Issue | [#13045](https://github.com/vllm-project/vllm/issues/13045) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: deepseek-r1 on A800

### Issue 正文摘录

### Your current environment 8 *a800 * 8 vllm 0.7.1 ray ### 🐛 Describe the bug I used Ray and 8 8*A800s to run deepseek-r1, set tp=8, pp=8, gpu utilization was 0.98, but one machine's video memory usage was very low, while the other machine's usage was close to the limit. Is there any way to balance the two machines? In the follow picture， machine 1 and 3： ![Image](https://github.com/user-attachments/assets/f2a9cc14-1cfc-488e-a010-65f9394b322b) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2b) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
