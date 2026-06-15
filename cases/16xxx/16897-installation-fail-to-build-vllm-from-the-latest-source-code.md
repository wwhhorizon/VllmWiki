# vllm-project/vllm#16897: [Installation]: Fail to build vllm from the latest source code

| 字段 | 值 |
| --- | --- |
| Issue | [#16897](https://github.com/vllm-project/vllm/issues/16897) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Fail to build vllm from the latest source code

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 14.0.0-1ubuntu1.1 CMake version: version 3.24.4 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.10.134-010.ali5000.al8.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: LAZY NVIDIA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 CUBLAS_VERSION=12.3.4.1 NVIDIA_REQUIRE_CUDA=cuda>=9.0 CUDA_CACHE_DISABLE=1 NCCL_VERSION=2.19.3 NVIDIA_DRIVER_CAPABILITIES=all NVIDIA_PRODUCT_NAME=Triton Server CUDA_VERSION=12.3.2.001 CUDNN_VERSION=8.9.7.29+cuda12.2 NVIDIA_TRITON_SERVER_VERSION=23.12 ``` ### How you are installing vllm ```sh MAX_JOBS=6 pip install -e . -v ``` ``` 3 errors detected in the compilation of "/home/logs/vllm/.deps/vllm-flash-attn-src/hopper/instantiations/flash_fwd_hdimall_e4m3_paged_softcap_sm90.cu". [295/314] Building CUDA object vllm-flash-attn/CMakeFiles/_vllm_f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: Fail to build vllm from the latest source code installation ### Your current environment ```text The output of `python collect_env.py` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ython collect_env.py` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 1 NCCL_VERSION=2.19.3 NVIDIA_DRIVER_CAPABILITIES=all NVIDIA_PRODUCT_NAME=Triton Server CUDA_VERSION=12.3.2.001 CUDNN_VERSION=8.9.7.29+cuda12.2 NVIDIA_TRITON_SERVER_VERSION=23.12 ``` ### How you are installing vllm ```sh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: f `python collect_env.py` PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: g -DNDEBUG -std=c++17 -Xcompiler=-fPIC --expt-relaxed-constexpr -DENABLE_FP8 --threads=1 --expt-extended-lambda --use_fast_math -DCUTLASS_ENABLE_DIRECT_CUDA_DRIVER_CALL=1 -D_GLIBCXX_USE_CX X11_ABI=0 -gencode arch=comput...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
