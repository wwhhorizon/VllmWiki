# vllm-project/vllm#27325: [Bug]: When spec_tokens count is greater than 1, the adaptation of cuda_graph_sizes causes the decoding process to fall back to eager mode.

| 字段 | 值 |
| --- | --- |
| Issue | [#27325](https://github.com/vllm-project/vllm/issues/27325) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When spec_tokens count is greater than 1, the adaptation of cuda_graph_sizes causes the decoding process to fall back to eager mode.

### Issue 正文摘录

### Your current environment This issue is irrelevant to env. ### 🐛 Describe the bug In the current [codebase](https://github.com/vllm-project/vllm/blob/main/vllm/config/scheduler.py#L243), if the `cuda_graph_sizes` variable is not provided, it defaults to the minimum of `self.max_num_seqs * 2` and `512`. However, when using the `spec_decode` feature with `num_spec_tokens >= 2` (let's use 2 as an example), the number of tokens processed per decode step becomes max_num_seqs * 3, which is larger than the maximum graph size allocated for this context. In this scenario, the decoding process is forced onto the eager mode, which we believe is likely unintended and suboptimal for performance. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: _graph_sizes causes the decoding process to fall back to eager mode. bug;stale ### Your current environment This issue is irrelevant to env. ### 🐛 Describe the bug In the current [codebase](https://github.com/vllm-proje...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: When spec_tokens count is greater than 1, the adaptation of cuda_graph_sizes causes the decoding process to fall back to eager mode. bug;stale ### Your current environment This issue is irrelevant to env. ### 🐛 D...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e current [codebase](https://github.com/vllm-project/vllm/blob/main/vllm/config/scheduler.py#L243), if the `cuda_graph_sizes` variable is not provided, it defaults to the minimum of `self.max_num_seqs * 2` and `512`. Ho...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
