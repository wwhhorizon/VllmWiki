# vllm-project/vllm#2957: I use vllm to accelerate the large model of qwen, mainly qwen7B/qwen14B. Two issues were found during the testing of the large model.

| 字段 | 值 |
| --- | --- |
| Issue | [#2957](https://github.com/vllm-project/vllm/issues/2957) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> I use vllm to accelerate the large model of qwen, mainly qwen7B/qwen14B. Two issues were found during the testing of the large model.

### Issue 正文摘录

I use vllm to accelerate the large model of qwen, mainly qwen7B/qwen14B. Two issues were found during the testing of the large model. 1) Compared to using vllm qwen7B/qwen14B acceleration, the accuracy of the reasoning results of the single round question answering test model has decreased. 2) Compared to using vllm qwen7B/qwen14B acceleration, the accuracy of the inference results of the streaming output test model has decreased. The vllm version is 0.3.0

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: I use vllm to accelerate the large model of qwen, mainly qwen7B/qwen14B. Two issues were found during the testing of the large model. stale I use vllm to accelerate the large model of qwen, mainly qwen7B/qwen14B. Two is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e model of qwen, mainly qwen7B/qwen14B. Two issues were found during the testing of the large model. stale I use vllm to accelerate the large model of qwen, mainly qwen7B/qwen14B. Two issues were found during the testin...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: large model. 1) Compared to using vllm qwen7B/qwen14B acceleration, the accuracy of the reasoning results of the single round question answering test model has decreased. 2) Compared to using vllm qwen7B/qwen14B acceler...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ence results of the streaming output test model has decreased. The vllm version is 0.3.0
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 7B/qwen14B. Two issues were found during the testing of the large model. stale I use vllm to accelerate the large model of qwen, mainly qwen7B/qwen14B. Two issues were found during the testing of the large model. 1) Com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
