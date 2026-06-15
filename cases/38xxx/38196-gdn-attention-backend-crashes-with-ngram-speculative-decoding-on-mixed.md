# vllm-project/vllm#38196: GDN attention backend crashes with ngram speculative decoding on mixed decode batches

| 字段 | 值 |
| --- | --- |
| Issue | [#38196](https://github.com/vllm-project/vllm/issues/38196) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;fp8;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> GDN attention backend crashes with ngram speculative decoding on mixed decode batches

### Issue 正文摘录

## Description The GDN (Gated Delta Network) attention backend in `vllm/v1/attention/backends/gdn_attn.py` crashes with an `AssertionError` when ngram speculative decoding produces a batch containing both regular decode tokens and speculative decode tokens. ## Environment - vLLM version: `0.17.2.dev0+g95c0f928c.d20260313` (nightly) - GPU: NVIDIA GH200 480GB - Model: Qwen3.5 9B (uses GDN linear attention) - Config: FP8 online quantization, ngram speculative decoding (128 tokens, prompt lookup) ## Error ``` File ".../vllm/v1/attention/backends/gdn_attn.py", line 310, in build assert not (num_decodes > 0 and num_spec_decodes > 0), ( AssertionError: num_decodes: 1, num_spec_decodes: 1 ``` ## Root Cause Line 310 in `gdn_attn.py`: ```python # Function code counted on either presency non-spec decode or spec decode, # but not both. assert not (num_decodes > 0 and num_spec_decodes > 0), ( f"num_decodes: {num_decodes}, num_spec_decodes: {num_spec_decodes}" ) ``` When ngram speculative decoding rejects some tokens, vLLM creates a batch with both: - Regular decode tokens (from rejected/verified sequences) - Speculative decode tokens (new speculative proposals) The GDN attention builder assume...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: lar decode tokens and speculative decode tokens. ## Environment - vLLM version: `0.17.2.dev0+g95c0f928c.d20260313` (nightly) - GPU: NVIDIA GH200 480GB - Model: Qwen3.5 9B (uses GDN linear attention) - Config: FP8 online...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: GDN attention backend crashes with ngram speculative decoding on mixed decode batches ## Description The GDN (Gated Delta Network) attention backend in `vllm/v1/attention/backends/gdn_attn.py` crashes with an `Assertion...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: IA GH200 480GB - Model: Qwen3.5 9B (uses GDN linear attention) - Config: FP8 online quantization, ngram speculative decoding (128 tokens, prompt lookup) ## Error ``` File ".../vllm/v1/attention/backends/gdn_attn.py", li...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: `0.17.2.dev0+g95c0f928c.d20260313` (nightly) - GPU: NVIDIA GH200 480GB - Model: Qwen3.5 9B (uses GDN linear attention) - Config: FP8 online quantization, ngram speculative decoding (128 tokens, prompt lookup) ## Error `...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: GDN attention backend crashes with ngram speculative decoding on mixed decode batches ## Description The GDN (Gated Delta Network) attention backend in `vllm/v1/attention/backends/gdn_attn.py` crashes with an `Assertion...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
