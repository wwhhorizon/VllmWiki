# vllm-project/vllm#28131: [Bug]: Batch Invariant Failed when enable cudagraph on L40s (Ada) GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#28131](https://github.com/vllm-project/vllm/issues/28131) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Batch Invariant Failed when enable cudagraph on L40s (Ada) GPU

### Issue 正文摘录

### 🐛 Describe the bug I was running experiments on an L40s GPU with `VLLM_BATCH_INVARIANT` set to 1. When I enable `eager=True`, the results are batch-invariant. However, when I enable cudagraphs, the outputs diverge. I noticed that the documentation mentions batch invariance is only supported on Hopper and Blackwell series GPUs. I’m wondering why eager mode works fine, but enabling cudagraphs causes divergence on L40s.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Batch Invariant Failed when enable cudagraph on L40s (Ada) GPU bug;stale ### 🐛 Describe the bug I was running experiments on an L40s GPU with `VLLM_BATCH_INVARIANT` set to 1. When I enable `eager=True`, the resul...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: agraphs, the outputs diverge. I noticed that the documentation mentions batch invariance is only supported on Hopper and Blackwell series GPUs. I’m wondering why eager mode works fine, but enabling cudagraphs causes div...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Bug]: Batch Invariant Failed when enable cudagraph on L40s (Ada) GPU bug;stale ### 🐛 Describe the bug I was running experiments on an L40s GPU with `VLLM_BATCH_INVARIANT` set to 1. When I enable `eager=True`, the result...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
