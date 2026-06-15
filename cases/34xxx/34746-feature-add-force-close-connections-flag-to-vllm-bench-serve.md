# vllm-project/vllm#34746: [Feature]: Add --force-close-connections flag to vllm bench serve

| 字段 | 值 |
| --- | --- |
| Issue | [#34746](https://github.com/vllm-project/vllm/issues/34746) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add --force-close-connections flag to vllm bench serve

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Add a CLI flag --force-close-connections to vllm bench serve that configures the aiohttp TCPConnector with force_close=True, causing TCP connections to be closed after each response instead of being returned to the connection pool for reuse. Currently, force_close=False is hardcoded in vllm/benchmarks/serve.py: connector = aiohttp.TCPConnector( limit=max_concurrency or 0, limit_per_host=max_concurrency or 0, ttl_dns_cache=300, use_dns_cache=True, keepalive_timeout=60, enable_cleanup_closed=True, force_close=False, # <-- no way to change this ssl=ssl_setting, ) The proposed change would add: vllm bench serve --force-close-connections ... Motivation: When benchmarking vLLM behind a load balancer (e.g. round-robin), persistent connections defeat the load balancing strategy. Since all pooled connections are established to the same backend chosen during the first request, subsequent requests continue hitting that same backend rather than being distributed across instances. Being able to close connections between requests allows the load balancer to route each new request independently, which is essential for accurately benchmarking multi-instance...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nts with round-robin or least-connections strategies. Pitch: This is a small, self-contained change — a single CLI argument wired to the existing force_close parameter on the TCPConnector. It has no impact on default be...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: Add --force-close-connections flag to vllm bench serve feature request;stale ### 🚀 The feature, motivation and pitch Add a CLI flag --force-close-connections to vllm bench serve that configures the aiohttp TCP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ction pool for reuse. Currently, force_close=False is hardcoded in vllm/benchmarks/serve.py: connector = aiohttp.TCPConnector( limit=max_concurrency or 0, limit_per_host=max_concurrency or 0, ttl_dns_cache=300, use_dns_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ncing strategy. Since all pooled connections are established to the same backend chosen during the first request, subsequent requests continue hitting that same backend rather than being distributed across instances. Be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: balancer (e.g. round-robin), persistent connections defeat the load balancing strategy. Since all pooled connections are established to the same backend chosen during the first request, subsequent requests continue hitt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
