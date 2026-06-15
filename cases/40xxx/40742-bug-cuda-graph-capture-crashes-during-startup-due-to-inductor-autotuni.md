# vllm-project/vllm#40742: [Bug]: CUDA graph capture crashes during startup due to Inductor autotuning torch.cuda.synchronize() inside graph capture (FULL_DECODE_ONLY + MLA + FP8) when PDL is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#40742](https://github.com/vllm-project/vllm/issues/40742) |
| 状态 | open |
| 标签 | torch.compile |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;quantization;triton |
| 症状 | build_error;crash;nondeterministic |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA graph capture crashes during startup due to Inductor autotuning torch.cuda.synchronize() inside graph capture (FULL_DECODE_ONLY + MLA + FP8) when PDL is enabled

### Issue 正文摘录

## Your current environment - **vLLM commit**: `d622e27d2be9cd4321d75073e4b7ef522204853d` - **PyTorch**: bundled in the container (aarch64) - **GPU**: NVIDIA GB200 (GH200-based, aarch64) - **CUDA**: Container default ## Model `nvidia/Kimi-K2.5-NVFP4` (DeepSeek V2 architecture with MLA attention, FP4/FP8 quantized) ## Bug description When launching a vLLM decode server with `--compilation_config.cudagraph_mode FULL_DECODE_ONLY` **and PDL enabled** (`TRTLLM_ENABLE_PDL=1`, `TORCHINDUCTOR_ENABLE_PDL=1`), the server crashes during startup at the `profile_cudagraph_memory()` phase. The root cause is that PyTorch Inductor's `CachingAutotuner` calls `torch.cuda.synchronize()` inside an active CUDA graph capture, which is an illegal CUDA operation. This issue appears to be specific to the PDL (Programmatic Dependent Launch) codepath — the same configuration without PDL env vars does not trigger this crash. ### Error chain 1. `gpu_worker.py` → `determine_available_memory()` → `model_runner.profile_cudagraph_memory()` 2. `gpu_model_runner.py` → `_warmup_and_capture()` → `_dummy_run()` → enters `torch.cuda.graph()` context 3. During the captured forward pass, the model runs through `deepseek_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e graph capture (FULL_DECODE_ONLY + MLA + FP8) when PDL is enabled torch.compile ## Your current environment - **vLLM commit**: `d622e27d2be9cd4321d75073e4b7ef522204853d` - **PyTorch**: bundled in the container (aarch64...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: torch.cuda.synchronize() inside graph capture (FULL_DECODE_ONLY + MLA + FP8) when PDL is enabled torch.compile ## Your current environment - **vLLM commit**: `d622e27d2be9cd4321d75073e4b7ef522204853d` - **PyTorch**: bun...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Inductor autotuning torch.cuda.synchronize() inside graph capture (FULL_DECODE_ONLY + MLA + FP8) when PDL is enabled torch.compile ## Your current environment - **vLLM commit**: `d622e27d2be9cd4321d75073e4b7ef522204853d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: eepseek_v2.py` → `mla_attention.py` → `_decode_concat_quant_fp8_op` 4. A Triton kernel (`triton_poi_fused__to_copy_cat_clamp_mul_reciprocal_view_0`) is encountered for the first time and hasn't been autotuned 5. Inducto...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: error: operation failed due to a previous error during capture ``` ### Reproducer ```bash # Environment variables (required to trigger the bug) export TRTLLM_ENABLE_PDL=1 export TORCHINDUCTOR_ENABLE_PDL=1 export TORCHIN...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
