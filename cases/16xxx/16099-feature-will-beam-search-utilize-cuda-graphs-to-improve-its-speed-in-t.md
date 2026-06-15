# vllm-project/vllm#16099: [Feature]: Will beam search utilize CUDA graphs to improve its speed in the future?

| 字段 | 值 |
| --- | --- |
| Issue | [#16099](https://github.com/vllm-project/vllm/issues/16099) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Will beam search utilize CUDA graphs to improve its speed in the future?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have noticed that beam search does not currently use CUDA graphs, which means it cannot benefit from paged attention. Will beam search utilize CUDA graphs to improve its speed in the future? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Will beam search utilize CUDA graphs to improve its speed in the future? feature request;stale ### 🚀 The feature, motivation and pitch I have noticed that beam search does not currently use CUDA graphs, which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: m search utilize CUDA graphs to improve its speed in the future? feature request;stale ### 🚀 The feature, motivation and pitch I have noticed that beam search does not currently use CUDA graphs, which means it cannot be...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance attention_kv_cache;frontend_api attention;cuda 🚀 The feature, motivation...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
