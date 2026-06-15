# vllm-project/vllm#2415: top_k = 50 will make vllm prediction align with transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#2415](https://github.com/vllm-project/vllm/issues/2415) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> top_k = 50 will make vllm prediction align with transformers

### Issue 正文摘录

There is a lot of issues about the different results between vllm and transformers. Some of them is caused by vllm sample implementation like repetition, or caused by kernel implementation bug. These bugs are fixed in the latest vllm release. When I test the latest version of vllm, I still get different results from transformers. After some investigation, I find that the default value of top_k is different between vllm and transformers. **Transformer's default top_k is 50, vllm's default top_k is -1**. I test vllm with top_k = 50, the result is same with transformers. Hope this will help.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: These bugs are fixed in the latest vllm release. When I test the latest version of vllm, I still get different results from transformers. After some investigation, I find that the default value of top_k is different bet...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: top_k = 50 will make vllm prediction align with transformers feature request There is a lot of issues about the different results between vllm and transformers. Some of them is caused by vllm sample implementation like...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: n, or caused by kernel implementation bug. These bugs are fixed in the latest vllm release. When I test the latest version of vllm, I still get different results from transformers. After some investigation, I find that...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
