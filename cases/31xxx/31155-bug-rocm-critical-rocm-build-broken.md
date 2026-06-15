# vllm-project/vllm#31155: [Bug] [ROCm] [Critical]: ROCm build broken

| 字段 | 值 |
| --- | --- |
| Issue | [#31155](https://github.com/vllm-project/vllm/issues/31155) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;moe |
| 子分类 | precision |
| Operator 关键词 | moe |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [ROCm] [Critical]: ROCm build broken

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This PR introduces some changes that broke ROCm vllm build. https://github.com/vllm-project/vllm/pull/30821 ``` DTORCH_HIP_VERSION=700 -Wno-shift-count-negative -Wno-shift-count-overflow -Wno-duplicate-decl-specifier -DCAFFE2_USE_MIOPEN -DTHRUST_DEVICE_SYSTEM=THRUST_DEVICE_SYSTEM_HIP -std=c++17 -DHIP_ENABLE_WARP_SYNC_BUILTINS -DHIPBLASLT_OUTER_VEC -DUSE_ROCM_CK_GEMM -MD -MT CMakeFiles/_C.dir/csrc/fused_qknorm_rope_kernel.hip.o -MF CMakeFiles/_C.dir/csrc/fused_qknorm_rope_kernel.hip.o.d -o CMakeFiles/_C.dir/csrc/fused_qknorm_rope_kernel.hip.o -x hip -c /app/vllm/build/temp.linux-x86_64-cpython-312/csrc/fused_qknorm_rope_kernel.hip #13 132.3 /app/vllm/build/temp.linux-x86_64-cpython-312/csrc/fused_qknorm_rope_kernel.hip:409:11: error: unused variable 'rotary_dim' [-Werror,-Wunused-variable] #13 132.3 409 | int64_t rotary_dim = cos_sin_cache.size(1); #13 132.3 | ^~~~~~~~~~ #13 132.3 1 error generated when compiling for gfx90a. #13 138.6 [8/37] Building CXX object CMakeFiles/_rocm_C.dir/csrc/rocm/torch_bindings.cpp.o #13 138.6 cc1plus: warning: command-line option ‘-Wno-duplicate-decl-specifier’ is valid for C/ObjC but not for C++ #1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug] [ROCm] [Critical]: ROCm build broken bug;rocm ### Your current environment ### 🐛 Describe the bug This PR introduces some changes that broke ROCm vllm build. https://github.com/vllm-project/vllm/pull/30821 ``` DTO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug] [ROCm] [Critical]: ROCm build broken bug;rocm ### Your current environment ### 🐛 Describe the bug This PR introduces some changes that broke ROCm vllm build. https://github.com/vllm-project/vllm/pull/30821 ``` DTOR
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ++17 -DHIP_ENABLE_WARP_SYNC_BUILTINS -DHIPBLASLT_OUTER_VEC -DUSE_ROCM_CK_GEMM -MD -MT CMakeFiles/_C.dir/csrc/fused_qknorm_rope_kernel.hip.o -MF CMakeFiles/_C.dir/csrc/fused_qknorm_rope_kernel.hip.o.d -o CMakeFiles/_C.di...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. correctness ci_build;hardware_porting;moe moe build_error;nan_inf env_dependency Your...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
