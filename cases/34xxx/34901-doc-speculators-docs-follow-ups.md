# vllm-project/vllm#34901: [Doc]: Speculators Docs Follow-ups

| 字段 | 值 |
| --- | --- |
| Issue | [#34901](https://github.com/vllm-project/vllm/issues/34901) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Speculators Docs Follow-ups

### Issue 正文摘录

### 📚 The doc issue The speculators documentation has recently been refactored, but is still missing many sections. Good speculation documentation will help drive users to adopt these awesome features. ### Suggest a potential alternative/fix - [ ] Add an MTP page detailing how MTP speculation works, when it's applicable, and a standardized example of how to use it in vLLM - [ ] Add some high-level performance benchmarks to the Speculators README which gives users a sense of which speculation methods are most effective and when. I recommend something like two columns, one for low QPS and one for high QPS - [ ] Fix MLP examples based on https://github.com/vllm-project/vllm/issues/34106 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: d example of how to use it in vLLM - [ ] Add some high-level performance benchmarks to the Speculators README which gives users a sense of which speculation methods are most effective and when. I recommend something lik...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 106 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
