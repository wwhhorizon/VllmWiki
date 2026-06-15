# vllm-project/vllm#639: VLLM supporting more than 1 completion per prompt - sampling?

| 字段 | 值 |
| --- | --- |
| Issue | [#639](https://github.com/vllm-project/vllm/issues/639) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> VLLM supporting more than 1 completion per prompt - sampling?

### Issue 正文摘录

Hi there, I want to generate more than one completion for one prompt (n > 1) without using beam search and instead using random sampling for these queries. However, there seems to be an issue when setting best_of to a value greater than 1, specifically when n=5 and best_of=1. The server has a condition that best_of must be greater than or equal to n, causing it to error out when doing sampling - `best_of must be 1 when using greedy sampling.` Just want to know if it is currently supported to perform multiple queries (n > 1) using random sampling with VLLM. Thanks for the help! Thanks, Arnav

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: seems to be an issue when setting best_of to a value greater than 1, specifically when n=5 and best_of=1. The server has a condition that best_of must be greater than or equal to n, causing it to error out when doing sa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ate more than one completion for one prompt (n > 1) without using beam search and instead using random sampling for these queries. However, there seems to be an issue when setting best_of to a value greater than 1, spec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
