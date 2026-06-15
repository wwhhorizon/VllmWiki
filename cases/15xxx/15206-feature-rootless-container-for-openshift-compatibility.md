# vllm-project/vllm#15206: [Feature]: Rootless container for OpenShift compatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#15206](https://github.com/vllm-project/vllm/issues/15206) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Rootless container for OpenShift compatibility

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The previous iterations of the vLLM containers were runnable in OpenShift, but due to the switch to virtual Python environments, this is not possible anymore. As it was working before the switch to `venv`, I assume there are no root-privileges required to actually run the software after everything has been installed correctly. Unfortunately I'm not that familiar with `uv` and `venv` and currently don't have the time to investigate myself, so I wanted to raise this issue for awareness. Anyway, I'll try to get a PR-ready as fast as possible. ### Alternatives Keeping "regular" installation for release-containers and keep virtual environment approach for development containers. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ivileges required to actually run the software after everything has been installed correctly. Unfortunately I'm not that familiar with `uv` and `venv` and currently don't have the time to investigate myself, so I wanted...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Rootless container for OpenShift compatibility feature request ### 🚀 The feature, motivation and pitch The previous iterations of the vLLM containers were runnable in OpenShift, but due to the switch to virtu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
