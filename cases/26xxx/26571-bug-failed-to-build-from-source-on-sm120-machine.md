# vllm-project/vllm#26571: [Bug]: failed to build from source on sm120 machine

| 字段 | 值 |
| --- | --- |
| Issue | [#26571](https://github.com/vllm-project/vllm/issues/26571) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: failed to build from source on sm120 machine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` >>> import vllm._C Traceback (most recent call last): File " ", line 1, in ImportError: /home/vllm/code/vllm/vllm/_C.abi3.so: undefined symbol: _Z20cutlass_moe_mm_sm100RN2at6TensorERKS0_S3_S3_S3_S3_S3_S3_S3_S3_bb ``` This is because `scaled_mm_entry.cu` was compiled with `ENABLE_CUTLASS_MOE_SM100`. ``` /usr/local/cuda-12.8/bin/nvcc \ -forward-unknown-to-host-compiler \ -DCUTLASS_ENABLE_DIRECT_CUDA_DRIVER_CALL=1 \ -DPy_LIMITED_API=3 \ -DTORCH_EXTENSION_NAME=_C \ -DUSE_C10D_GLOO -DUSE_C10D_NCCL \ -DUSE_DISTRIBUTED -DUSE_RPC \ -DUSE_TENSORPIPE -D_C_EXPORTS \ -I/home/vllm/code/vllm/csrc \ -I/home/vllm/code/vllm/cmake-build-release/_deps/cutlass-src/include \ -I/home/vllm/code/vllm/cmake-build-release/_deps/cutlass-src/tools/util/include \ -isystem /usr/include/python3.12 \ -isystem /home/vllm/code/vllm/.venv/lib/python3.12/site-packages/torch/include \ -isystem /home/vllm/code/vllm/.venv/lib/python3.12/site-packages/torch/include/torch/csrc/api/include \ -isystem /usr/local/cuda-12.8/include \ -DONNX_NAMESPACE=onnx_c2 \ -Xcudafe \ --diag_suppress=cc_clobber_ignored,--diag_suppress=field_without_dll_interface,--diag_suppress=base_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: failed to build from source on sm120 machine bug;stale ### Your current environment ### 🐛 Describe the bug ``` >>> import vllm._C Traceback (most recent call last): File " ", line 1, in ImportError: /home/vllm/co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: _sm100RN2at6TensorERKS0_S3_S3_S3_S3_S3_S3_S3_S3_bb ``` This is because `scaled_mm_entry.cu` was compiled with `ENABLE_CUTLASS_MOE_SM100`. ``` /usr/local/cuda-12.8/bin/nvcc \ -forward-unknown-to-host-compiler \ -DCUTLASS...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: failed to build from source on sm120 machine bug;stale ### Your current environment ### 🐛 Describe the bug ``` >>> import vllm._C Traceback (most recent call last): File " ", line 1, in ImportError: /home/vllm/co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ImportError: /home/vllm/code/vllm/vllm/_C.abi3.so: undefined symbol: _Z20cutlass_moe_mm_sm100RN2at6TensorERKS0_S3_S3_S3_S3_S3_S3_S3_S3_bb ``` This is because `scaled_mm_entry.cu` was compiled with `ENABLE_CUTLASS_MOE_SM...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ror: /home/vllm/code/vllm/vllm/_C.abi3.so: undefined symbol: _Z20cutlass_moe_mm_sm100RN2at6TensorERKS0_S3_S3_S3_S3_S3_S3_S3_S3_bb ``` This is because `scaled_mm_entry.cu` was compiled with `ENABLE_CUTLASS_MOE_SM100`. ``...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
