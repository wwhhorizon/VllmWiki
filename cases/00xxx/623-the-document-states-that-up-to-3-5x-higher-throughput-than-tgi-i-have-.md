# vllm-project/vllm#623: The document states that up to 3.5x higher throughput than TGI，I have my doubts

| 字段 | 值 |
| --- | --- |
| Issue | [#623](https://github.com/vllm-project/vllm/issues/623) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The document states that up to 3.5x higher throughput than TGI，I have my doubts

### Issue 正文摘录

What is the TGI version you are comparing? This is not consistent with the benchmark results of some friends，I'm a bit confused. https://zhuanlan.zhihu.com/p/645732302 ![image](https://github.com/vllm-project/vllm/assets/57557769/9e9ce2bb-3179-463d-94b5-6447c5c84f79)

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: The document states that up to 3.5x higher throughput than TGI，I have my doubts What is the TGI version you are comparing? This is not consistent with the benchmark results of some friends，I'm a bit confused. https://zh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t up to 3.5x higher throughput than TGI，I have my doubts What is the TGI version you are comparing? This is not consistent with the benchmark results of some friends，I'm a bit confused. https://zhuanlan.zhihu.com/p/6457...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
