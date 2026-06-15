# vllm-project/vllm#18975: [Feature]: Colocating multiple LLM engines in the same process with sleep mode.

| 字段 | 值 |
| --- | --- |
| Issue | [#18975](https://github.com/vllm-project/vllm/issues/18975) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Colocating multiple LLM engines in the same process with sleep mode.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch For vLLM verison > 0.7, when creating multiple LLM engines on the same process with sleep mode enabled, the following assertion error will be triggered: `AssertionError: Sleep mode can only be used for one instance per process.` This assertion appears in both v1/non-v1 engines, i.e., both `vllm/v1/worker/gpu_worker.py` and `vllm/worker/gpu_worker.py`. This feature is particularly useful for RL training with multiple rollout engines as different roles. Please consider enabling multiple LLM engines with sleep mode. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cating multiple LLM engines in the same process with sleep mode. feature request;stale ### 🚀 The feature, motivation and pitch For vLLM verison > 0.7, when creating multiple LLM engines on the same process with sleep mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
