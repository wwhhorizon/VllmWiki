# vllm-project/vllm#10727: [RFC]: Implement disaggregated prefilling using Mooncake

| 字段 | 值 |
| --- | --- |
| Issue | [#10727](https://github.com/vllm-project/vllm/issues/10727) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Implement disaggregated prefilling using Mooncake

### Issue 正文摘录

### Motivation. Disaggregated prefilling/decoding is expected to achieve better performance (e.g., long documents) in LLM inference. [#5557](https://github.com/vllm-project/vllm/issues/5557) proposes a good paradigm. In addition, the Transfer Engine of [Mooncake](https://github.com/kvcache-ai/mooncake), which is a KVCache-centric disaggregated architecture for LLM serving, is open-sourced. Compared with NCCL, Mooncake Transfer Engine has the following features: - a unified programming interface for data transfers between DRAM-to-DRAM (both local and remote), DRAM-to-GPU VRAM (both local and remote), and DRAM-to-remote NVMe devices - support for TCP, RDMA, and NVMe-of protocols - topology-aware path selection (link to our english doc, transfer_engine.md), aggregating bandwidth from multiple NICs ### Proposed Change. The plan is to integrate vLLM with Mooncake. Initially we have implemented a prototype that replaces nccl with Transfer Engine in the data plane. In the future, we are planning to develop Mooncake Store to fully support disaggregated prefilling (M prefill & N decode) and make it ready for production. Mooncake's architecture is [here](https://github.com/kvcache-ai/Moonca...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Implement disaggregated prefilling using Mooncake RFC;stale ### Motivation. Disaggregated prefilling/decoding is expected to achieve better performance (e.g., long documents) in LLM inference. [#5557](https://git...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rt for TCP, RDMA, and NVMe-of protocols - topology-aware path selection (link to our english doc, transfer_engine.md), aggregating bandwidth from multiple NICs ### Proposed Change. The plan is to integrate vLLM with Moo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ithub.com/kvcache-ai/mooncake), which is a KVCache-centric disaggregated architecture for LLM serving, is open-sourced. Compared with NCCL, Mooncake Transfer Engine has the following features: - a unified programming in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
