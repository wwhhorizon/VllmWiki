# vllm-project/vllm#25170: [Feature]: support chunked prefill on non-x86 platform

| 字段 | 值 |
| --- | --- |
| Issue | [#25170](https://github.com/vllm-project/vllm/issues/25170) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support chunked prefill on non-x86 platform

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently chunked prefill only works on x86 CPU, as shown in [source code](https://github.com/vllm-project/vllm/blob/fbd6523ac00082c398dc8126434cede595169609/vllm/engine/arg_utils.py#L1178). This feature request is to support chunked prefill on non-x86 CPUs like Arm. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: support chunked prefill on non-x86 platform feature request;stale ### 🚀 The feature, motivation and pitch Currently chunked prefill only works on x86 CPU, as shown in [source code](https://github.com/vllm-pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
