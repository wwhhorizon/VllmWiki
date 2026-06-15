# vllm-project/vllm#490: Baichuan model can not be run

| 字段 | 值 |
| --- | --- |
| Issue | [#490](https://github.com/vllm-project/vllm/issues/490) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Baichuan model can not be run

### Issue 正文摘录

Hello, the PR one merged into main are actually can not run..... The output can not be given just thrown some value error which I don't know where caused it. However, I have tested another Baichuan PR, it works as expected. Please fix it, otherwise would cause many users confused.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Baichuan model can not be run bug Hello, the PR one merged into main are actually can not run..... The output can not be given just thrown some value error which I don't know where caused it. However, I have tested anot...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: wn some value error which I don't know where caused it. However, I have tested another Baichuan PR, it works as expected. Please fix it, otherwise would cause many users confused.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
