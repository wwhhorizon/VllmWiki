# vllm-project/vllm#28912: [RFC]: Support Context Pipeline Parallelism(CPP).

| 字段 | 值 |
| --- | --- |
| Issue | [#28912](https://github.com/vllm-project/vllm/issues/28912) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support Context Pipeline Parallelism(CPP).

### Issue 正文摘录

### Motivation. Currently, vLLM is supporting DCP and will support PCP to enhance long-sequence inference capabilities and optimize inference efficiency. However, in scenarios with varying sequence lengths, Context Parallelism performs poorly and may even lead to overall performance degradation. Additionally, to support and optimize ultra-long sequence inputs (e.g., reaching 1M tokens or more), introducing a new partitioning dimension is necessary. For ultra-long and variable-length sequence scenarios, combining Context Pipeline Parallelism(CPP, or named Chunked Pipeline Parallelism, Sequence Pipeline Parallelism) with an SLO-based scheduling strategy can achieve better overall inference performance. For reference, see the paper: [2409.17264](https://arxiv.org/abs/2409.17264v4). tldr: CPP is a kind of fine-grained PP with computational-load-based chunked prefill strategy. Here, we'd like to introduce CPP first and then gradually optimize the SLO-based priority scheduling strategy. ### Vanilla PP Currently, the pipeline parallelism implemented in vLLM operates as shown in the figure below. Each PP rank device has an independent scheduler that processes and selects requests to form...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: CPP is a kind of fine-grained PP with computational-load-based chunked prefill strategy. Here, we'd like to introduce CPP first and then gradually optimize the SLO-based priority scheduling strategy. ### Vanilla PP Curr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Support Context Pipeline Parallelism(CPP). RFC ### Motivation. Currently, vLLM is supporting DCP and will support PCP to enhance long-sequence inference capabilities and optimize inference efficiency. However, in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: worker` and `scheduler` components, along with minor adjustments such as configuration options. The changes to the `gpu_worker` will mainly focus on the `Worker.execute_model` function, where the Pipeline Parallelism gr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: enhance long-sequence inference capabilities and optimize inference efficiency. However, in scenarios with varying sequence lengths, Context Parallelism performs poorly and may even lead to overall performance degradati...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e, there are currently four known types of bubbles: - Bubble0: caused by blocking synchronous communication. - Bubble1: caused by synchronous schedulers (asynchronous schedulers are currently under development). - Bubbl...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
