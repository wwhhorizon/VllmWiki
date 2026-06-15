# vllm-project/vllm#8745: Error loading models since versions 0.6.1xxx

| 字段 | 值 |
| --- | --- |
| Issue | [#8745](https://github.com/vllm-project/vllm/issues/8745) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Error loading models since versions 0.6.1xxx

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.31 Python version: 3.11.7 (main, Dec 15 2023, 18:12:31) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-187-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 GPU 3: NVIDIA A40 Nvidia driver version: 535.183.01 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 57 bits virtual CPU(s): 96 On-line CPU(s) list: 0-95 Thread(s) per core: 2 Core(s) per socket: 24 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 106 Model name: Intel(R) Xeon(R) Gold 6336Y CPU @ 2.40GHz Stepping: 6 CPU MHz: 800.012 BogoMIPS: 4800.00 Vir...

## 现有链接修复摘要

#8157 [Core][Bugfix][Perf] Introduce `MQLLMEngine` to avoid `asyncio` OH

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Error loading models since versions 0.6.1xxx installation ### Your current environment ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: rent environment ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Error loading models since versions 0.6.1xxx installation ### Your current environment ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 2...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: current environment ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: last): File " ", line 1, in File "/home/ido.amit/miniconda3/envs/benchmark/lib/python3.11/multiprocessing/spawn.py", line 122, in spawn_main exitcode = _main(fd, parent_sentinel) ^^^^^^^^^^^^^^^^^^^^^^^^^^

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8157](https://github.com/vllm-project/vllm/pull/8157) | mentioned | 0.45 | [Core][Bugfix][Perf] Introduce `MQLLMEngine` to avoid `asyncio` OH | vailable version through pip is the old 0.6.1.post2. for example, [#8157](https://github.com/vllm-project/vllm/pull/8157) possibly fix issue [#8553](https://github.com/vllm-projec… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
