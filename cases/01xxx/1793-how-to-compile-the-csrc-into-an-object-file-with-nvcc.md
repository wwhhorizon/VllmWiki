# vllm-project/vllm#1793: How to compile the `csrc` into an object file with `nvcc`?

| 字段 | 值 |
| --- | --- |
| Issue | [#1793](https://github.com/vllm-project/vllm/issues/1793) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> How to compile the `csrc` into an object file with `nvcc`?

### Issue 正文摘录

Hello everybody, I am trying to compile the `csrc` part of `vllm` into an object file (excluding the Python bindings). However, I cannot find a way to do this. This is the command I was using: ``` "nvcc" "-ccbin=c++" "-Xcompiler" "-O0" "-Xcompiler" "-ffunction-sections" "-Xcompiler" "-fdata-sections" "-Xcompiler" "-fPIC" "-G" "-Xcompiler" "-gdwarf-4" "-Xcompiler" "-fno-omit-frame-pointer" "-m64" "-Xcompiler" "-Wall" "-Xcompiler" "-Wextra" "-I /home/ericbuehler/.local/lib/python3.10/site-packages/torch/include" "-I /home/ericbuehler/.local/lib/python3.10/site-packages/torch/include/torch/csrc/api/include" "-I /usr/include/python3.10" "-gencode" "arch=compute_62,code=sm_62" "-o" "/home/ericbuehler/candle-vllm/target/debug/build/candle-vllm-40c333732b7323b5/out/csrc/attention/attention_kernels.o" "-c" "csrc/attention/attention_kernels.cu" ``` It simply attempts to compile all `*.cu` files for a Jetson TX2 GPU (compute 6.2) as a test case, and provides paths to my libraries. However, it fails with an error code 1 and an error message that I could not find in the log. I have read the `setup.py` and see [this](https://github.com/vllm-project/vllm/blob/7c600440f7560348e571f021f2b2d1469de...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: How to compile the `csrc` into an object file with `nvcc`? Hello everybody, I am trying to compile the `csrc` part of `vllm` into an object file (excluding the Python bindings). However, I cannot find a way to do this....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: include/torch/csrc/api/include" "-I /usr/include/python3.10" "-gencode" "arch=compute_62,code=sm_62" "-o" "/home/ericbuehler/candle-vllm/target/debug/build/candle-vllm-40c333732b7323b5/out/csrc/attention/attention_kerne...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: mpts to compile all `*.cu` files for a Jetson TX2 GPU (compute 6.2) as a test case, and provides paths to my libraries. However, it fails with an error code 1 and an error message that I could not find in the log. I hav...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
