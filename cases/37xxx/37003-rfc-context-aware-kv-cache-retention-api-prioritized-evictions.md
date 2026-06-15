# vllm-project/vllm#37003: [RFC]: Context-Aware KV-Cache Retention API (Prioritized Evictions)

| 字段 | 值 |
| --- | --- |
| Issue | [#37003](https://github.com/vllm-project/vllm/issues/37003) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Context-Aware KV-Cache Retention API (Prioritized Evictions)

### Issue 正文摘录

### Motivation. _[tracker doc: [Context-Aware KV-Cache Retention API](https://docs.google.com/document/d/1kRKAZBG7te38tqv9Twxyyc-Pdkk2JZPm7gqHHnNhFpE/edit?usp=sharing) (llm-d)]_ Agentic workloads break prefix caching under concurrent load. Over 90% of tokens in a typical agent turn are prefixes reused verbatim from the previous turn. With prefix caching, this is a hit. But 40–60% of session wall time is spent paused on tool calls, and during those pauses the agent's blocks are unreferenced. Under concurrent load, other agents evict them via LRU. When the session resumes: cache miss, full recomputation of the entire context — which grows to 70K–200K tokens by session end. Hard pinning doesn't scale. What's needed is a way for the orchestrator to express *which blocks matter more* when eviction is unavoidable. The orchestrator knows this structure — which sessions are live, which tokens are shared prefixes, which are unique tails. LRU sees only recency. **Evidence that LRU is insufficient:** - **Production traces confirm skewed reuse.** Alibaba's study of production LLM traffic found 10% of KV blocks account for 77% of reuses. Workload-aware eviction achieved up to 41.9% lower mean...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ependently. **Status.** We have a working implementation, with standard test coverage. Early benchmarking on a multi-turn ReAct workload shows measurable TTFT and session latency improvements under memory pressure. Thor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: are unique tails. LRU sees only recency. **Evidence that LRU is insufficient:** - **Production traces confirm skewed reuse.** Alibaba's study of production LLM traffic found 10% of KV blocks account for 77% of reuses. W...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t-pinning) are consumers of the API, not the API itself. **Scoped ownership.** An optional `retention_scope` (opaque string, typically session ID) allows multi-tenant scenarios. Any scope can escalate a block's priority...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: time is spent paused on tool calls, and during those pauses the agent's blocks are unreferenced. Under concurrent load, other agents evict them via LRU. When the session resumes: cache miss, full recomputation of the en...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: **token-range retention directive** that lets the orchestrator annotate requests with per-range eviction priorities: ``` RetentionDirective: start: int # token index (inclusive) end: int | null # token index (exclusive)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
