# vllm-project/vllm#633: T4 machine got stuck

| 字段 | 值 |
| --- | --- |
| Issue | [#633](https://github.com/vllm-project/vllm/issues/633) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> T4 machine got stuck

### Issue 正文摘录

INFO 08-01 03:08:39 scheduler.py:271] Throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 92.9%, CPU KV cache usage: 0.0% INFO 08-01 03:08:45 scheduler.py:271] Throughput: 181.6 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 100.0%, CPU KV cache usage: 0.0% INFO 08-01 03:08:51 scheduler.py:271] Throughput: 185.4 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 100.0%, CPU KV cache usage: 0.0% INFO 08-01 03:08:56 scheduler.py:271] Throughput: 189.7 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 100.0%, CPU KV cache usage: 0.0% INFO 08-01 03:09:02 scheduler.py:271] Throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 1 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 08-01 03:09:07 scheduler.py:271] Throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 1 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 08-01 03:09:12 scheduler.py:271] Throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 1 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 08-01 03:09:17 sche...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: T4 machine got stuck bug INFO 08-01 03:08:39 scheduler.py:271] Throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 92.9%, CPU KV cache usage: 0.0% INFO 08-01 03:08:45 schedul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: U KV cache usage: 0.0%, CPU KV cache usage: 0.0% **_when i use V100 and A100, everything is ok, but deploy in T4 machine , some cases are ok, some cases got stuck, if one case gets stuck, others can't request._** perfor...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 92.9%, CPU KV cache usage: 0.0% INFO 08-01 03:08:45 scheduler.py:271] Throughput: 181.6 tokens/s, Running: 1 reqs, Swapped: 0 reqs...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: T4 machine got stuck bug INFO 08-01 03:08:39 scheduler.py:271] Throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 92.9%, CPU KV cache usage: 0.0% INFO 08-01 03:08:45 schedul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
