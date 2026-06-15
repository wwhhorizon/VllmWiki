# vllm-project/vllm#16039: Integrate PPLX-kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#16039](https://github.com/vllm-project/vllm/issues/16039) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Integrate PPLX-kernels

### Issue 正文摘录

Integrate [pplx-kernels](https://github.com/ppl-ai/pplx-kernels) and integrate them into our DP+EP implementation TODOs: - [ ] Refactor MoE kernels (https://github.com/vllm-project/vllm/pull/15956 and https://github.com/vllm-project/vllm/pull/15914)

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ntegrate them into our DP+EP implementation TODOs: - [ ] Refactor MoE kernels (https://github.com/vllm-project/vllm/pull/15956 and https://github.com/vllm-project/vllm/pull/15914)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
