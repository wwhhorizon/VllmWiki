# vllm-project/vllm#21751: [Bug]: Fail to build in arm64 CPU.

| 字段 | 值 |
| --- | --- |
| Issue | [#21751](https://github.com/vllm-project/vllm/issues/21751) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Fail to build in arm64 CPU.

### Issue 正文摘录

### Your current environment gcc version 12.3.1 ### 🐛 Describe the bug Build by following [https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html#build-wheel-from-source](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html#build-wheel-from-source) ``` pip install --upgrade pip pip install -v -r requirements/cpu-build.txt --extra-index-url https://download.pytorch.org/whl/cpu pip install -v -r requirements/cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu VLLM_TARGET_DEVICE=cpu python setup.py install ``` but got: ``` -- Build type: RelWithDebInfo -- Target device: cpu -- Found python matching: /data2/conda/envs/vllm2/bin/python. CMake Warning at /data2/conda/envs/vllm/lib/python3.12/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message): static library kineto_LIBRARY-NOTFOUND not found. Call Stack (most recent call first): /data2/conda/envs/vllm/lib/python3.12/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:125 (append_torchlib_if_found) CMakeLists.txt:80 (find_package) -- ARMv8 or later architecture detected CMake Warning at cmake/cpu_extension.cmake:166 (message): BF16 functionality is not available Call Stack (mo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Fail to build in arm64 CPU. bug ### Your current environment gcc version 12.3.1 ### 🐛 Describe the bug Build by following [https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html#build-wheel-from-sou...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ure detected CMake Warning at cmake/cpu_extension.cmake:166 (message): BF16 functionality is not available Call Stack (most recent call first): CMakeLists.txt:97 (include) -- DNNL_TARGET_ARCH: AARCH64 -- DNNL_LIBRARY_NA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: torchlib_if_found) CMakeLists.txt:80 (find_package) -- ARMv8 or later architecture detected CMake Warning at cmake/cpu_extension.cmake:166 (message): BF16 functionality is not available Call Stack (most recent call firs...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: onda/envs/vllm/lib/python3.12/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message): static library kineto_LIBRARY-NOTFOUND not found. Call Stack (most recent call first): /data2/conda/envs/vllm/lib/pytho...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: bled primitive CPU ISA: ALL -- Enabled primitive GPU ISA: ALL -- Enabled GeMM kernels ISA: ALL -- Primitive cache is enabled -- CPU extension compile flags: -fopenmp;-DVLLM_CPU_EXTENSION;-march=armv8.2-a+dotprod+fp16 --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
