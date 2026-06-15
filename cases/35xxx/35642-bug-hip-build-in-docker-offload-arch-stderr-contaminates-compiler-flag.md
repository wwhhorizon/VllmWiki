# vllm-project/vllm#35642: [Bug]: HIP build in Docker: offload-arch stderr contaminates compiler flags via cmake/utils.cmake and CMAKE_HIP_FLAGS

| 字段 | 值 |
| --- | --- |
| Issue | [#35642](https://github.com/vllm-project/vllm/issues/35642) |
| 状态 | open |
| 标签 | bug;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: HIP build in Docker: offload-arch stderr contaminates compiler flags via cmake/utils.cmake and CMAKE_HIP_FLAGS

### Issue 正文摘录

### Your current environment - Fedora 43 (Docker) - ROCm: TheRock nightlies 7.11.0a20260106 (gfx1151) - PyTorch: 2.11.0a0+rocm7.11.0a20260106 - vLLM: step-audio2-mini branch (stepfun-ai/vllm), but bug exists in mainline cmake/utils.cmake - CMake: 3.31.10 - Hardware: AMD Ryzen AI Max+ 395, Radeon 8060S (gfx1151), 128GB unified memory ### 🐛 Describe the bug ## Summary Building vLLM with HIP inside Docker (no GPU passthrough at build time) fails because `offload-arch` stderr output gets baked into compiler flags through two independent paths, causing `clang++` to interpret the warning string as a filename. ## Error ``` clang++: error: no such file or directory: '[WARNING] offload-arch failed with return code 1[stderr] -D__HIP_PLATFORM_AMD__=1' ninja: build stopped: subcommand failed. ``` ## Root Cause Two contamination paths: ### Path 1: cmake/utils.cmake (line 116-117) `get_torch_gpu_compiler_flags()` runs: ```python import torch.utils.cpp_extension as t; print(';'.join(t.COMMON_HIP_FLAGS + t.COMMON_HIPCC_FLAGS)) ``` When PyTorch initializes `cpp_extension`, it runs `offload-arch` which fails in Docker (no GPU). The warning string gets captured into `COMMON_HIPCC_FLAGS` and passed t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: HIP build in Docker: offload-arch stderr contaminates compiler flags via cmake/utils.cmake and CMAKE_HIP_FLAGS bug;rocm;stale ### Your current environment - Fedora 43 (Docker) - ROCm: TheRock nightlies 7.11.0a202...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: HIP build in Docker: offload-arch stderr contaminates compiler flags via cmake/utils.cmake and CMAKE_HIP_FLAGS bug;rocm;stale ### Your current environment - Fedora 43 (Docker) - ROCm: TheRock nightlies 7.11.0a202...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: )|" cmake/utils.cmake ``` ### For Path 2 — sanitize build.ninja between configure and build: Patch `setup.py` to insert a sanitizer in `build_extensions()` between `self.configure(ext)` and `subprocess.check_call(["cmak...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: uses instructions not supported on gfx1151. Fix: `--enforce-eager` 2. **Triton flash attention doesn't support SWA on this arch** — Fix: `VLLM_USE_TRITON_FLASH_ATTN=0` (use CK flash attention) ## Working Dockerfile ```...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i;hardware_porting;model_support attention;cuda;triton build_error;crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
