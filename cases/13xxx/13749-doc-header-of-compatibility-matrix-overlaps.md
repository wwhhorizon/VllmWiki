# vllm-project/vllm#13749: [Doc]: header of compatibility_matrix overlaps

| 字段 | 值 |
| --- | --- |
| Issue | [#13749](https://github.com/vllm-project/vllm/issues/13749) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: header of compatibility_matrix overlaps

### Issue 正文摘录

### 📚 The doc issue I found headers of compatibility_matrix overlap. It seems `vertical-table-header` css has some problems. [compatibility_matrix](https://docs.vllm.ai/en/latest/features/compatibility_matrix.html) I test the following css and it works fine. If needed, I'd like to submit a pr to fix it. ### Suggest a potential alternative/fix ```css .vertical-table-header th.head:not(.stub) { writing-mode: sideways-lr; white-space: nowrap; p { margin: 0; } } .vertical-table-header th abbr { white-space: nowrap; } ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: css has some problems. [compatibility_matrix](https://docs.vllm.ai/en/latest/features/compatibility_matrix.html) I test the following css and it works fine. If needed, I'd like to submit a pr to fix it. ### Suggest a po...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
