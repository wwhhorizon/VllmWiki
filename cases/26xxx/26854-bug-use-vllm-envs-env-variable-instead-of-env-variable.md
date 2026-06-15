# vllm-project/vllm#26854: [Bug]: Use vllm.envs.ENV_VARIABLE instead of ENV_VARIABLE

| 字段 | 值 |
| --- | --- |
| Issue | [#26854](https://github.com/vllm-project/vllm/issues/26854) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Use vllm.envs.ENV_VARIABLE instead of ENV_VARIABLE

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug Avoid directly using TYPE_CHECKING environment variables in the code (by updating all code with from vllm.envs import FOO_BAR). And use envs.FOO_BAR instead, which go through the envs.__getattr__ which has 2 benefits: - no extra overhead, as environment variable caching is added in https://github.com/vllm-project/vllm/pull/26146 - using __getattr__ ensured we adopted environment variable updates during service startup time. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ironment variables in the code (by updating all code with from vllm.envs import FOO_BAR). And use envs.FOO_BAR instead, which go through the envs.__getattr__ which has 2 benefits: - no extra overhead, as environment var...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: me. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Use vllm.envs.ENV_VARIABLE instead of ENV_VARIABLE bug;stale ### Your current environment N/A ### 🐛 Describe the bug Avoid directly using TYPE_CHECKING environment variables in the code (by updating all code with...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
