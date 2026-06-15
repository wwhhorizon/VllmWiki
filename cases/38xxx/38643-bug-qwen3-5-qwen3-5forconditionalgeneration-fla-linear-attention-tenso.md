# vllm-project/vllm#38643: [Bug]: Qwen3.5 (Qwen3_5ForConditionalGeneration) FLA linear attention tensor format mismatch causes gibberish output

| 字段 | 值 |
| --- | --- |
| Issue | [#38643](https://github.com/vllm-project/vllm/issues/38643) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;kernel;operator;quantization |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 (Qwen3_5ForConditionalGeneration) FLA linear attention tensor format mismatch causes gibberish output

### Issue 正文摘录

## Description When running `Qwen3_5ForConditionalGeneration` (Qwen3.5-4B-NVFP4) with vLLM nightly, the model produces completely garbled/gibberish output — a mix of random tokens from multiple languages. ## Root Cause The following warning is emitted during every inference call, indicating a tensor format mismatch in the FLA (Flash Linear Attention) ops layer: ``` vllm/model_executor/layers/fla/ops/utils.py:113: UserWarning: Input tensor shape suggests potential format mismatch: seq_len (12) < num_heads (32). This may indicate the inputs were passed in head-first format [B, H, T, ...] when head_first=False was specified. Please verify your input tensor format matches the expected shape [B, T, H, ...]. ``` Also from `torch/_dynamo/eval_frame.py`: ``` UserWarning: Input tensor shape suggests potential format mismatch: seq_len (12) < num_heads (16). This may indicate the inputs were passed in head-first format [B, H, T, ...] Please verify your input tensor format matches the expected shape [B, T, H, ...]. ``` Qwen3.5 uses a hybrid Transformer + linear attention (Mamba-style) architecture. The `linear_attn.conv1d` layers are present in multiple decoder layers. The FLA ops kernel appe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: passed in head-first format [B, H, T, ...] when head_first=False was specified. Please verify your input tensor format matches the expected shape [B, T, H, ...]. ``` Also from `torch/_dynamo/eval_frame.py`: ``` UserWarn...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: Description When running `Qwen3_5ForConditionalGeneration` (Qwen3.5-4B-NVFP4) with vLLM nightly, the model produces completely garbled/gibberish output — a mix of random tokens from multiple languages. ## Root Cause The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 5 (Qwen3_5ForConditionalGeneration) FLA linear attention tensor format mismatch causes gibberish output ## Description When running `Qwen3_5ForConditionalGeneration` (Qwen3.5-4B-NVFP4) with vLLM nightly, the model produ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3.5 (Qwen3_5ForConditionalGeneration) FLA linear attention tensor format mismatch causes gibberish output ## Description When running `Qwen3_5ForConditionalGeneration` (Qwen3.5-4B-NVFP4) with vLLM nightly, th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: max-model-len", "32768", "--trust-remote-code", "--attention-backend", "flashinfer" ] ``` ```bash curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen3.5-4B-NVFP4",...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
