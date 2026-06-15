# vllm-project/vllm#28868: [Bug]: When compiling with ranges, we should pass the range information to Inductor

| 字段 | 值 |
| --- | --- |
| Issue | [#28868](https://github.com/vllm-project/vllm/issues/28868) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When compiling with ranges, we should pass the range information to Inductor

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug Might be more of a feature request. Context is that https://github.com/vllm-project/vllm/pull/24248 adds a new compile ranges API, where a user can specify which ranges to compile on. We should tell Inductor how to constrain the compilation on the symints of the compile ranges ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: with ranges, we should pass the range information to Inductor bug;torch.compile;stale ### Your current environment main ### 🐛 Describe the bug Might be more of a feature request. Context is that https://github.com/vllm-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nges, we should pass the range information to Inductor bug;torch.compile;stale ### Your current environment main ### 🐛 Describe the bug Might be more of a feature request. Context is that https://github.com/vllm-project...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ges ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: When compiling with ranges, we should pass the range information to Inductor bug;torch.compile;stale ### Your current environment main ### 🐛 Describe the bug Might be more of a feature request. Context is that ht...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
