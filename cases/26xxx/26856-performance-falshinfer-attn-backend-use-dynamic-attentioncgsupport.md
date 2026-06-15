# vllm-project/vllm#26856: [Performance]: FalshInfer attn backend. Use dynamic AttentionCGSupport

| 字段 | 值 |
| --- | --- |
| Issue | [#26856](https://github.com/vllm-project/vllm/issues/26856) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: FalshInfer attn backend. Use dynamic AttentionCGSupport

### Issue 正文摘录

### Proposal to improve performance Right now FlashInfer attn backend uses `AttentionCGSupport.UNIFORM_SINGLE_TOKEN_DECODE` that doesn't allow to use FULL cudagraph in case if speculative decoding. In fact FlashInfer contains several attn those chose dynamically. TRT_LLM Gen backend (one of the fastest) supports speculative decoding (`AttentionCGSupport.UNIFORM_BATCH`) and it does make sense to enable cudagraph for decode phase.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Performance]: FalshInfer attn backend. Use dynamic AttentionCGSupport performance ### Proposal to improve performance Right now FlashInfer attn backend uses `AttentionCGSupport.UNIFORM_SINGLE_TOKEN_DECODE` that doesn't...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ow FlashInfer attn backend uses `AttentionCGSupport.UNIFORM_SINGLE_TOKEN_DECODE` that doesn't allow to use FULL cudagraph in case if speculative decoding. In fact FlashInfer contains several attn those chose dynamically...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ionCGSupport.UNIFORM_SINGLE_TOKEN_DECODE` that doesn't allow to use FULL cudagraph in case if speculative decoding. In fact FlashInfer contains several attn those chose dynamically. TRT_LLM Gen backend (one of the faste...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: several attn those chose dynamically. TRT_LLM Gen backend (one of the fastest) supports speculative decoding (`AttentionCGSupport.UNIFORM_BATCH`) and it does make sense to enable cudagraph for decode phase.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
