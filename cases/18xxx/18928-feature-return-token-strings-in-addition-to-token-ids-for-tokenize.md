# vllm-project/vllm#18928: [Feature]: Return token strings in addition to token ids for /tokenize

| 字段 | 值 |
| --- | --- |
| Issue | [#18928](https://github.com/vllm-project/vllm/issues/18928) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Return token strings in addition to token ids for /tokenize

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently /tokenize return array of token ids ``` "tokens": [ 50258, 50363, 16216 ], ``` Can it also return the token strings, e.g. ``` "token_strs": [ "this", " is", " a" ], ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: re]: Return token strings in addition to token ids for /tokenize feature request ### 🚀 The feature, motivation and pitch Currently /tokenize return array of token ids ``` "tokens": [ 50258, 50363, 16216 ], ``` Can it al...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
