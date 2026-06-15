# vllm-project/vllm#14587: [Bug]: [V1] Beam Search Test Fails on V1

| 字段 | 值 |
| --- | --- |
| Issue | [#14587](https://github.com/vllm-project/vllm/issues/14587) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [V1] Beam Search Test Fails on V1

### Issue 正文摘录

### Your current environment Per note. It would be great if someone could look into this! ### 🐛 Describe the bug ```bash pytest VLLM_USE_V1=1 tests/samplers/test_beam_search.py ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: [V1] Beam Search Test Fails on V1 bug;stale ### Your current environment Per note. It would be great if someone could look into this! ### 🐛 Describe the bug ```bash pytest VLLM_USE_V1=1 tests/samplers/test_beam_s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: [V1] Beam Search Test Fails on V1 bug;stale ### Your current environment Per note. It would be great if someone could look into this! ### 🐛 Describe the bug ```bash pytest VLLM_USE_V1=1 tests/samplers/test_beam_s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: [V1] Beam Search Test Fails on V1 bug;stale ### Your current environment Per note. It would be great if someone could look into this! ### 🐛 Describe the bug ```bash pytest VLLM_USE_V1=1 tests/samplers/test_beam_s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
