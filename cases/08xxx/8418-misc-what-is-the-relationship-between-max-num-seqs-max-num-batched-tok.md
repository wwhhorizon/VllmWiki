# vllm-project/vllm#8418: [Misc]: What is the relationship between max-num-seqs, max-num-batched-tokens and max-model-len?

| 字段 | 值 |
| --- | --- |
| Issue | [#8418](https://github.com/vllm-project/vllm/issues/8418) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: What is the relationship between max-num-seqs, max-num-batched-tokens and max-model-len?

### Issue 正文摘录

### Anything you want to discuss about vllm. 1. If max-num-seqs refers to the maximum number of sequences per batch, and max-model-len controls the max tokens per sequence, can the maximum number of tokens processed per batch be calculated as max-num-seqs*max-model-len? 2. If the answer to the above is yes, how does max-num-batched-tokens relate to max-num-seqs*max-model-len? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Misc]: What is the relationship between max-num-seqs, max-num-batched-tokens and max-model-len? stale ### Anything you want to discuss about vllm. 1. If max-num-seqs refers to the maximum number of sequences per batch,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is the relationship between max-num-seqs, max-num-batched-tokens and max-model-len? stale ### Anything you want to discuss about vllm. 1. If max-num-seqs refers to the maximum number of sequences per batch, and max-mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tionship between max-num-seqs, max-num-batched-tokens and max-model-len? stale ### Anything you want to discuss about vllm. 1. If max-num-seqs refers to the maximum number of sequences per batch, and max-model-len contr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
