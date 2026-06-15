# vllm-project/vllm#4654: [Bug]: CPU Docker build quickstart `static library kineto_LIBRARY-NOTFOUND not found`

| 字段 | 值 |
| --- | --- |
| Issue | [#4654](https://github.com/vllm-project/vllm/issues/4654) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CPU Docker build quickstart `static library kineto_LIBRARY-NOTFOUND not found`

### Issue 正文摘录

### Your current environment Fresh ubuntu instance with docker CE installed ### 🐛 Describe the bug Simply running `docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g .` from https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#quick-start-using-dockerfile throws the following error. Using a ubuntu 24.04 build on a dedicated cpu amd hetzner cloud VM. ``` 3.794 CMake Warning at /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message): 3.794 static library kineto_LIBRARY-NOTFOUND not found. 3.794 Call Stack (most recent call first): 3.794 /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Torch/TorchConfig.cmake:127 (append_torchlib_if_found) 3.794 CMakeLists.txt:67 (find_package) 3.794 3.794 3.795 -- Found Torch: /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch.so 3.799 CMake Error at cmake/cpu_extension.cmake:57 (message): 3.799 vLLM CPU backend requires AVX512 ISA support. 3.799 Call Stack (most recent call first): 3.799 CMakeLists.txt:88 (include) 3.799 3.799 3.800 -- Configuring incomplete, errors occurred! 3.826 Traceback (most recent call last): 3.826 File "/workspace/vllm/setup.py", line 397, in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: CPU Docker build quickstart `static library kineto_LIBRARY-NOTFOUND not found` bug ### Your current environment Fresh ubuntu instance with docker CE installed ### 🐛 Describe the bug Simply running `docker build -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: CMake Error at cmake/cpu_extension.cmake:57 (message): 3.799 vLLM CPU backend requires AVX512 ISA support. 3.799 Call Stack (most recent call first): 3.799 CMakeLists.txt:88 (include) 3.799 3.799 3.800 -- Configuring in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: UT_DIRECTORY=/workspace/vllm/build/lib.linux-x86_64-3.10/vllm', '-DCMAKE_ARCHIVE_OUTPUT_DIRECTORY=build/temp.linux-x86_64-3.10', '-DVLLM_TARGET_DEVICE=cpu', '-DVLLM_PYTHON_EXECUTABLE=/usr/bin/python3', '-DCMAKE_JOB_POOL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: at /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message): 3.794 static library kineto_LIBRARY-NOTFOUND not found. 3.794 Call Stack (most recent call first): 3.794 /usr/local/lib/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: file.cpu -t vllm-cpu-env --shm-size=4g .` from https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#quick-start-using-dockerfile throws the following error. Using a ubuntu 24.04 build on a dedicated cpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
