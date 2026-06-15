# vllm-project/vllm#8996: [Installation]: RISC-V support?

| 字段 | 值 |
| --- | --- |
| Issue | [#8996](https://github.com/vllm-project/vllm/issues/8996) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: RISC-V support?

### Issue 正文摘录

### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Fedora Linux 38 (Thirty Eight) (riscv64) GCC version: (GCC) 13.2.1 20230728 (Red Hat 13.2.1-1) Clang version: Could not collect CMake version: version 3.27.4 Libc version: glibc-2.37 Python version: 3.11.5 (main, Sep 15 2023, 00:00:00) [GCC 13.2.1 20230728 (Red Hat 13.2.1-1)] (64-bit runtime) Python platform: Linux-6.1.80-riscv64-with-glibc2.37 Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: riscv64 Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 NUMA node(s): 8 NUMA node0 CPU(s): 0-7,16-23 NUMA node1 CPU(s): 8-15,24-31 NUMA node2 CPU(s): 32-39,48-55 NUMA node3 CPU(s): 40-47,56-63 NUMA node4 CPU(s): 64-71,80-87 NUMA node5 CPU(s): 72-79,88-95 NUMA node6 CPU(s): 96-103,112-119 NUMA node7 CPU(s): 104-111,120-127 Versions of relevant libraries: [pip3] No relevant...

## 现有链接修复摘要

#20292 [Hardware][RISC-V] Add RISC-V architecture cpu inference support | #22112 [Hardware][RISC-V] Add riscv64 support for vLLM with scalar

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: RISC-V support? installation;stale ### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Fedora Linux 38 (Thirt
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ur current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Fedora Linux 38 (Thirty Eight) (riscv64) GCC version: (GCC) 13.2.1 20230728 (Re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: A runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: RISC-V support? installation;stale ### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Fedora Linux 38 (Thirt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting;model_support cuda build_error env_dependency #...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20292](https://github.com/vllm-project/vllm/pull/20292) | mentioned | 0.6 | [Hardware][RISC-V] Add RISC-V architecture  cpu inference support | enables vLLM to run efficiently on RISC-V CPUs, related to #19611 and #8996. ## Changes - Add csrc/cpu/cpu_types_riscv.hpp, which implement fp16/bf16/fp32 - Add kernel for RISC-V… |
| [#22112](https://github.com/vllm-project/vllm/pull/22112) | mentioned | 0.6 | [Hardware][RISC-V] Add riscv64 support for vLLM with scalar | nd FP32(see csrc/cpu/cpu_types_scalar.hpp). Related to issue #19611 , #8996 and #20292 with rvv. Also, implementation supports other unsupported architectures as well. ## Test Pla… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
