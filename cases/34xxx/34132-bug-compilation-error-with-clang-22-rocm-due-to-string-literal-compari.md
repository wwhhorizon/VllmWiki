# vllm-project/vllm#34132: [Bug]: Compilation Error with Clang 22+ (ROCm) due to String Literal Comparison in  quant_utils.cuh

| 字段 | 值 |
| --- | --- |
| Issue | [#34132](https://github.com/vllm-project/vllm/issues/34132) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;quantization |
| 子分类 | build_fail |
| Operator 关键词 | fp8;quantization |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Compilation Error with Clang 22+ (ROCm) due to String Literal Comparison in  quant_utils.cuh

### Issue 正文摘录

### Your current environment Environment - OS: Fedora 43 (Container) - Compiler: AMD clang version 22.0.0git - ROCm Version: 6.3 (nightly) - GPU: AMD Ryzen AI Max "Strix Halo" (gfx1151) ### 🐛 Describe the bug When compiling vLLM with a newer Clang version (e.g., AMD clang version 22.0.0git), the build fails with -Wstring-compare and -Warray-compare errors. This is caused by the DISPATCH_BY_KV_CACHE_DTYPE macro in `csrc/quantization/w8a8/fp8/amd/quant_utils.cuh` comparing the KV_DTYPE template argument (which is a string literal) using ==. Full build log: https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/actions/runs/21778795245/job/62839590033 Error Log ```csrc/cache_kernels.hip:1298:3: warning: comparison between two arrays compare their addresses and will be deprecated in c++20 [-Warray-compare] DISPATCH_BY_KV_CACHE_DTYPE(k.dtype(), "fp8_e4m3", ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ csrc/quantization/w8a8/fp8/amd/quant_utils.cuh:643:18: note: expanded from macro 'DISPATCH_BY_KV_CACHE_DTYPE' if (KV_DTYPE == "auto") { ~~~~~~~~ ^ ~~~~~~ ``` # Steps to Reproduce - Use a toolchain with Clang 22+ (which treats this warning as an error by default or via -Werror). - Buil...

## 现有链接修复摘要

#34469 [Bugfix][Hardware][AMD] Fix string literal comparison in DISPATCH_BY_KV_CACHE_DTYPE macro

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Your current environment Environment - OS: Fedora 43 (Container) - Compiler: AMD clang version 22.0.0git - ROCm Version: 6.3 (nightly) - GPU: AMD Ryzen AI Max "Strix Halo" (gfx1151) ### 🐛 Describe the bug When compi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ilation Error with Clang 22+ (ROCm) due to String Literal Comparison in quant_utils.cuh bug;rocm ### Your current environment Environment - OS: Fedora 43 (Container) - Compiler: AMD clang version 22.0.0git - ROCm Versio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Compilation Error with Clang 22+ (ROCm) due to String Literal Comparison in quant_utils.cuh bug;rocm ### Your current environment Environment - OS: Fedora 43 (Container) - Compiler: AMD clang version 22.0.0git -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: with -Wstring-compare and -Warray-compare errors. This is caused by the DISPATCH_BY_KV_CACHE_DTYPE macro in `csrc/quantization/w8a8/fp8/amd/quant_utils.cuh` comparing the KV_DTYPE template argument (which is a string li...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: if (KV_DTYPE == "auto") { ~~~~~~~~ ^ ~~~~~~ ``` # Steps to Reproduce - Use a toolchain with Clang 22+ (which treats this warning as an error by default or via -Werror). - Build vLLM from source. # Proposed Fix Explicitl...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34469](https://github.com/vllm-project/vllm/pull/34469) | closes_keyword | 0.95 | [Bugfix][Hardware][AMD] Fix string literal comparison in DISPATCH_BY_KV_CACHE_DTYPE macro | Fixes #34132 ## Test plan - Build vLLM with Clang 22+ / ROCm 6.3+ (previously failed at `csrc/cache_kernels.hip:1298`) - Verify existing AMD CI tests continue to pass (the fix is |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
