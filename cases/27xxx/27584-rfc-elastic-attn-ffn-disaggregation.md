# vllm-project/vllm#27584: [RFC]: Elastic Attn-FFN Disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#27584](https://github.com/vllm-project/vllm/issues/27584) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Elastic Attn-FFN Disaggregation

### Issue 正文摘录

### Motivation. With AFD, large-scale MoE inference on vLLM runs across two execution sides: an Attention side that batches requests, manages KV cache, and performs routing, and an FFN (Experts) side that executes expert MLPs. In proposal #22799, we introduce AFD as a single instance spanning DP-Attention and EP-FFN. To further improve the online serving performance and reliability, online elasticity of AFD becomes important by keeping QoS and throughput when traffic spikes and nodes fail. Prior work (Elastic EP #20323) established online elasticity for DeepEP; coordinating AFD is broader in scope. Elastic AFD needs a new architecture that jointly coordinates Attention and FFN across control and data planes and reframes load balancing for AFD pipelines. There are two goals in this RFC: 1) We need low MTTR within one elastic AFD instance: apply live edits to Attention/FFN group membership and placement, resize DP ranks, and adjust expert placement while the service stays up. 2) We also need high throughput before and after scale in/out: tune per-node concurrency on the Attention and FFN paths by changing pipeline allocation, micro-batch distribution, threads, streams and SM utiliza...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: or DeepEP; coordinating AFD is broader in scope. Elastic AFD needs a new architecture that jointly coordinates Attention and FFN across control and data planes and reframes load balancing for AFD pipelines. There are tw...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: her improve the online serving performance and reliability, online elasticity of AFD becomes important by keeping QoS and throughput when traffic spikes and nodes fail. Prior work (Elastic EP #20323) established online...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: Attn-FFN Disaggregation RFC;stale ### Motivation. With AFD, large-scale MoE inference on vLLM runs across two execution sides: an Attention side that batches requests, manages KV cache, and performs routing, and an FFN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Elastic Attn-FFN Disaggregation RFC;stale ### Motivation. With AFD, large-scale MoE inference on vLLM runs across two execution sides: an Attention side that batches requests, manages KV cache, and performs routi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: liability, online elasticity of AFD becomes important by keeping QoS and throughput when traffic spikes and nodes fail. Prior work (Elastic EP #20323) established online elasticity for DeepEP; coordinating AFD is broade...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
