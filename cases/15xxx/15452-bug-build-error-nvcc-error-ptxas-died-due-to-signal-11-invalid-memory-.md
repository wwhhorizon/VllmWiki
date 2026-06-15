# vllm-project/vllm#15452: [Bug]: Build error, nvcc error   : 'ptxas' died due to signal 11 (Invalid memory reference)

| 字段 | 值 |
| --- | --- |
| Issue | [#15452](https://github.com/vllm-project/vllm/issues/15452) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Build error, nvcc error   : 'ptxas' died due to signal 11 (Invalid memory reference)

### Issue 正文摘录

### Your current environment L20, CUDA 12.6, PyTorch 2.6.0 ### 🐛 Describe the bug ```bash FAILED: vllm-flash-attn/CMakeFiles/_vllm_fa3_C.dir/hopper/instantiations/flash_fwd_hdimall_fp16_paged_split_sm90.cu.o /usr/local/cuda/bin/nvcc -forward-unknown-to-host-compiler -DFLASHATTENTION_DISABLE_BACKWARD -DFLASHATTENTION_DISABLE_DROPOUT -DFLASHATTENTION_DISABLE_PYBIND -DFLASHATTENTION_DISABLE_UNEVEN_K -DFLASHATTENTION_VARLEN_ONLY -DPy_LIMITED_API=3 -DTORCH_EXTENSION_NAME=_vllm_fa3_C -DUSE_C10D_GLOO -DUSE_C10D_NCCL -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -D_vllm_fa3_C_EXPORTS -I/workspace/dev/vipshop/vllm/.deps/vllm-flash-attn-src/csrc -I/workspace/dev/vipshop/vllm/.deps/vllm-flash-attn-src/hopper -I/workspace/dev/vipshop/vllm/.deps/vllm-flash-attn-src/csrc/common -I/workspace/dev/vipshop/vllm/.deps/vllm-flash-attn-src/csrc/cutlass/include -isystem /usr/include/python3.12 -isystem /usr/local/lib/python3.12/dist-packages/torch/include -isystem /usr/local/lib/python3.12/dist-packages/torch/include/torch/csrc/api/include -isystem /usr/local/cuda/include -DONNX_NAMESPACE=onnx_c2 -Xcudafe --diag_suppress=cc_clobber_ignored,--diag_suppress=field_without_dll_interface,--diag_suppress=base...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Build error, nvcc error : 'ptxas' died due to signal 11 (Invalid memory reference) bug ### Your current environment L20, CUDA 12.6, PyTorch 2.6.0 ### 🐛 Describe the bug ```bash FAILED: vllm-flash-attn/CMakeFiles/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Build error, nvcc error : 'ptxas' died due to signal 11 (Invalid memory reference) bug ### Your current environment L20, CUDA 12.6, PyTorch 2.6.0 ### 🐛 Describe the bug ```bash FAILED: vllm-flash-attn/CMakeFiles/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ### 🐛 Describe the bug ```bash FAILED: vllm-flash-attn/CMakeFiles/_vllm_fa3_C.dir/hopper/instantiations/flash_fwd_hdimall_fp16_paged_split_sm90.cu.o /usr/local/cuda/bin/nvcc -forward-unknown-to-host-compiler -DFLASHATTE...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: g -DNDEBUG -std=c++17 -Xcompiler=-fPIC --expt-relaxed-constexpr -DENABLE_FP8 --threads=1 --expt-extended-lambda --use_fast_math -DCUTLASS_ENABLE_DIRECT_CUDA_DRIVER_CALL=1 -D_GLIBCXX_USE_CXX11_ABI=0 -gencode arch=compute...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ly asked questions. performance attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting cuda build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
