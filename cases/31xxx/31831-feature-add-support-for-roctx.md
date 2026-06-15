# vllm-project/vllm#31831: [Feature]: Add support for ROCTx

| 字段 | 值 |
| --- | --- |
| Issue | [#31831](https://github.com/vllm-project/vllm/issues/31831) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for ROCTx

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the pytorch profiler is unable to get the shape data of launched kernels due to a lack of annotations provided by vLLM. ROCTx support needs to be added to support more detailed profiles (e.g. kernel shape data). ### Alternatives _No response_ ### Additional context NVTX is already supported, and ROCTx only has parity with NVTX v0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add support for ROCTx feature request;stale ### 🚀 The feature, motivation and pitch Currently the pytorch profiler is unable to get the shape data of launched kernels due to a lack of annotations provided by...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: est;stale ### 🚀 The feature, motivation and pitch Currently the pytorch profiler is unable to get the shape data of launched kernels due to a lack of annotations provided by vLLM. ROCTx support needs to be added to supp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: v0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
