# vllm-project/vllm#11004: [Performance]: why pipeline parallel performance will be severely degraded when using offline batching?

| 字段 | 值 |
| --- | --- |
| Issue | [#11004](https://github.com/vllm-project/vllm/issues/11004) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: why pipeline parallel performance will be severely degraded when using offline batching?

### Issue 正文摘录

### Proposal to improve performance I wonder is pipeline parallel performance more efficient than tensor parallel when using offline batching, but I got `NotImplementedError: Pipeline parallelism is only supported through AsyncLLMEngine as performance will be severely degraded otherwise`. As tensor parallel uses more communication than pipeline parallel, each transformer block using at least 4 times communication in tensor parallel, but pipeline parallel only need to send activation to next stage. It seems pipeline is more efficient? But why `Pipeline parallelism is only supported through AsyncLLMEngine as performance will be severely degraded otherwise` ? ![image](https://github.com/user-attachments/assets/f5c3188d-4fa2-46a8-812d-a428e67c0872) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sing offline batching, but I got `NotImplementedError: Pipeline parallelism is only supported through AsyncLLMEngine as performance will be severely degraded otherwise`. As tensor parallel uses more communication than p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: improve performance I wonder is pipeline parallel performance more efficient than tensor parallel when using offline batching, but I got `NotImplementedError: Pipeline parallelism is only supported through AsyncLLMEngin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: arallel uses more communication than pipeline parallel, each transformer block using at least 4 times communication in tensor parallel, but pipeline parallel only need to send activation to next stage. It seems pipeline...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: mance will be severely degraded when using offline batching? performance;stale ### Proposal to improve performance I wonder is pipeline parallel performance more efficient than tensor parallel when using offline batchin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
