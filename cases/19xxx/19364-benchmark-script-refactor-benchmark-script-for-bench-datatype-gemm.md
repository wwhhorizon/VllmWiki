# vllm-project/vllm#19364: [Benchmark Script] Refactor benchmark script for `bench_datatype_gemm`

| 字段 | 值 |
| --- | --- |
| Issue | [#19364](https://github.com/vllm-project/vllm/issues/19364) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Benchmark Script] Refactor benchmark script for `bench_datatype_gemm`

### Issue 正文摘录

>I know this is a bnechmark script but I think this could still be refactored. Perhaps a few functions/objects and a dictionary? _Originally posted by @ProExpertProg in https://github.com/vllm-project/vllm/pull/19233#discussion_r2133137967_ I think this is a great idea, example config designed: ```py PROVIDER_CFGS = { "int8-tensor-w-token-a": dict(w="tensor", a="token", no_a_quant=False), "int8-tensor-w-tensor-a": dict(w="tensor", a="tensor", no_a_quant=False), "int8-channel-w-token-a": dict(w="channel", a="token", no_a_quant=False), "int8-channel-w-tensor-a": dict(w="channel", a="tensor", no_a_quant=False), "int8-tensor-w-token-a-noquant": dict(w="tensor", a="token", no_a_quant=True), "int8-tensor-w-tensor-a-noquant": dict(w="tensor", a="tensor", no_a_quant=True), "int8-channel-w-token-a-noquant": dict(w="channel", a="token", no_a_quant=True), "int8-channel-w-tensor-a-noquant": dict(w="channel", a="tensor", no_a_quant=True), } ``` After https://github.com/vllm-project/vllm/pull/19233 merged, I can have another PR optimizing this, and update `benchmarks/kernels/bench_fp8_gemm.py` as well.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: R_CFGS = { "int8-tensor-w-token-a": dict(w="tensor", a="token", no_a_quant=False), "int8-tensor-w-tensor-a": dict(w="tensor", a="tensor", no_a_quant=False), "int8-channel-w-token-a": dict(w="channel", a="token", no_a_qu...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Benchmark Script] Refactor benchmark script for `bench_datatype_gemm` >I know this is a bnechmark script but I think this could still be refactored. Perhaps a few functions/objects and a dictionary? _Originally posted...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: { "int8-tensor-w-token-a": dict(w="tensor", a="token", no_a_quant=False), "int8-tensor-w-tensor-a": dict(w="tensor", a="tensor", no_a_quant=False), "int8-channel-w-token-a": dict(w="channel", a="token", no_a_quant=False...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ull/19233#discussion_r2133137967_ I think this is a great idea, example config designed: ```py PROVIDER_CFGS = { "int8-tensor-w-token-a": dict(w="tensor", a="token", no_a_quant=False), "int8-tensor-w-tensor-a": dict(w="...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Benchmark Script] Refactor benchmark script for `bench_datatype_gemm` >I know this is a bnechmark script but I think this could still be refactored. Perhaps a few functions/objects and a dictionary? _Originally posted b

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
