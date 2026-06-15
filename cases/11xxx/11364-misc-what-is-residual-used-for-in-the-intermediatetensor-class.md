# vllm-project/vllm#11364: [Misc]: What is 'residual' used for in the IntermediateTensor class? 

| 字段 | 值 |
| --- | --- |
| Issue | [#11364](https://github.com/vllm-project/vllm/issues/11364) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: What is 'residual' used for in the IntermediateTensor class? 

### Issue 正文摘录

### Anything you want to discuss about vllm. We found that when using Pipeline Parallelism, the _IntermediateTensor_ objects passed between nodes contain a tensor volumn named 'residual', and wondering what it is used for and when it will be consumed during the inference computation. We used another framework named **Petals** for deploying LLMs in Pipeline Parallelism manner before, but Petals only sends 'hidden_states' as intermediate activation. Haven't found much information about 'residual' in the documentations. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: want to discuss about vllm. We found that when using Pipeline Parallelism, the _IntermediateTensor_ objects passed between nodes contain a tensor volumn named 'residual', and wondering what it is used for and when it wi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: y sends 'hidden_states' as intermediate activation. Haven't found much information about 'residual' in the documentations. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: What is 'residual' used for in the IntermediateTensor class? stale ### Anything you want to discuss about vllm. We found that when using Pipeline Parallelism, the _IntermediateTensor_ objects passed between node...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
