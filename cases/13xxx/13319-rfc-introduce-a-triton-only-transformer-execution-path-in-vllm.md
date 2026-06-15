# vllm-project/vllm#13319: [RFC]: Introduce a Triton-only Transformer Execution Path in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#13319](https://github.com/vllm-project/vllm/issues/13319) |
| 状态 | closed |
| 标签 | RFC;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Introduce a Triton-only Transformer Execution Path in vLLM

### Issue 正文摘录

### Motivation. As heterogeneous hardware becomes increasingly popular—and will only continue to grow in the future—vLLM's Roadmap shows a clear trend of continuously expanding hardware support, both in the past and present. This makes it essential to establish an execution path that can seamlessly operate across all heterogeneous hardware. Clearly, CUDA and platform-specific languages are not sufficient to achieve this goal. In contrast, Triton code has been consistently designed to support various heterogeneous hardware. As long as a vendor supports Triton, our execution path can run on that vendor's chip. Additionally, vLLM has adopted Triton for the prefill and decode phases in attention, such as `triton_attention` and `triton_decode_attention`. Unfortunately, there is no fully Triton-based execution path for vLLM inference serving. As a result, we propose a fully CUDA-free/Triton-only transformer execution path in vLLM, including attention and non-attention operators, to address the aforementioned problems and keep up with the trend. ### Proposed Change. We plan to submit two major PRs to implement the Triton-only transformer execution path. Each PR will include multiple comm...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: that can seamlessly operate across all heterogeneous hardware. Clearly, CUDA and platform-specific languages are not sufficient to achieve this goal. In contrast, Triton code has been consistently designed to support va...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Introduce a Triton-only Transformer Execution Path in vLLM RFC;unstale ### Motivation. As heterogeneous hardware becomes increasingly popular—and will only continue to grow in the future—vLLM's Roadmap shows a cl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [RFC]: Introduce a Triton-only Transformer Execution Path in vLLM RFC;unstale ### Motivation. As heterogeneous hardware becomes increasingly popular—and will only continue to grow in the future—vLLM's Roadmap shows a cl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: perate across all heterogeneous hardware. Clearly, CUDA and platform-specific languages are not sufficient to achieve this goal. In contrast, Triton code has been consistently designed to support various heterogeneous h...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ludes: 1. Prefill phase implementation 2. Decode phase implementation 3. KV cache management We are currently preparing these PRs. The detailed design and list of planned changes are here: [[Design doc] Introduce a Trit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
