# vllm-project/vllm#7497: [Bug]: Dockerfile Build breaks in local

| 字段 | 值 |
| --- | --- |
| Issue | [#7497](https://github.com/vllm-project/vllm/issues/7497) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;moe |
| 子分类 |  |
| Operator 关键词 | cuda;moe |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Dockerfile Build breaks in local

### Issue 正文摘录

### Your current environment using docker desktop to build vllm ### 🐛 Describe the bug Whenever you will try to build the image using the dockerfile in the repo. the build fails at line 114: && python3 setup.py bdist_wheel --dist-dir=dist --py-limited-api=cp38 \ Error: .98 /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Caffe2/Caffe2Config.cmake:86 (include) 13.98 /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Torch/TorchConfig.cmake:68 (find_package) 13.98 CMakeLists.txt:67 (find_package) 13.98 13.98 13.98 -- Added CUDA NVCC flags for: -gencode;arch=compute_70,code=sm_70;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_80,code=sm_80; -gencode;arch=compute_86,code=sm_86;-gencode;arch=compute_89,code=sm_89;-gencode;arch=compute_90,code=sm_90;-gencode;arch=compute_90,code=comput e_90 14.00 CMake Warning at /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message): 14.00 static library kineto_LIBRARY-NOTFOUND not found. 14.00 Call Stack (most recent call first): 14.00 /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Torch/TorchConfig.cmake:120 (append_torchlib_if_found) 14.00 CMakeLists.txt:67 (find_package)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Bug]: Dockerfile Build breaks in local bug;stale ### Your current environment using docker desktop to build vllm ### 🐛 Describe the bug Whenever you will try to build the image using the dockerfile in the repo. the bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: age) 13.98 CMakeLists.txt:67 (find_package) 13.98 13.98 13.98 -- Added CUDA NVCC flags for: -gencode;arch=compute_70,code=sm_70;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_80,code=sm_80; -gencode;arch=comp...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: guring cuBLAS ... done. 32.16 -- Enabling C extension. 32.16 -- Enabling moe extension. 32.16 -- Configuring done (28.1s) 32.26 -- Generating done (0.1s) 32.26 -- Build files have been written to: /workspace/build/temp....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -real;89-real;90-real;90-virtual 31.95 -- CMake Version: 3.30.2 31.95 -- CUTLASS 3.5.1 31.95 -- CUDART: /usr/local/cuda/lib64/libcudart.so 31.95 -- CUDA Driver: /usr/local/cuda/lib64/stubs/libcuda.so 31.95 -- NVRTC: /us...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 90,code=[compute_90]" -Xcompiler=-fPIC --expt-relaxed-constexpr -DENABLE_FP8 --thread s=8 -D_GLIBCXX_USE_CXX11_ABI=0 -MD -MT CMakeFiles/_C.dir/csrc/cache_kernels.cu.o -MF CMakeFiles/_C.dir/csrc/cache_kernels.cu.o.d -x c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
