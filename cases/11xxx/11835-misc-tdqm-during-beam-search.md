# vllm-project/vllm#11835: [Misc]: tdqm during beam_search

| 字段 | 值 |
| --- | --- |
| Issue | [#11835](https://github.com/vllm-project/vllm/issues/11835) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: tdqm during beam_search

### Issue 正文摘录

### Anything you want to discuss about vllm. I would like to use the 'use_tqdm' feature with the 'beam_search' method. However, it appears that 'use_tqdm' is currently only supported for the 'generate' method. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Misc]: tdqm during beam_search stale ### Anything you want to discuss about vllm. I would like to use the 'use_tqdm' feature with the 'beam_search' method. However, it appears that 'use_tqdm' is currently only supporte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: tdqm during beam_search stale ### Anything you want to discuss about vllm. I would like to use the 'use_tqdm' feature with the 'beam_search' method. However, it appears that 'use_tqdm' is currently only supporte...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
