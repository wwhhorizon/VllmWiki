# vllm-project/vllm#34067: [Feature]: nightly docker and wheels for ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#34067](https://github.com/vllm-project/vllm/issues/34067) |
| 状态 | closed |
| 标签 | feature request;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: nightly docker and wheels for ROCm

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently on vllm.ai page, there is no upstream nightly docker image or wheel for installation for ROCm. Glad to see vLLM upstream releases stable docker images and stable wheels for ROCm. We should support nightly docker and wheels as well. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: nightly docker and wheels for ROCm feature request;rocm ### 🚀 The feature, motivation and pitch Currently on vllm.ai page, there is no upstream nightly docker image or wheel for installation for ROCm. Glad to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: nightly docker and wheels for ROCm feature request;rocm ### 🚀 The feature, motivation and pitch Currently on vllm.ai page, there is no upstream nightly docker image or wheel for installation for ROCm. Glad to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: nightly docker and wheels for ROCm feature request;rocm ### 🚀 The feature, motivation and pitch Currently on vllm.ai page, there is no upstream nightly docker image or wheel for installation for ROCm. Glad to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
