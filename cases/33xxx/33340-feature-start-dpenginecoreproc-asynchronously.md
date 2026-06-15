# vllm-project/vllm#33340: [Feature]: start DPEngineCoreProc asynchronously

| 字段 | 值 |
| --- | --- |
| Issue | [#33340](https://github.com/vllm-project/vllm/issues/33340) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: start DPEngineCoreProc asynchronously

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Motivation Currently, vllm launches each DPEngineCoreProc in a synchronous manner. This issue proposed starting DPEngineCoreProc in a asynchronous manner, which would improve service startup speed ### Proposed Implementation Details **utils.py** - Add start_async to execute all DPEngineCoreProc process start - Add _enginecore_bootstrap to set device id and call EngineCoreProc.run_engine_core - Use ThreadPoolExecutor to run start_async This implementation set device id after starting subprocess, which is not satisfying [https://github.com/vllm-project/vllm/pull/21211](url). ### Future Work Hope for some suggestion about the implementation to start DPEngineCoreProc in a asynchronous manner correctly. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: start DPEngineCoreProc asynchronously feature request;stale ### 🚀 The feature, motivation and pitch ### Motivation Currently, vllm launches each DPEngineCoreProc in a synchronous manner. This issue proposed s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
