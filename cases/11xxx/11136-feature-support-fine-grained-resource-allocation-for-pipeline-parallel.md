# vllm-project/vllm#11136: [Feature]: Support fine grained resource allocation for pipeline parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#11136](https://github.com/vllm-project/vllm/issues/11136) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support fine grained resource allocation for pipeline parallelism

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In the context of pipeline parallelism (PP), the communication bandwidth between GPUs is critically important due to varying GPU to GPU topologies. As a Ray application, the scheduler needs more detailed information to effectively manage resource allocation and enhance performance. The current Ray scheduler may not fully account for these nuances, which can lead to suboptimal performance, especially in bandwidth-sensitive scenarios. I propose enhancing placement and scheduling to support more fine-grained resource allocation for applications in pipeline parallelism scenarios. Specifically, vLLM should provide Ray with more detailed information about the communication requirements. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: upport fine grained resource allocation for pipeline parallelism feature request;stale ### 🚀 The feature, motivation and pitch In the context of pipeline parallelism (PP), the communication bandwidth between GPUs is cri...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: parallelism (PP), the communication bandwidth between GPUs is critically important due to varying GPU to GPU topologies. As a Ray application, the scheduler needs more detailed information to effectively manage resource...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Feature]: Support fine grained resource allocation for pipeline parallelism feature request;stale ### 🚀 The feature, motivation and pitch In the context of pipeline parallelism (PP), the communication bandwidth between...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: PU topologies. As a Ray application, the scheduler needs more detailed information to effectively manage resource allocation and enhance performance. The current Ray scheduler may not fully account for these nuances, wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
