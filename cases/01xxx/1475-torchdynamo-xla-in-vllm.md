# vllm-project/vllm#1475: TorchDynamo & XLA in VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#1475](https://github.com/vllm-project/vllm/issues/1475) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TorchDynamo & XLA in VLLM

### Issue 正文摘录

We came across this post which talks about gains in Llama inference with TorchDynamo and XLA https://pytorch.org/blog/path-achieve-low-inference-latency/?utm_content=254892693&utm_medium=social&utm_source=linkedin&hss_channel=lcp-78618366 I had the following questions :- (a) Has the vllm team or anyone here explored these optimizations with VLLM ? If yes, do you see similar gains as discussed in the blog ? (b) Does the VLLM team plan to support TorchDynamo and XLA ? (c) Do you think any of the optimizations brought in by TorchDynamo can conflict with the optimizations or custom implementation in VLLM itself ?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g/path-achieve-low-inference-latency/?utm_content=254892693&utm_medium=social&utm_source=linkedin&hss_channel=lcp-78618366 I had the following questions :- (a) Has the vllm team or anyone here explored these optimizatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Dynamo & XLA in VLLM We came across this post which talks about gains in Llama inference with TorchDynamo and XLA https://pytorch.org/blog/path-achieve-low-inference-latency/?utm_content=254892693&utm_medium=social&utm_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: TorchDynamo and XLA https://pytorch.org/blog/path-achieve-low-inference-latency/?utm_content=254892693&utm_medium=social&utm_source=linkedin&hss_channel=lcp-78618366 I had the following questions :- (a) Has the vllm tea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
