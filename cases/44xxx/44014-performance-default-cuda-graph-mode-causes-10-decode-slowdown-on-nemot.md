# vllm-project/vllm#44014: [Performance]: Default CUDA graph mode causes 10× decode slowdown on Nemotron-3-Nano-30B (TP=2, hybrid Mamba+MoE)

| 字段 | 值 |
| --- | --- |
| Issue | [#44014](https://github.com/vllm-project/vllm/issues/44014) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;moe |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;moe |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Default CUDA graph mode causes 10× decode slowdown on Nemotron-3-Nano-30B (TP=2, hybrid Mamba+MoE)

### Issue 正文摘录

_本地原始数据中没有 issue 正文。_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Performance]: Default CUDA graph mode causes 10× decode slowdown on Nemotron-3-Nano-30B (TP=2, hybrid Mamba+MoE) performance performance distributed_parallel;moe cuda;moe slowdown
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: de causes 10× decode slowdown on Nemotron-3-Nano-30B (TP=2, hybrid Mamba+MoE) performance performance distributed_parallel;moe cuda;moe slowdown
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Default CUDA graph mode causes 10× decode slowdown on Nemotron-3-Nano-30B (TP=2, hybrid Mamba+MoE) performance performance distributed_parallel;moe cuda;moe slowdown

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
