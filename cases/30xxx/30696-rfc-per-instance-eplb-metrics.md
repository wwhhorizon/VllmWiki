# vllm-project/vllm#30696: [RFC]: Per-instance EPLB metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#30696](https://github.com/vllm-project/vllm/issues/30696) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Per-instance EPLB metrics

### Issue 正文摘录

### 🚀 The feature, motivation and pitch (co-authored with @sallyom and Claude) In replicated vLLM deployments behind a load balancer, the load balancer has no visibility into EPLB (Expert-Parallel Load Balancing) state when making routing decisions. EPLB dynamically replicates heavily-used experts across EP ranks to balance load, and instances experiencing high expert load imbalance or active rebalancing operations have degraded capacity. Without metrics exposing this state, load balancers cannot avoid routing traffic to struggling instances, leading to suboptimal performance and increased tail latencies. EPLB already tracks and logs this information to stdout when `--eplb-log-balancedness` is enabled: ``` EPLB step: 2500: avg_tokens=1024, max_tokens=2048, balancedness=0.5000 ``` But these are obviously not queryable by load balancers. This proposal exports the same data that's currently logged as Prometheus metrics, enabling intelligent load balancing decisions based on instance health. Note - these stats are EP-group-wide, and should not be reported per-engine (i.e. with the `engine_idx` label), instead they should probably only be recorded on DP rank 0. ## Proposed Metrics | Me...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: s behind a load balancer, the load balancer has no visibility into EPLB (Expert-Parallel Load Balancing) state when making routing decisions. EPLB dynamically replicates heavily-used experts across EP ranks to balance l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: visibility into EPLB (Expert-Parallel Load Balancing) state when making routing decisions. EPLB dynamically replicates heavily-used experts across EP ranks to balance load, and instances experiencing high expert load im...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the load balancer has no visibility into EPLB (Expert-Parallel Load Balancing) state when making routing decisions. EPLB dynamically replicates heavily-used experts across EP ranks to balance load, and instances experie...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: mance and increased tail latencies. EPLB already tracks and logs this information to stdout when `--eplb-log-balancedness` is enabled: ``` EPLB step: 2500: avg_tokens=1024, max_tokens=2048, balancedness=0.5000 ``` But t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
