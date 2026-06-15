# vllm-project/vllm#26516: [Refactor][MLA]: Lift prefill/decode split into compiled region

| 字段 | 值 |
| --- | --- |
| Issue | [#26516](https://github.com/vllm-project/vllm/issues/26516) |
| 状态 | open |
| 标签 | feature request;torch.compile;keep-open |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Refactor][MLA]: Lift prefill/decode split into compiled region

### Issue 正文摘录

This issue is to track part 5 of #24620 follow ups. We want the prefill/decode split outside the unified custom op so surrounding GEMMs/pointwise become visible to torch.compile, improving fusion and reducing Python overhead. This must still play nicely with piecewise CUDAGraphs. That should be the case automatically, as Inductor automatically partitions on data-dependent ops. We might need to do a bit of extra work to preserve piecewise cudagraph behavior with Dynamo splitting, but it should be possible. This will likely require moving code from the MLA Attention backend implementation to the new MLAAttention layer class. cc @ProExpertProg @LucasWilkinson @MatthewBonanni > For 5, the computation we would extract out of `unified_attention` would look something like this in the `fx.Graph` (super simplified): > > ``` > # new (data-dependent) dynamic size > n_prefill: u89 = torch.ops.vllm.split_batch(...) > > # prefill path > qkv_prefill = qkv[..., :n_prefill] > qkv_prefill_2 = torch.bmm(qkv_prefill, ...) > o_prefill = mla_attention_prefill(qkv_prefill_2, ...) > > # decode path > qkv_decode = qkv[..., n_prefill:] > o_decode = mla_attention_decode(qkv_decode, ...) > o_decode_2 = torch...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Refactor][MLA]: Lift prefill/decode split into compiled region feature request;torch.compile;keep-open This issue is to track part 5 of #24620 follow ups. We want the prefill/decode split outside the unified custom op...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Refactor][MLA]: Lift prefill/decode split into compiled region feature request;torch.compile;keep-open This issue is to track part 5 of #24620 follow ups. We want the prefill/decode split outside the unified custom op...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: nt the prefill/decode split outside the unified custom op so surrounding GEMMs/pointwise become visible to torch.compile, improving fusion and reducing Python overhead. This must still play nicely with piecewise CUDAGra...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e possible. This will likely require moving code from the MLA Attention backend implementation to the new MLAAttention layer class. cc @ProExpertProg @LucasWilkinson @MatthewBonanni > For 5, the computation we would ext...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: this exposed to `torch.compile` is these regions might get complex, have quantization, etc. and we still want to do fusions/optimizations on them and benefit from torch.compile.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
