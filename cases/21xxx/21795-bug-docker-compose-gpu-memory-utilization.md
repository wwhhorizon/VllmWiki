# vllm-project/vllm#21795: [Bug]: 在docker compose里配置两个容器，gpu-memory-utilization的值问题

| 字段 | 值 |
| --- | --- |
| Issue | [#21795](https://github.com/vllm-project/vllm/issues/21795) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 在docker compose里配置两个容器，gpu-memory-utilization的值问题

### Issue 正文摘录

### Your current environment vllm 0.8.5 ### 🐛 Describe the bug 我在docker compose里配置了两个容器，加载的是同一个模型。 两个容器的gpu-memory-utilization的值都是0.48。 当查看GPU内存使用情况时，为什么看起来是两个容器总共占了GPU内存的0.48，而不是分别占0.48？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: 在docker compose里配置两个容器，gpu-memory-utilization的值问题 bug;stale ### Your current environment vllm 0.8.5 ### 🐛 Describe the bug 我在docker compose里配置了两个容器，加载的是同一个模型。 两个容器的gpu-memory-utilization的值都是0.48。 当查看GPU内存使用情况时，为什...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 48？ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: 在docker compose里配置两个容器，gpu-memory-utilization的值问题 bug;stale ### Your current environment vllm 0.8.5 ### 🐛 Describe the bug 我在docker compose里配置了两个容器，加载的是同一个模型。 两个容器的gpu-memory-utilization的值都是0.48。 当查看GPU内存使用情况时，为什...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
