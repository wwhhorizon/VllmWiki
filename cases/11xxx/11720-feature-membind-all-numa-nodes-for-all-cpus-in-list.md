# vllm-project/vllm#11720: [Feature]: membind all NUMA nodes for all CPUs in list

| 字段 | 值 |
| --- | --- |
| Issue | [#11720](https://github.com/vllm-project/vllm/issues/11720) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: membind all NUMA nodes for all CPUs in list

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When specifying VLLM_CPU_OMP_THREADS_BIND it might be better if vLLM did a membind to all or the nodes related to the CPU list rather than just doing it to the node associated with first CPU in the list. ### Alternatives Using numactl and OMP environment variables (i.e. OMP_PLACES, etc...) give better overall control of binding but isn't compatible with CPU tensor parallel partitioning. ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: membind all NUMA nodes for all CPUs in list feature request;stale ### 🚀 The feature, motivation and pitch When specifying VLLM_CPU_OMP_THREADS_BIND it might be better if vLLM did a membind to all or the nodes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t feature request;stale ### 🚀 The feature, motivation and pitch When specifying VLLM_CPU_OMP_THREADS_BIND it might be better if vLLM did a membind to all or the nodes related to the CPU list rather than just doing it to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
