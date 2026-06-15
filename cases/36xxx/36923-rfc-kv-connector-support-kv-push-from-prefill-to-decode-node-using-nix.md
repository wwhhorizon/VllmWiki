# vllm-project/vllm#36923: [RFC]: [KV Connector]: Support KV push from Prefill to Decode node using Nixl Connector

| 字段 | 值 |
| --- | --- |
| Issue | [#36923](https://github.com/vllm-project/vllm/issues/36923) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: [KV Connector]: Support KV push from Prefill to Decode node using Nixl Connector

### Issue 正文摘录

### Motivation. The current vLLM P/D disaggregation architecture uses a **pull-based** KV transfer model: the Decode (D) node initiates a NIXL READ to pull KV blocks from the Prefill (P) node after P finishes computation. While functional, this approach has a key limitation - **D must wait for P to finish before it can begin transferring KV data**, adding latency to the critical path. In the pull model, the sequence is strictly serial: 1. Proxy sends request to P 2. P computes KV and finishes the request 3. Proxy sends request to D with P's `kv_transfer_params` 4. D allocates blocks, handshakes with P, and initiates NIXL READ 5. D begins decoding after transfer completes This serialization means D sits idle during P's computation phase. For large prompts or high-TP configurations, this idle time is significant. ### Advantages of Push Mode Push-based KV transfer builds on the existing pull infrastructure and offers several benefits: **1. Reduced TTFT through concurrent operation** With push, D can register its blocks with P while P is still computing. The moment P finishes, it WRITEs KV directly to D's pre-registered memory -- no round-trip through the proxy to relay `kv_transfer_p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: [KV Connector]: Support KV push from Prefill to Decode node using Nixl Connector RFC ### Motivation. The current vLLM P/D disaggregation architecture uses a **pull-based** KV transfer model: the Decode (D) node i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: wait for P to finish before it can begin transferring KV data**, adding latency to the critical path. In the pull model, the sequence is strictly serial: 1. Proxy sends request to P 2. P computes KV and finishes the req...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: t vLLM P/D disaggregation architecture uses a **pull-based** KV transfer model: the Decode (D) node initiates a NIXL READ to pull KV blocks from the Prefill (P) node after P finishes computation. While functional, this...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: **4. Proxy exits the transfer critical path** Push allows the proxy to dispatch to P and D simultaneously. D registers blocks directly with P via a ZMQ side channel, and P pushes when ready. The transfer coordination ha...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ime is significant. ### Advantages of Push Mode Push-based KV transfer builds on the existing pull infrastructure and offers several benefits: **1. Reduced TTFT through concurrent operation** With push, D can register i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
