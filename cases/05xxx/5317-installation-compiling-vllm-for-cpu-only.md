# vllm-project/vllm#5317: [Installation]: Compiling VLLM for cpu only.

| 字段 | 值 |
| --- | --- |
| Issue | [#5317](https://github.com/vllm-project/vllm/issues/5317) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Compiling VLLM for cpu only.

### Issue 正文摘录

To ease the bug report I prepared a google colab notebook: https://colab.research.google.com/drive/1wd29UiknYI3r-8H5Inco9IkWYcuZAVNR?usp=sharing I followed the instructions in the documentation and this is what I got: ``` -- The CXX compiler identification is GNU 12.3.0 -- Detecting CXX compiler ABI info -- Detecting CXX compiler ABI info - done -- Check for working CXX compiler: /usr/bin/c++ - skipped -- Detecting CXX compile features -- Detecting CXX compile features - done -- Build type: RelWithDebInfo -- Target device: cpu -- Found Python: /usr/bin/python3 (found version "3.10.12") found components: Interpreter Development.Module -- Found python matching: /usr/bin/python3. CMake Warning at /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message): static library kineto_LIBRARY-NOTFOUND not found. Call Stack (most recent call first): /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Torch/TorchConfig.cmake:127 (append_torchlib_if_found) CMakeLists.txt:67 (find_package) -- Found Torch: /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch.so CMake Error at cmake/cpu_extension.cmake:57 (message): vLLM CPU backend requires AVX512 I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: Compiling VLLM for cpu only. installation;stale To ease the bug report I prepared a google colab notebook: https://colab.research.google.com/drive/1wd29UiknYI3r-8H5Inco9IkWYcuZAVNR?usp=sharing I followed
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: h.so CMake Error at cmake/cpu_extension.cmake:57 (message): vLLM CPU backend requires AVX512 ISA support. Call Stack (most recent call first): CMakeLists.txt:88 (include) -- Configuring incomplete, errors occurred! Trac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se the bug report I prepared a google colab notebook: https://colab.research.google.com/drive/1wd29UiknYI3r-8H5Inco9IkWYcuZAVNR?usp=sharing I followed the instructions in the documentation and this is what I got: ``` --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: at /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message): static library kineto_LIBRARY-NOTFOUND not found. Call Stack (most recent call first): /usr/local/lib/python3.10/dist-pa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: Compiling VLLM for cpu only. installation;stale To ease the bug report I prepared a google colab notebook: https://colab.research.google.com/drive/1wd29UiknYI3r-8H5Inco9IkWYcuZAVNR?usp=sharing I followed...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
