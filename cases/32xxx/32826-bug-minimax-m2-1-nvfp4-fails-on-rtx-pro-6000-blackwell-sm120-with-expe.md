# vllm-project/vllm#32826: [Bug]: MiniMax-M2.1 NVFP4 fails on RTX PRO 6000 Blackwell (SM120) with expert parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#32826](https://github.com/vllm-project/vllm/issues/32826) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;gemm;kernel;moe;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MiniMax-M2.1 NVFP4 fails on RTX PRO 6000 Blackwell (SM120) with expert parallel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## How would you like to use vllm Running MiniMax-M2.1 NVFP4 with expert parallel on dual RTX PRO 6000 Blackwell GPUs. ## Before submitting a new issue... - [x] I have searched existing issues to see if this problem has already been reported. - [x] I have verified this is not a deployment/server configuration issue. ## Problem Description Running MiniMax-M2.1 NVFP4 on RTX PRO 6000 Blackwell (SM120) fails with two different errors depending on configuration: ### Error 1: FlashInfer MoE FP4 JIT compilation failure When `VLLM_USE_FLASHINFER_MOE_FP4=1`, JIT compilation fails with missing CUDA headers: ``` /usr/local/lib/python3.12/dist-packages/flashinfer/data/csrc/nv_internal/include/tensorrt_llm/common/cudaUtils.h:19:10: fatal error: cublasLt.h: No such file or directory 19 | #include | ^~~~~~~~~~~~ compilation terminated. ninja: build stopped: subcommand failed. RuntimeError: Engine core initialization failed. ``` This occurs during compilation of `fused_moe_120` kernels (SM120 specific): - `moe_gemm_kernels_fp8_uint4.cuda.o` - `moe_gemm_kernels_bf16_fp4.cuda.o` - `flashinfer_cutlass_fused_moe_sm100_binding.cuda.o` - etc. ### Erro...

## 现有链接修复摘要

#43044 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | #43047 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug]: MiniMax-M2.1 NVFP4 fails on RTX PRO 6000 Blackwell (SM120) with expert parallel bug;stale ### Your current environment ### 🐛 Describe the bug ## How would you like to use vllm Running MiniMax-M2.1 NVFP4 with expe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: MiniMax-M2.1 NVFP4 fails on RTX PRO 6000 Blackwell (SM120) with expert parallel bug;stale ### Your current environment ### 🐛 Describe the bug ## How would you like to use vllm Running MiniMax-M2.1 NVFP4 with expe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: #include | ^~~~~~~~~~~~ compilation terminated. ninja: build stopped: subcommand failed. RuntimeError: Engine core initialization failed. ``` This occurs during compilation of `fused_moe_120` kernels (SM120 specific): -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ails with two different errors depending on configuration: ### Error 1: FlashInfer MoE FP4 JIT compilation failure When `VLLM_USE_FLASHINFER_MOE_FP4=1`, JIT compilation fails with missing CUDA headers: ``` /usr/local/li...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ady been reported. - [x] I have verified this is not a deployment/server configuration issue. ## Problem Description Running MiniMax-M2.1 NVFP4 on RTX PRO 6000 Blackwell (SM120) fails with two different errors depending...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43044](https://github.com/vllm-project/vllm/pull/43044) | mentioned | 0.6 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | . Partially addresses the same root cause in #38918, #36802, #41063, #32826. ### Motivation Triton kernels in vLLM often ship with autotune config lists tuned for the largest shme… |
| [#43047](https://github.com/vllm-project/vllm/pull/43047) | mentioned | 0.6 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | . Partially addresses the same root cause in #38918, #36802, #41063, #32826. ### Motivation Triton kernels in vLLM often ship with autotune config lists tuned for the largest shme… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
