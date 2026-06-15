# vllm-project/vllm#37548: [Bug][ROCm]: Aiter unified attention fails during compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#37548](https://github.com/vllm-project/vllm/issues/37548) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm]: Aiter unified attention fails during compilation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the following serving command ```bash VLLM_ROCM_USE_AITER=1 \ vllm serve RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8 \ --trust-remote-code \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --no-enable-prefix-caching \ --port 9095 \ --kv-cache-dtype fp8 \ --attention-config '{"backend": "ROCM_AITER_UNIFIED_ATTN"}' \ > logs/server.log 2>&1 ``` vllm fails due to failures while processing an MLIR pass pipeline. The full log is shown below Additionally, all `test_attention_quant_pattern` are failing failing for `AttentionBackendEnum.ROCM_AITER_UNIFIED_ATTN` ```log =========================== short test summary info ============================ FAILED tests/compile/passes/test_fusion_attn.py::test_attention_quant_pattern[AttentionBackendEnum.ROCM_AITER_UNIFIED_ATTN-amd/Llama-3.1-8B-Instruct-FP8-KV-TestAttentionFp8StaticQuantPatternModel-+quant_fp8-dtype0-8-128-32-8] FAILED tests/compile/passes/test_fusion_attn.py::test_attention_quant_pattern[AttentionBackendEnum.ROCM_AITER_UNIFIED_ATTN-amd/Llama-3.1-8B-Instruct-FP8-KV-TestAttentionFp8StaticQuantPatternModel-+quant_fp8-dtype0-8-128-40-8] FAILED tests/compile/passes/t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ====== short test summary info ============================ FAILED tests/compile/passes/test_fusion_attn.py::test_attention_quant_pattern[AttentionBackendEnum.ROCM_AITER_UNIFIED_ATTN-amd/Llama-3.1-8B-Instruct-FP8-KV-Tes...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][ROCm]: Aiter unified attention fails during compilation bug;rocm ### Your current environment ### 🐛 Describe the bug When running the following serving command ```bash VLLM_ROCM_USE_AITER=1 \ vllm serve RedHatAI/M...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: h VLLM_ROCM_USE_AITER=1 \ vllm serve RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8 \ --trust-remote-code \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --no-enable-prefix-caching \ --port 9095 \ --kv-cache-dtype...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug][ROCm]: Aiter unified attention fails during compilation bug;rocm ### Your current environment ### 🐛 Describe the bug When running the following serving command ```bash VLLM_ROCM_USE_AITER=1 \ vllm serve RedHatAI/M...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: serving command ```bash VLLM_ROCM_USE_AITER=1 \ vllm serve RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8 \ --trust-remote-code \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --no-enable-prefix-caching \ --port 90...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
