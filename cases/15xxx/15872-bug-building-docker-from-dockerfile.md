# vllm-project/vllm#15872: [Bug]: building docker from Dockerfile

| 字段 | 值 |
| --- | --- |
| Issue | [#15872](https://github.com/vllm-project/vllm/issues/15872) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;moe |
| 子分类 | install |
| Operator 关键词 | cuda;moe |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: building docker from Dockerfile

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Can't build from Dockerfile. `DOCKER_BUILDKIT=1 docker build . -t registry.jsc.fz-juelich.de/sdlaml/blablador/vllm --file Dockerfile` Results in ```python ... #31 67.58 -- Found Python: /usr/bin/python3 (found version "3.12.9") found components: Interpreter Development.Module Development.SABIModule #31 71.29 CMake Warning at .deps/vllm-flash-attn-src/CMakeLists.txt:75 (message): #31 71.29 Pytorch version 2.4.0 expected for CUDA build, saw 2.6.0 instead. #31 71.29 #31 71.29 #31 71.29 -- CUDA target architectures: 7.0;7.5;8.0;8.6;8.9;9.0 #31 71.29 -- CUDA supported target architectures: 8.0;8.6;8.9;9.0 #31 75.39 -- FA2_ARCHS: 8.0;9.0 #31 75.40 -- FA3_ARCHS: 9.0a;8.0 #31 75.42 -- vllm-flash-attn is available at /workspace/.deps/vllm-flash-attn-src #31 75.42 -- Configuring done (58.3s) #31 75.57 -- Generating done (0.2s) #31 75.57 -- Build files have been written to: /workspace/build/temp.linux-x86_64-cpython-312 #31 75.60 Using MAX_JOBS=2 as the number of jobs. #31 75.60 /bin/sh: 1: lsmod: not found #31 75.62 Using NVCC_THREADS=8 as the number of nvcc threads. #31 78.64 [1/308] Building CXX object CMakeFiles/_moe_C.dir/csrc/moe/torc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Bug]: building docker from Dockerfile bug;stale ### Your current environment ### 🐛 Describe the bug Can't build from Dockerfile. `DOCKER_BUILDKIT=1 docker build . -t registry.jsc.fz-juelich.de/sdlaml/blablador/vllm --f
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: keLists.txt:75 (message): #31 71.29 Pytorch version 2.4.0 expected for CUDA build, saw 2.6.0 instead. #31 71.29 #31 71.29 #31 71.29 -- CUDA target architectures: 7.0;7.5;8.0;8.6;8.9;9.0 #31 71.29 -- CUDA supported targe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: hitectures: 8.0;8.6;8.9;9.0 #31 75.39 -- FA2_ARCHS: 8.0;9.0 #31 75.40 -- FA3_ARCHS: 9.0a;8.0 #31 75.42 -- vllm-flash-attn is available at /workspace/.deps/vllm-flash-attn-src #31 75.42 -- Configuring done (58.3s) #31 75...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: g -DNDEBUG -std=c++17 -Xcompiler=-fPIC --expt-relaxed-constexpr -DENABLE_FP8 --threads=8 -DENABLE_SCALED_MM_SM90=1 -DENABLE_SCALED_MM_C2X=1 -DENABLE_SPARSE_SCALED_MM_C3X=1 -D_GLIBCXX_USE_CXX11_ABI=0 -gencode arch=comput...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: umber of nvcc threads. #31 78.64 [1/308] Building CXX object CMakeFiles/_moe_C.dir/csrc/moe/torch_bindings.cpp.o #31 78.69 [2/308] Building CXX object CMakeFiles/cumem_allocator.dir/csrc/cumem_allocator.cpp.o #31 79.51...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
