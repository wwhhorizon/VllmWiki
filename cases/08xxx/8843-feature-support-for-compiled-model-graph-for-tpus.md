# vllm-project/vllm#8843: [Feature]: Support for compiled model graph for TPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#8843](https://github.com/vllm-project/vllm/issues/8843) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for compiled model graph for TPUs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch A very naive question, is there any way to get or download the compiled LLM model graph for TPUs, so that we can bypass the time consuming step of graph compilation on TPU VMs. What I am trying to find out is that can I compile the (model + Hardware) graph on the CPU and execute that on TPU cluster. Thank you so much for considering. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support for compiled model graph for TPUs feature request;stale ### 🚀 The feature, motivation and pitch A very naive question, is there any way to get or download the compiled LLM model graph for TPUs, so tha...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Support for compiled model graph for TPUs feature request;stale ### 🚀 The feature, motivation and pitch A very naive question, is there any way to get or download the compiled LLM model graph for TPUs, so tha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support for compiled model graph for TPUs feature request;stale ### 🚀 The feature, motivation and pitch A very naive question, is there any way to get or download the compiled LLM model graph for TPUs, so tha...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
