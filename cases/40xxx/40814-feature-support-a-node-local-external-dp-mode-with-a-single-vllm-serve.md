# vllm-project/vllm#40814: [Feature]: Support a node-local external DP mode with a single `vllm serve` and aggregated admin health endpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#40814](https://github.com/vllm-project/vllm/issues/40814) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support a node-local external DP mode with a single `vllm serve` and aggregated admin health endpoint

### Issue 正文摘录

### 🚀 The feature, motivation and pitch as described in [llm-d/guides/wide-ep-lws/experimental-dp-aware at main · llm-d/llm-d](https://github.com/llm-d/llm-d/tree/main/guides/wide-ep-lws/experimental-dp-aware) , we currently have DP-aware Dp/Ep scheduling in llm-d as experimental, because our launch mechanism does not interact well with K8s service health checking, etc We should instead have a single server launch command in vllm that intersects well with k8s startup and health checking probes ## Proposal Add a new **node-local external DP mode** in `vLLM` with the following behavior: - a single `vllm serve` command runs **one supervisor per node** - that supervisor launches **one child API server per local DP rank** - each child rank still exposes its own endpoint/port, so external routers can target ranks directly - the supervisor exposes an **admin endpoint** for aggregated health/readiness - if **any local rank** fails or is not ready, the admin endpoint reports unhealthy / not ready - when received the `SIGTERM`, admin process will transfer the signal to all children ranks so that everything exits elegantly. ## Example ```bash vllm serve $MODEL \ --data-parallel-size 8 \ --da...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: are Dp/Ep scheduling in llm-d as experimental, because our launch mechanism does not interact well with K8s service health checking, etc We should instead have a single server launch command in vllm that intersects well...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ank** - each child rank still exposes its own endpoint/port, so external routers can target ranks directly - the supervisor exposes an **admin endpoint** for aggregated health/readiness - if **any local rank** fails or...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: the nice part of external DP mode: - one endpoint per rank - rank-aware routing remains possible But it also makes the deployment much more Kubernetes-friendly: - one top-level `vllm serve` - first-class supervision of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nks so that everything exits elegantly. ## Example ```bash vllm serve $MODEL \ --data-parallel-size 8 \ --data-parallel-size-local 8 \ --data-parallel-start-rank 0 \ --data-parallel-local-external-lb \ --port 8000 \ --d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: with a single `vllm serve` and aggregated admin health endpoint feature request ### 🚀 The feature, motivation and pitch as described in [llm-d/guides/wide-ep-lws/experimental-dp-aware at main · llm-d/llm-d](https://gith...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
