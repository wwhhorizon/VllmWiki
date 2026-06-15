# vllm-project/vllm#22244: [Bug]: I do not get the same result when predecting one token at a time and when I predecting several tokens at the same time

| 字段 | 值 |
| --- | --- |
| Issue | [#22244](https://github.com/vllm-project/vllm/issues/22244) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: I do not get the same result when predecting one token at a time and when I predecting several tokens at the same time

### Issue 正文摘录

### Your current environment why I am having different results when doing max_tokens=4 and when I am generating one token at a time sequentially? temperature=0 and top_p=1? ### 🐛 Describe the bug params = SamplingParams(temperature=0.0, top_p=1.0, max_tokens=4,detokenize=False) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s = SamplingParams(temperature=0.0, top_p=1.0, max_tokens=4,detokenize=False) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom rig...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: oken at a time and when I predecting several tokens at the same time bug;stale ### Your current environment why I am having different results when doing max_tokens=4 and when I am generating one token at a time sequenti...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
