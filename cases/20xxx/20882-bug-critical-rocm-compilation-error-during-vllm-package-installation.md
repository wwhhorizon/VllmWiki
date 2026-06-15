# vllm-project/vllm#20882: [Bug] [Critical] [ROCm]: Compilation error during vLLM package installation

| 字段 | 值 |
| --- | --- |
| Issue | [#20882](https://github.com/vllm-project/vllm/issues/20882) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [Critical] [ROCm]: Compilation error during vLLM package installation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This commit [[Model] New model support for microsoft/Phi-4-mini-flash-reasoning (#… · vllm-project/vllm@2c11a73](https://github.com/vllm-project/vllm/commit/2c11a738b35e6e65731c5ad7774581ca2c33dc6a) break mamba support on ROCm and vllm is not able to compile successfully during installation step `python3 setup.py develop` ``` [4/5] Building HIP object CMakeFiles/_C.dir/csrc/mamba/mamba_ssm/selective_scan_fwd.hip.o FAILED: CMakeFiles/_C.dir/csrc/mamba/mamba_ssm/selective_scan_fwd.hip.o /opt/rocm-6.4.1/lib/llvm/bin/clang++ -DCUTLASS_ENABLE_DIRECT_CUDA_DRIVER_CALL=1 -DPy_LIMITED_API=3 -DTORCH_EXTENSION_NAME=_C -DUSE_C10D_GLOO -DUSE_C10D_NCCL -DUSE_DISTRIBUTED -DUSE_PROF_API=1 -DUSE_RPC -DUSE_TENSORPIPE -D_C_EXPORTS -D__HIP_PLATFORM_AMD__ -D__HIP_PLATFORM_AMD__=1 -D__HIP_ROCclr__=1 -I/app/upstreamupgradeaiter/mtp-v1/csrc -isystem /usr/include/python3.10 -isystem /usr/local/lib/python3.10/dist-packages/torch/include -isystem /usr/local/lib/python3.10/dist-packages/torch/include/torch/csrc/api/include -isystem /opt/rocm-6.4.1/include/hiprand -isystem /opt/rocm-6.4.1/include/rocrand -Wno-unused-result -O2 -g -DNDEBUG --offload-arch=gfx9...

## 现有链接修复摘要

#20883 [ROCm] [Bugfix] [Critical]: Fix mamba compilation bug

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug] [Critical] [ROCm]: Compilation error during vLLM package installation bug ### Your current environment ### 🐛 Describe the bug This commit [[Model] New model support for microsoft/Phi-4-mini-flash-reasoning (#… · v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug] [Critical] [ROCm]: Compilation error during vLLM package installation bug ### Your current environment ### 🐛 Describe the bug This commit [[Model] New model support for microsoft/Phi-4-mini-flash-reasoning (#… · v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: mba_ssm/selective_scan_fwd.hip.o /opt/rocm-6.4.1/lib/llvm/bin/clang++ -DCUTLASS_ENABLE_DIRECT_CUDA_DRIVER_CALL=1 -DPy_LIMITED_API=3 -DTORCH_EXTENSION_NAME=_C -DUSE_C10D_GLOO -DUSE_C10D_NCCL -DUSE_DISTRIBUTED -DUSE_PROF_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: LF_CONVERSIONS__=1 -DHIP_ENABLE_WARP_SYNC_BUILTINS=1 -DUSE_ROCM -DENABLE_FP8 -U__HIP_NO_HALF_CONVERSIONS__ -U__HIP_NO_HALF_OPERATORS__ -Werror=unused-variable -fno-gpu-rdc -D_GLIBCXX_USE_CXX11_ABI=1 -DTORCH_HIP_VERSION=...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: tem /opt/rocm-6.4.1/include/rocrand -Wno-unused-result -O2 -g -DNDEBUG --offload-arch=gfx942 -fPIC -fPIC -D__HIP_PLATFORM_AMD__=1 -DUSE_ROCM=1 -DHIPBLAS_V2 -DCUDA_HAS_FP16=1 -D__HIP_NO_HALF_OPERATORS__=1 -D__HIP_NO_HALF...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20883](https://github.com/vllm-project/vllm/pull/20883) | closes_keyword | 0.95 | [ROCm] [Bugfix] [Critical]: Fix mamba compilation bug | FIX #20882 ## Test Plan Able to install on ROCm. Run mamba unit tests - `tests/kernels/mamba/test_causal_conv1d.py` - `tests/kernels/mamba/test_mamba_mixer2.py` - `tests/kernels |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
