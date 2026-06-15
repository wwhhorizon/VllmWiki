# vllm-project/vllm#139: Publish wheels with pre-built CUDA binaries

| 字段 | 值 |
| --- | --- |
| Issue | [#139](https://github.com/vllm-project/vllm/issues/139) |
| 状态 | closed |
| 标签 | help wanted;installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Publish wheels with pre-built CUDA binaries

### Issue 正文摘录

Currently, pip installing our package takes 5-10 minutes because our CUDA kernels are compiled on the user machine. For better UX, we should include pre-built CUDA binaries in our PyPI distribution, just like PyTorch and xformers.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Publish wheels with pre-built CUDA binaries help wanted;installation Currently, pip installing our package takes 5-10 minutes because our CUDA kernels are compiled on the user machine. For better UX, we should include p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Publish wheels with pre-built CUDA binaries help wanted;installation Currently, pip installing our package takes 5-10 minutes because our CUDA kernels are compiled on the user machine. For better UX, we should include p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
