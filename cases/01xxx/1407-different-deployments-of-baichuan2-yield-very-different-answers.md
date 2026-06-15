# vllm-project/vllm#1407: Different deployments of Baichuan2 yield very different answers

| 字段 | 值 |
| --- | --- |
| Issue | [#1407](https://github.com/vllm-project/vllm/issues/1407) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Different deployments of Baichuan2 yield very different answers

### Issue 正文摘录

Using vllm mode to deploy Baichuan2, providing test interface, using postman test, and using page mode to deploy Baichuan2, two ways to ask the same question, why the use of postman interface mode to get the answer will be wrong, and after the error to ask other questions will also be wrong? ![image](https://github.com/vllm-project/vllm/assets/139730426/a5367a4e-bf6b-4dbf-8c9f-c2f5699dbf50) ![image](https://github.com/vllm-project/vllm/assets/139730426/69acc051-2785-4c4b-8b41-a6fbca4eedaa)

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ld very different answers Using vllm mode to deploy Baichuan2, providing test interface, using postman test, and using page mode to deploy Baichuan2, two ways to ask the same question, why the use of postman interface m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
