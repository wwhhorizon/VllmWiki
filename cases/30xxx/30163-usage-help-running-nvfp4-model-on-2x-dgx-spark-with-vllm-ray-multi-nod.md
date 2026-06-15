# vllm-project/vllm#30163: [Usage]: Help Running NVFP4 model on 2x DGX Spark with vLLM + Ray (multi-node)

| 字段 | 值 |
| --- | --- |
| Issue | [#30163](https://github.com/vllm-project/vllm/issues/30163) |
| 状态 | closed |
| 标签 | usage;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;gemm;kernel;moe;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Help Running NVFP4 model on 2x DGX Spark with vLLM + Ray (multi-node)

### Issue 正文摘录

### Your current environment # Help: Running NVFP4 model on 2x DGX Spark with vLLM + Ray (multi-node) ## Hardware - **2x DGX Spark** (GB10 GPU each, sm_121a / compute capability 12.1) - Connected via 200GbE ConnectX-7/Ethernet - Driver: 580.95.05, Host CUDA: 13.0 ## Goal Run `lukealonso/GLM-4.6-NVFP4` (357B MoE model, NVFP4 quantization) across both nodes using vLLM with Ray distributed backend. ## What I've Tried ### 1. `nvcr.io/nvidia/vllm:25.11-py3` (NGC) - vLLM 0.11.0 - **Error:** `FlashInfer kernels unavailable for ModelOptNvFp4FusedMoE on current platform` - NVFP4 requires vLLM 0.12.0+ ### 2. `vllm/vllm-openai:nightly-aarch64` (vLLM 0.11.2.dev575) - With `VLLM_USE_FLASHINFER_MOE_FP4=1` - **Error:** `ptxas fatal: Value 'sm_121a' is not defined for option 'gpu-name'` - Triton's bundled ptxas 12.8 doesn't support GB10 ### 3. `vllm/vllm-openai:v0.12.0-aarch64` (vLLM 0.12.0) - Fixed ptxas with symlink: `ln -sf /usr/local/cuda/bin/ptxas /usr/local/lib/python3.12/dist-packages/triton/backends/nvidia/bin/ptxas` - Triton compilation passes ✅ - **Error:** `RuntimeError: [FP4 gemm Runner] Failed to run cutlass FP4 gemm on sm120. Error: Error Internal` ### 4. Tried both parallelism mode...

## 现有链接修复摘要

#35568 [Bugfix] Fix SM121 (DGX Spark) exclusion from Marlin/CUTLASS FP8 paths | #35947 fix: Software E2M1 conversion for SM12x NVFP4 activation quantization

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 9: vLLM + Ray (multi-node) ## Hardware - **2x DGX Spark** (GB10 GPU each, sm_121a / compute capability 12.1) - Connected via 200GbE ConnectX-7/Ethernet - Driver: 580.95.05, Host CUDA: 13.0 ## Goal Run `lukealonso/GLM-4.6-N...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: . `vllm/vllm-openai:v0.12.0-aarch64` (vLLM 0.12.0) - Fixed ptxas with symlink: `ln -sf /usr/local/cuda/bin/ptxas /usr/local/lib/python3.12/dist-packages/triton/backends/nvidia/bin/ptxas` - Triton compilation passes ✅ -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: l, NVFP4 quantization) across both nodes using vLLM with Ray distributed backend. ## What I've Tried ### 1. `nvcr.io/nvidia/vllm:25.11-py3` (NGC) - vLLM 0.11.0 - **Error:** `FlashInfer kernels unavailable for ModelOptNv...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: Help Running NVFP4 model on 2x DGX Spark with vLLM + Ray (multi-node) usage;unstale ### Your current environment # Help: Running NVFP4 model on 2x DGX Spark with vLLM + Ray (multi-node) ## Hardware - **2x DGX S...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Help Running NVFP4 model on 2x DGX Spark with vLLM + Ray (multi-node) usage;unstale ### Your current environment # Help: Running NVFP4 model on 2x DGX Spark with vLLM + Ray (multi-node) ## Hardware - **2x DGX S...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35568](https://github.com/vllm-project/vllm/pull/35568) | closes_keyword | 0.95 | [Bugfix] Fix SM121 (DGX Spark) exclusion from Marlin/CUTLASS FP8 paths | Fixes #30163. Relates to #30135. Contributed by Second Nature Computing (https://joinsecondnature.com) ## Test plan - [x] Validated on SM121a hardware (DGX Spark) - [x] Marlin F |
| [#35947](https://github.com/vllm-project/vllm/pull/35947) | closes_keyword | 0.95 | fix: Software E2M1 conversion for SM12x NVFP4 activation quantization | Fixes #35519, #30163 Contributed by [Second Nature Computing](https://joinsecondnature.com) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
