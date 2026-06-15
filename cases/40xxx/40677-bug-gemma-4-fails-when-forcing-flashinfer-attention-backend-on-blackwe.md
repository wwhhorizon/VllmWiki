# vllm-project/vllm#40677: [Bug]: Gemma-4 fails when forcing FLASHINFER attention backend on Blackwell SM120 (head_size not supported)

| 字段 | 值 |
| --- | --- |
| Issue | [#40677](https://github.com/vllm-project/vllm/issues/40677) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma-4 fails when forcing FLASHINFER attention backend on Blackwell SM120 (head_size not supported)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On a RTX PRO 6000 GPU, forcing the `FLASHINFER` attention backend for Gemma-4 causes vLLM to fail during engine initialization with: ```text ValueError: Selected backend AttentionBackendEnum.FLASHINFER is not valid for this configuration. Reason: ['head_size not supported'] ``` Without the override, the same model loads and runs correctly with `TRITON_ATTN`. This reproduces for: - the base model: `google/gemma-4-31b-it` - quantized FP8 checkpoint - quantized NVFP4 checkpoint Gemma-4 config on this model reports: - `head_dim=256` - `global_head_dim=512` ### Minimal repro ```python from vllm import LLM LLM( model="google/gemma-4-31b-it", tokenizer="google/gemma-4-31b-it", dtype="bfloat16", tensor_parallel_size=1, max_model_len=2048, gpu_memory_utilization=0.9, enforce_eager=True, disable_log_stats=True, attention_config={"backend": "FLASHINFER"}, ) ``` Observed failure: ```text Using AttentionBackendEnum.FLASHINFER backend. ValueError: Selected backend AttentionBackendEnum.FLASHINFER is not valid for this configuration. Reason: ['head_size not supported'] ``` ### What I expected Either: 1. `FLASHINFER` should work for Gemma-4 on th...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: ATTN`. This reproduces for: - the base model: `google/gemma-4-31b-it` - quantized FP8 checkpoint - quantized NVFP4 checkpoint Gemma-4 config on this model reports: - `head_dim=256` - `global_head_dim=512` ### Minimal re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Gemma-4 fails when forcing FLASHINFER attention backend on Blackwell SM120 (head_size not supported) bug ### Your current environment ### 🐛 Describe the bug On a RTX PRO 6000 GPU, forcing the `FLASHINFER` attenti...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Gemma-4 fails when forcing FLASHINFER attention backend on Blackwell SM120 (head_size not supported) bug ### Your current environment ### 🐛 Describe the bug On a RTX PRO 6000 GPU, forcing the `FLASHINFER` attenti...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Gemma-4 fails when forcing FLASHINFER attention backend on Blackwell SM120 (head_size not supported) bug ### Your current environment ### 🐛 Describe the bug On a RTX PRO 6000 GPU, forcing the `FLASHINFER` attenti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma-4 fails when forcing FLASHINFER attention backend on Blackwell SM120 (head_size not supported) bug ### Your current environment ### 🐛 Describe the bug On a RTX PRO 6000 GPU, forcing the `FLASHINFER` attenti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
