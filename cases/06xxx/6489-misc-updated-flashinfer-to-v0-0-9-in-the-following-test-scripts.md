# vllm-project/vllm#6489: [Misc] Updated flashinfer to v0.0.9 in the following test scripts:

| 字段 | 值 |
| --- | --- |
| Issue | [#6489](https://github.com/vllm-project/vllm/issues/6489) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc] Updated flashinfer to v0.0.9 in the following test scripts:

### Issue 正文摘录

### Anything you want to discuss about vllm. Updated flashinfer to v0.0.9 in the following test scripts: - Async Engine, Inputs, Utils, Worker Test - Tensorizer, Metrics, Tracing Test - Basic Correctness Test - Core Test - Distributed Tests (2 GPUs) - Distributed Tests (4 GPUs) - Kernels Test - Models Test - Vision Language Models Test This update ensures compatibility with the latest flashinfer version.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ts: - Async Engine, Inputs, Utils, Worker Test - Tensorizer, Metrics, Tracing Test - Basic Correctness Test - Core Test - Distributed Tests (2 GPUs) - Distributed Tests (4 GPUs) - Kernels Test - Models Test - Vision Lan...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Misc] Updated flashinfer to v0.0.9 in the following test scripts: stale ### Anything you want to discuss about vllm. Updated flashinfer to v0.0.9 in the following test scripts: - Async Engine, Inputs, Utils, Worker Tes...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Distributed Tests (2 GPUs) - Distributed Tests (4 GPUs) - Kernels Test - Models Test - Vision Language Models Test This update ensures compatibility with the latest flashinfer version.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc] Updated flashinfer to v0.0.9 in the following test scripts: stale ### Anything you want to discuss about vllm. Updated flashinfer to v0.0.9 in the following test scripts: - Async Engine, Inputs, Utils, Worker Tes...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Misc] Updated flashinfer to v0.0.9 in the following test scripts: stale ### Anything you want to discuss about vllm. Updated flashinfer to v0.0.9 in the following test scripts: - Async Engine, Inputs, Utils, Worker Tes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
