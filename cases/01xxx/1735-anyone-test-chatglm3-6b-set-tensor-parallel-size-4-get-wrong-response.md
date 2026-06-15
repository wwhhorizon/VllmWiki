# vllm-project/vllm#1735: anyone test chatglm3-6b? set tensor_parallel_size=4, get wrong response

| 字段 | 值 |
| --- | --- |
| Issue | [#1735](https://github.com/vllm-project/vllm/issues/1735) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> anyone test chatglm3-6b? set tensor_parallel_size=4, get wrong response

### Issue 正文摘录

Set tensor_parallel_size=1 or tensor_parallel_size=2. the response is OK. my env info: vllm==0.2.2 ray==2.8.0 transformers==4.34.0 torch==2.1.0

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: anyone test chatglm3-6b? set tensor_parallel_size=4, get wrong response Set tensor_parallel_size=1 or tensor_parallel_size=2. the response is OK. my env info: vllm==0.2.2 ray==2.8.0 transformers==4.34.0 torch==2.1.0

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
