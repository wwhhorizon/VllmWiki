# vllm-project/vllm#38756: [vLLM IR] Port RoPE ops to IR

| 字段 | 值 |
| --- | --- |
| Issue | [#38756](https://github.com/vllm-project/vllm/issues/38756) |
| 状态 | open |
| 标签 | vllm-ir |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [vLLM IR] Port RoPE ops to IR

### Issue 正文摘录

There are many flavors of rope, but some of them only contain a native implementation; those do not need to be ported. Additionally, the sin_cos_cache initialization logic should remain in the layer. At the very least, the following should be ported: - `RotaryEmbedding` - `DeepseekScalingRotaryEmbedding` However, we should carefully inspect semantics if any of the ops can be consolidated, especially using simple bool params. This will help us reduce the maintenance burden and increase the coverage for rope+cache related fusions. Final challenge for rope will be the inplace semantics, as the _C implementation is fully inplace, and the arguments are views, which will complicate the aliasing analysis for the clone elimination after the lowering pass (see #36823)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d carefully inspect semantics if any of the ops can be consolidated, especially using simple bool params. This will help us reduce the maintenance burden and increase the coverage for rope+cache related fusions. Final c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
