# vllm-project/vllm#20323: [RFC]: Elastic Expert Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#20323](https://github.com/vllm-project/vllm/issues/20323) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Elastic Expert Parallelism

### Issue 正文摘录

### Motivation. Expert parallelism (**EP**) is a key technique in enabling high-throughput, low-latency large scale LLM serving of Mixture-of-Expert models such as DeepSeek-V3/R1. However, EP today is static in vLLM as well as many other inference frameworks: when there are more requests that exceed the current serving capacity, vLLM could not scale up to meet the demand; and when there are less requests, vLLM could not scale down to reduce GPU usage and cost. The only viable solution today is to perform a complete restart with a new configuration, which is quite slow and would drop a lot of traffic. In this RFC, we propose Elastic Expert Parallelism to address the above challenges. With Elastic EP, vLLM will be able to dynamically scale up or down based on workload fluctuations, with minimal interruption to serving. ### Proposed Change. **Background**: Expert Parallelism is closely related to Data Parallel (**DP**) Attention, please refer to [[RFC]: Data Parallel Attention and Expert Parallel MoEs](https://github.com/vllm-project/vllm/issues/16037) for background. From a high level, we propose to add the following functionality to support Elastic EP: - Bring up new DP engine-core...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: vation. Expert parallelism (**EP**) is a key technique in enabling high-throughput, low-latency large scale LLM serving of Mixture-of-Expert models such as DeepSeek-V3/R1. However, EP today is static in vLLM as well as...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: in vLLM as well as many other inference frameworks: when there are more requests that exceed the current serving capacity, vLLM could not scale up to meet the demand; and when there are less requests, vLLM could not sca...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: eworks: when there are more requests that exceed the current serving capacity, vLLM could not scale up to meet the demand; and when there are less requests, vLLM could not scale down to reduce GPU usage and cost. The on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: Elastic Expert Parallelism RFC;keep-open ### Motivation. Expert parallelism (**EP**) is a key technique in enabling high-throughput, low-latency large scale LLM serving of Mixture-of-Expert models such as DeepSee...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: igh-throughput, low-latency large scale LLM serving of Mixture-of-Expert models such as DeepSeek-V3/R1. However, EP today is static in vLLM as well as many other inference frameworks: when there are more requests that e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
