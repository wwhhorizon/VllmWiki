# vllm-project/vllm#35771: [RFC][torch.compile]: Disable Sequence Parallelism (SP) for piecewise compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#35771](https://github.com/vllm-project/vllm/issues/35771) |
| 状态 | closed |
| 标签 | RFC;torch.compile |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC][torch.compile]: Disable Sequence Parallelism (SP) for piecewise compilation

### Issue 正文摘录

### Motivation. When compiling piecewise (dynamo partition and non-empty `splitting_ops`), the RMSNorm residual tensor gets passed between piecewise subgraphs. This poses a challenge for sequence parallelism as it splits along the num_tokens dimension, which means the residual gets split across TP ranks. That means the size of the residual is different before and after the SP pass. The initial implementation of SP had to work on piecewise compiled graphs as it was done before we had full cudagraph support and way before Inductor partition. It requires static sizes because otherwise residual splitting didn't work (@cascade812 who implemented this might remember more). It still (unsafely) changes the size of the residual passed between subgraphs, but if the pass succeeds on all subgraphs, the end result happens to be correct. We have since added support for SP with fullgraph compilation (Inductor partition or `splitting_ops=[]`), which is the default approach as it allows SP to run on dynamic shape `num_tokens` graphs. We also want to enable SP for large `num_tokens` which is unlikely to be compiled with static sizes anyway. But the piecewise support is still there. And we added uns...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC][torch.compile]: Disable Sequence Parallelism (SP) for piecewise compilation RFC;torch.compile ### Motivation. When compiling piecewise (dynamo partition and non-empty `splitting_ops`), the RMSNorm residual tensor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: or not. However, this is incompatible with `--enable-prompt-embeds` and multimodal models, as a graph input becomes the residual in this case so it has to be sliced properly (fix in #33322). I believe the fix breaks the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC][torch.compile]: Disable Sequence Parallelism (SP) for piecewise compilation RFC;torch.compile ### Motivation. When compiling piecewise (dynamo partition and non-empty `splitting_ops`), the RMSNorm residual tensor...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: should initially resolve this by passing the whole residual and slicing/all-gathering at the start/end of a PP region after the pass. In the future, we can instead all-gather/slice before the SP transformation and then...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
