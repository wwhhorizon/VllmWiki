# vllm-project/vllm#43807: [RFC]: Deprecate `kv_both` for NIXLConnector and Enforce Explicit P/D Roles

| 字段 | 值 |
| --- | --- |
| Issue | [#43807](https://github.com/vllm-project/vllm/issues/43807) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Deprecate `kv_both` for NIXLConnector and Enforce Explicit P/D Roles

### Issue 正文摘录

### Motivation. Today, NIXL P/D instances are all configured with kv_role: "kv_both". The actual prefill-vs-decode behavior is determined by incoming request at runtime, via kv_transfer_params (do_remote_prefill / do_remote_decode). This means there is no reliable way for an instance to know whether it is a P or D before the handshake. In practice, to the best of my knowledge, kv_both does not provide real value: Instances are never re-purposed at runtime. P and D are already started with distinct configurations: low-latency/high-throughput, different tensor-parallel degrees, or even different GPU types. The proxy maintains separate P and D endpoint lists. I have observed no real-world scenario where a running P instance gets repurposed as D or vice versa. If such a need exist please comment on this RFC! :) Role ambiguity blocks config-time optimizations. Any optimization that depends on knowing producer vs consumer semantics -- memory allocation strategies, model loading decisions, scheduler behavior -- must either be deferred to request time (adding per-request overhead) or resort to brittle heuristics like `num_computed_tokens == 0` to infer role. Other connectors already enfor...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: IXL P/D instances are all configured with kv_role: "kv_both". The actual prefill-vs-decode behavior is determined by incoming request at runtime, via kv_transfer_params (do_remote_prefill / do_remote_decode). This means...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: t runtime. P and D are already started with distinct configurations: low-latency/high-throughput, different tensor-parallel degrees, or even different GPU types. The proxy maintains separate P and D endpoint lists. I ha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: using a clear "is_producer" interface. This eliminates the block-count mismatch that currently requires a scheduler-level workaround (#22317) and avoids regressions for other spec-decode methods (#43733) . Future optimi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: xplicit P/D Roles RFC ### Motivation. Today, NIXL P/D instances are all configured with kv_role: "kv_both". The actual prefill-vs-decode behavior is determined by incoming request at runtime, via kv_transfer_params (do_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: g using a clear "is_producer" interface. This eliminates the block-count mismatch that currently requires a scheduler-level workaround (#22317) and avoids regressions for other spec-decode methods (#43733) . Future opti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
