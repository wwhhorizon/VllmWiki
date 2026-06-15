# vllm-project/vllm#21950: [Bug]: Verify that the `min_tokens` sampling parameter is working and covered by CI tests

| 字段 | 值 |
| --- | --- |
| Issue | [#21950](https://github.com/vllm-project/vllm/issues/21950) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Verify that the `min_tokens` sampling parameter is working and covered by CI tests

### Issue 正文摘录

It has been reported that this is not working in the latest V1 code. I'm fairly sure we have this in our CI but perhaps it was only for V0. It may be related to the recent refactoring to move the implementation to a LogitsProcessor. Ref: https://github.com/vllm-project/vllm/issues/21672#issuecomment-3127534960 cc @afeldman-nm

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: erify that the `min_tokens` sampling parameter is working and covered by CI tests bug;good first issue It has been reported that this is not working in the latest V1 code. I'm fairly sure we have this in our CI but perh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: fy that the `min_tokens` sampling parameter is working and covered by CI tests bug;good first issue It has been reported that this is not working in the latest V1 code. I'm fairly sure we have this in our CI but perhaps...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
