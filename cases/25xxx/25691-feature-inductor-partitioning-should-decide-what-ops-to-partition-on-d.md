# vllm-project/vllm#25691: [Feature]: Inductor partitioning should decide what ops to partition on dynamically

| 字段 | 值 |
| --- | --- |
| Issue | [#25691](https://github.com/vllm-project/vllm/issues/25691) |
| 状态 | closed |
| 标签 | help wanted;feature request;torch.compile |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Inductor partitioning should decide what ops to partition on dynamically

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, if `use_inductor_graph_partition` is set, we always partition on attention by making it cudagraph unsafe - instead we should respect `splitting_ops` (or likely make a new field). Use `register_should_partition_rule` from pytorch/pytorch#163310 and pytorch/pytorch#163395. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Inductor partitioning should decide what ops to partition on dynamically help wanted;feature request;torch.compile ### 🚀 The feature, motivation and pitch Currently, if `use_inductor_graph_partition` is set,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r_graph_partition` is set, we always partition on attention by making it cudagraph unsafe - instead we should respect `splitting_ops` (or likely make a new field). Use `register_should_partition_rule` from pytorch/pytor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g should decide what ops to partition on dynamically help wanted;feature request;torch.compile ### 🚀 The feature, motivation and pitch Currently, if `use_inductor_graph_partition` is set, we always partition on attentio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
