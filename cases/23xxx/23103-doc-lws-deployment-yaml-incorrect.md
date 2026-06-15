# vllm-project/vllm#23103: [Doc]: LWS deployment yaml incorrect

| 字段 | 值 |
| --- | --- |
| Issue | [#23103](https://github.com/vllm-project/vllm/issues/23103) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: LWS deployment yaml incorrect

### Issue 正文摘录

### 📚 The doc issue The yaml for the LWS (LeaderWorkerSet) integration is slightly incorrect: https://docs.vllm.ai/en/latest/deployment/frameworks/lws.html The displayed yaml creates two sets of leaders with one worker for each set. This renders the description incorrect. You would need to have 4 machines with 8 GPUs each for this configuration to work. It would be correct to have 1 leader with one worker each to reflect the config described at the top of the page. ### Suggest a potential alternative/fix I have tested and fixed the yaml locally. I'll open a PR in a minute. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: te. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n incorrect. You would need to have 4 machines with 8 GPUs each for this configuration to work. It would be correct to have 1 leader with one worker each to reflect the config described at the top of the page. ### Sugge...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: WorkerSet) integration is slightly incorrect: https://docs.vllm.ai/en/latest/deployment/frameworks/lws.html The displayed yaml creates two sets of leaders with one worker for each set. This renders the description incor...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
