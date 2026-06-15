# vllm-project/vllm#33541: [Feature]: Automatic full-core utilization for TP=1 on arm multi-NUMA CPU systems

| 字段 | 值 |
| --- | --- |
| Issue | [#33541](https://github.com/vllm-project/vllm/issues/33541) |
| 状态 | closed |
| 标签 | feature request;cpu |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Automatic full-core utilization for TP=1 on arm multi-NUMA CPU systems

### Issue 正文摘录

### 🚀 The feature, motivation and pitch On arm servers with two NUMA nodes, when tensor parallelism (TP) is set to 1, the runtime currently utilizes cores from only a single NUMA node unless VLLM_CPU_OMP_THREADS_BIND is explicitly configured. For example, on a two NUMA system with 64 cores, only cores 0–31 are active by default. With TP=2, cores are correctly partitioned across NUMA nodes without requiring any manual configuration. Requested enhancement: When TP=1, the runtime should automatically detect multi-NUMA arm systems and utilize all available CPU cores by default, eliminating the need for users to manually set VLLM_CPU_OMP_THREADS_BIND. cc: @fadara01 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tion and pitch On arm servers with two NUMA nodes, when tensor parallelism (TP) is set to 1, the runtime currently utilizes cores from only a single NUMA node unless VLLM_CPU_OMP_THREADS_BIND is explicitly configured. F...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: es from only a single NUMA node unless VLLM_CPU_OMP_THREADS_BIND is explicitly configured. For example, on a two NUMA system with 64 cores, only cores 0–31 are active by default. With TP=2, cores are correctly partition...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m only a single NUMA node unless VLLM_CPU_OMP_THREADS_BIND is explicitly configured. For example, on a two NUMA system with 64 cores, only cores 0–31 are active by default. With TP=2, cores are correctly partitioned acr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tic full-core utilization for TP=1 on arm multi-NUMA CPU systems feature request;cpu ### 🚀 The feature, motivation and pitch On arm servers with two NUMA nodes, when tensor parallelism (TP) is set to 1, the runtime curr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
