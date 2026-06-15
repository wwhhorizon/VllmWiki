# vllm-project/vllm#16742: [Feature]: AMD Ryzen AI NPU support

| 字段 | 值 |
| --- | --- |
| Issue | [#16742](https://github.com/vllm-project/vllm/issues/16742) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: AMD Ryzen AI NPU support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Are there any plans to support AMD NPUs? These might not be ultra fast but are extremely power efficient and good for prompt processing. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: AMD Ryzen AI NPU support feature request;stale ### 🚀 The feature, motivation and pitch Are there any plans to support AMD NPUs? These might not be ultra fast but are extremely power efficient and good for pro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: port AMD NPUs? These might not be ultra fast but are extremely power efficient and good for prompt processing. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
