# vllm-project/vllm#42: Modify the current PyTorch model to C++

| 字段 | 值 |
| --- | --- |
| Issue | [#42](https://github.com/vllm-project/vllm/issues/42) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Modify the current PyTorch model to C++

### Issue 正文摘录

Expected gain: For 13B models, we should see a 20%-30% latency gain on a single GPU and 2-3x on 4 GPUs. For smaller models, the gain should be even higher. Having a single iteration's computation being completely C++ should be enough for high performance. In this way, we can keep most complicated scheduling logics in Python, including weight loading. Potential sources of overheads: 1. Python v.s. C++. 2. PyTorch (even in C++) v.s. FasterTransformer. How to implement a C++ version: 1. (Fake C++) Torch compiler (torch.jit). 2. Libtorch, C++ version of PyTorch (easier to implement and extend, but can only solve overhead 1). 3. Prune out the useful single model code from FasterTransformer to CacheFlow. This solves both overheads but is harder to implement.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 2. PyTorch (even in C++) v.s. FasterTransformer. How to implement a C++ version: 1. (Fake C++) Torch compiler (torch.jit). 2. Libtorch, C++ version of PyTorch (easier to implement and extend, but can only solve overhead...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: hould see a 20%-30% latency gain on a single GPU and 2-3x on 4 GPUs. For smaller models, the gain should be even higher. Having a single iteration's computation being completely C++ should be enough for high performance...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Modify the current PyTorch model to C++ performance Expected gain: For 13B models, we should see a 20%-30% latency gain on a single GPU and 2-3x on 4 GPUs. For smaller models, the gain should be even higher. Having a si...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: o C++ performance Expected gain: For 13B models, we should see a 20%-30% latency gain on a single GPU and 2-3x on 4 GPUs. For smaller models, the gain should be even higher. Having a single iteration's computation being...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
