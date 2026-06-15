# vllm-project/vllm#20416: [Usage]: whether torchrun-compatible mode supports DP/EP?

| 字段 | 值 |
| --- | --- |
| Issue | [#20416](https://github.com/vllm-project/vllm/issues/20416) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: whether torchrun-compatible mode supports DP/EP?

### Issue 正文摘录

### Your current environment None ### How would you like to use vllm I have read https://github.com/vllm-project/vllm/pull/12071 and it's a wonderful work. I wonder if this torchrun-compatible executor supports EP? Since the comments in https://github.com/vllm-project/vllm/pull/12071 point out that the input should be same across all ranks (maybe the context is TP). In EP scenario, all ranks in the same EP group should have different input to take the advantage of EP MoE. And if DeepEP is enabled, prefill and decode would dispatch to normal kernels and ll kernels separately. This requires schedulers ascross ranks in the same EP group should schedule the same prefill/decode action with different inputs. Are we now ensuring this behavior or this is not necessary in current design? ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: whether torchrun-compatible mode supports DP/EP? usage;stale ### Your current environment None ### How would you like to use vllm I have read https://github.com/vllm-project/vllm/pull/12071 and it's a wonderful...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: advantage of EP MoE. And if DeepEP is enabled, prefill and decode would dispatch to normal kernels and ll kernels separately. This requires schedulers ascross ranks in the same EP group should schedule the same prefill/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: gn? ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: he same EP group should have different input to take the advantage of EP MoE. And if DeepEP is enabled, prefill and decode would dispatch to normal kernels and ll kernels separately. This requires schedulers ascross ran...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
