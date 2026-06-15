# vllm-project/vllm#22183: [Bug]: downgrade the wrong platform of pytorch version, should be ppc instead aarch64

| 字段 | 值 |
| --- | --- |
| Issue | [#22183](https://github.com/vllm-project/vllm/issues/22183) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: downgrade the wrong platform of pytorch version, should be ppc instead aarch64

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/pull/21343 downgrade the wrong platform of pytorch version, should change ppc instead of aarch64. `requirements/cpu.txt` ``` torch==2.7.0; platform_machine == "ppc64le" torch==2.6.0; platform_machine == "aarch64" # for arm64 CPUs, torch 2.7.0 has a issue: https://github.com/vllm-project/vllm/issues/17960 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: downgrade the wrong platform of pytorch version, should be ppc instead aarch64 bug;stale ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/pull/21343 downgrade the wrong pla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: downgrade the wrong platform of pytorch version, should be ppc instead aarch64 bug;stale ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/pull/21343 downgrade the wrong platform o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: the wrong platform of pytorch version, should be ppc instead aarch64 bug;stale ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/pull/21343 downgrade the wrong platform of pytorch...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
