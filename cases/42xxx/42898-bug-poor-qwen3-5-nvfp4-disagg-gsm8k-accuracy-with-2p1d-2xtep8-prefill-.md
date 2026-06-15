# vllm-project/vllm#42898: [Bug]: Poor Qwen3.5 NVFP4 disagg GSM8K accuracy with 2p1d (2xTEP8 prefill, 1xDEP8 decode)

| 字段 | 值 |
| --- | --- |
| Issue | [#42898](https://github.com/vllm-project/vllm/issues/42898) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Poor Qwen3.5 NVFP4 disagg GSM8K accuracy with 2p1d (2xTEP8 prefill, 1xDEP8 decode)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary Qwen3.5 NVFP4 disaggregated serving with NIXL becomes accuracy-unstable across repeated identical GSM8K runs in the same server process. Topology: ```text prefill: 2xTEP8 decode: 1xDEP8 KV cache dtype: bfloat16 prefix caching: disabled async scheduling: disabled HMA: enabled SSM conv state layout: DS ``` The first 32-question GSM8K run is healthy, but the second identical run in the same job degrades sharply. Logs show successful NIXL transfers and no `NIXL transfer failure`, `compatibility hash mismatch`, `Traceback`, or `ERROR`. ## Environment ```text Hardware: GB200, 4 GPUs/node Model: Qwen3.5-397B-A17B-NVFP4 vLLM commit: 24337fb860a89f2087df27b02b7c9620a7fd0093 vLLM version: 0.20.2rc1.dev354+g24337fb86.precompiled Dynamo: 1.2.0.dev20260429 NIXL: nixl-cu13==1.0.1, nixl==1.0.1 ``` ## Repro Run disagg server with: ```text prefill: 2 workers, each TP8 + expert parallel decode: 1 logical worker, DP8 + expert parallel VLLM_SSM_CONV_STATE_LAYOUT=DS --kv-cache-dtype bfloat16 --no-enable-prefix-caching --no-async-scheduling --no-disable-hybrid-kv-cache-manager --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Poor Qwen3.5 NVFP4 disagg GSM8K accuracy with 2p1d (2xTEP8 prefill, 1xDEP8 decode) bug ### Your current environment ### 🐛 Describe the bug ## Summary Qwen3.5 NVFP4 disaggregated serving with NIXL becomes accuracy...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 7B-A17B-NVFP4 vLLM commit: 24337fb860a89f2087df27b02b7c9620a7fd0093 vLLM version: 0.20.2rc1.dev354+g24337fb86.precompiled Dynamo: 1.2.0.dev20260429 NIXL: nixl-cu13==1.0.1, nixl==1.0.1 ``` ## Repro Run disagg server with...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: [Bug]: Poor Qwen3.5 NVFP4 disagg GSM8K accuracy with 2p1d (2xTEP8 prefill, 1xDEP8 decode) bug ### Your current environment ### 🐛 Describe the bug ## Summary Qwen3.5 NVFP4 disaggregated serving with NIXL becomes accuracy...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Poor Qwen3.5 NVFP4 disagg GSM8K accuracy with 2p1d (2xTEP8 prefill, 1xDEP8 decode) bug ### Your current environment ### 🐛 Describe the bug ## Summary Qwen3.5 NVFP4 disaggregated serving with NIXL becomes accuracy...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: same server process. Topology: ```text prefill: 2xTEP8 decode: 1xDEP8 KV cache dtype: bfloat16 prefix caching: disabled async scheduling: disabled HMA: enabled SSM conv state layout: DS ``` The first 32-question GSM8K r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
