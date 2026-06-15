# vllm-project/vllm#36077: [Bug]: FlashInfer JIT build fails when serving Qwen3.5-35B-A3B (nvcc path found but ninja build fails)

| 字段 | 值 |
| --- | --- |
| Issue | [#36077](https://github.com/vllm-project/vllm/issues/36077) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer JIT build fails when serving Qwen3.5-35B-A3B (nvcc path found but ninja build fails)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` (EngineCore_DP0 pid=1359765) ERROR 03-05 09:56:09 [core.py:1100] :/usr/local/cuda-12.8/bin/nvcc --generate-dependencies-with-compile --dependency-output /root/.cache/flashinfer/0.6.4/89/cached_ops/batch_prefill_with_kv_cache_dtype_q_bf16_dtype_kv_e4m3_dtype_o_bf16_dtype_idx_i32_head_dim_qk_256_head_dim_vo_256_posenc_0_use_swa_False_use_logits_cap_False_f16qk_False/batch_prefill_jit_binding.cuda.o.d -DPy_LIMITED_API=0x03090000 -D_GLIBCXX_USE_CXX11_ABI=1 -isystem /data/tools/conda/envs/vLLM_new/include/python3.11 -isystem :/usr/local/cuda-12.8/include -isystem :/usr/local/cuda-12.8/include/cccl -isystem /data/tools/conda/envs/vLLM_new/lib/python3.11/site-packages/tvm_ffi/include -isystem /data/tools/conda/envs/vLLM_new/lib/python3.11/site-packages/tvm_ffi/include -isystem /data/tools/conda/envs/vLLM_new/lib/python3.11/site-packages/flashinfer/data/include -isystem /data/tools/conda/envs/vLLM_new/lib/python3.11/site-packages/flashinfer/data/csrc -isystem /data/tools/conda/envs/vLLM_new/lib/python3.11/site-packages/flashinfer/data/cutlass/include -isystem /data/tools/conda/envs/vLLM_new/lib/python3.11/site-packages/flashinfer/dat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: FlashInfer JIT build fails when serving Qwen3.5-35B-A3B (nvcc path found but ninja build fails) bug ### Your current environment ### 🐛 Describe the bug ``` (EngineCore_DP0 pid=1359765) ERROR 03-05 09:56:09 [core....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: /root/.cache/flashinfer/0.6.4/89/cached_ops/batch_prefill_with_kv_cache_dtype_q_bf16_dtype_kv_e4m3_dtype_o_bf16_dtype_idx_i32_head_dim_qk_256_head_dim_vo_256_posenc_0_use_swa_False_use_logits_cap_False_f16qk_False/batch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: FlashInfer JIT build fails when serving Qwen3.5-35B-A3B (nvcc path found but ninja build fails) bug ### Your current environment ### 🐛 Describe the bug ``` (EngineCore_DP0 pid=1359765) ERROR 03-05 09:56:09 [core....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ineCore_DP0 pid=1359765) ERROR 03-05 09:56:09 [core.py:1100] :/usr/local/cuda-12.8/bin/nvcc --generate-dependencies-with-compile --dependency-output /root/.cache/flashinfer/0.6.4/89/cached_ops/batch_prefill_with_kv_cach...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: FlashInfer JIT build fails when serving Qwen3.5-35B-A3B (nvcc path found but ninja build fails) bug ### Your current environment ### 🐛 Describe the bug ``` (EngineCore_DP0 pid=1359765) ERROR 03-05 09:56:09 [core....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
