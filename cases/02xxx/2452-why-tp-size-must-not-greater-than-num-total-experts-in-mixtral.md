# vllm-project/vllm#2452: why tp_size must not greater than num_total_experts in mixtral

| 字段 | 值 |
| --- | --- |
| Issue | [#2452](https://github.com/vllm-project/vllm/issues/2452) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> why tp_size must not greater than num_total_experts in mixtral

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/38581531/a5742255-bcfe-4384-bbd9-01ecb48287fe)

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: why tp_size must not greater than num_total_experts in mixtral ![image](https://github.com/vllm-project/vllm/assets/38581531/a5742255-bcfe-4384-bbd9-01ecb48287fe)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
