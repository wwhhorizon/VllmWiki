# vllm-project/vllm#33678: [Bug]: [ROCm] Kimi-K2.5 produces incorrect results on AMD MI308X

| 字段 | 值 |
| --- | --- |
| Issue | [#33678](https://github.com/vllm-project/vllm/issues/33678) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | gemm;quantization |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [ROCm] Kimi-K2.5 produces incorrect results on AMD MI308X

### Issue 正文摘录

### Your current environment ## Environment - **GPU**: AMD Instinct MI308X - **vLLM version**: v0.15.0 - **Model**: moonshotai/Kimi-K2.5 (compressed-tensors INT4 quantization) ### 🐛 Describe the bug ## Issue Running Kimi-K2.5 on AMD MI308X produces completely incorrect outputs. The gsm8k benchmark accuracy is ~0%. ## Reproduction ```bash # Start vLLM server VLLM_USE_V1=1 \ SAFETENSORS_FAST_GPU=1 \ VLLM_ROCM_USE_AITER=0 \ VLLM_ROCM_USE_AITER_MOE=0 \ VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS=0 \ VLLM_USE_TRITON_FLASH_ATTN=0 NCCL_DEBUG=WARN \ VLLM_LOGGING_LEVEL=DEBUG \ VLLM_RPC_TIMEOUT=18000000 \ VLLM_ROCM_USE_AITER_ASMMOE=0 \ VLLM_ROCM_USE_AITER_MLA=0 \ VLLM_ROCM_USE_AITER_MHA=0 \ VLLM_TORCH_PROFILER_DIR=./vllm_profile \ AITER_ENABLE_AOT_GLUON_PA_MQA_LOGITS=0 \ vllm serve /path/xxx \ --tensor-parallel-size 8 --data-parallel-size 1 \ --max-num-seqs 15 --max-num-batched-tokens 32768 \ --mm-encoder-tp-mode data --tool-call-parser kimi_k2 --reasoning-parser kimi_k2 \ --trust-remote-code \ --no-enable-prefix-caching --disable-log-requests \ --gpu-memory-utilization 0.8 --load-format fastsafetensors \ --block-size 64 --async-scheduling \ --compilation-config '{"cudagraph_mode": "FULL_AND_...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: Kimi-K2.5 on AMD MI308X produces completely incorrect outputs. The gsm8k benchmark accuracy is ~0%. ## Reproduction ```bash # Start vLLM server VLLM_USE_V1=1 \ SAFETENSORS_FAST_GPU=1 \ VLLM_ROCM_USE_AITER=0 \ VLLM_ROCM_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: version**: v0.15.0 - **Model**: moonshotai/Kimi-K2.5 (compressed-tensors INT4 quantization) ### 🐛 Describe the bug ## Issue Running Kimi-K2.5 on AMD MI308X produces completely incorrect outputs. The gsm8k benchmark accu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: [ROCm] Kimi-K2.5 produces incorrect results on AMD MI308X bug;rocm ### Your current environment ## Environment - **GPU**: AMD Instinct MI308X - **vLLM version**: v0.15.0 - **Model**: moonshotai/Kimi-K2.5 (compres...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: \ --gpu-memory-utilization 0.8 --load-format fastsafetensors \ --block-size 64 --async-scheduling \ --compilation-config '{"cudagraph_mode": "FULL_AND_PIECEWISE", "custom_ops": ["+rotary_embedding"]}' # Run evaluation l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vironment - **GPU**: AMD Instinct MI308X - **vLLM version**: v0.15.0 - **Model**: moonshotai/Kimi-K2.5 (compressed-tensors INT4 quantization) ### 🐛 Describe the bug ## Issue Running Kimi-K2.5 on AMD MI308X produces comp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
