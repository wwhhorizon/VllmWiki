# vllm-project/vllm#20817: [Bug]: Collecting profile data can lead to a 30% performance degradation.

| 字段 | 值 |
| --- | --- |
| Issue | [#20817](https://github.com/vllm-project/vllm/issues/20817) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Collecting profile data can lead to a 30% performance degradation.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug export VLLM_TORCH_PROFILER_DIR=PROFILER_DIR ``` llm.start_profile() llm.generate() llm.stop_profile() ``` It will result in a performance degradation of approximately 30%, making performance analysis impossible. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Collecting profile data can lead to a 30% performance degradation. bug;stale ### Your current environment ### 🐛 Describe the bug export VLLM_TORCH_PROFILER_DIR=PROFILER_DIR ``` llm.start_profile() llm.generate()...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : Collecting profile data can lead to a 30% performance degradation. bug;stale ### Your current environment ### 🐛 Describe the bug export VLLM_TORCH_PROFILER_DIR=PROFILER_DIR ``` llm.start_profile() llm.generate() llm.s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
