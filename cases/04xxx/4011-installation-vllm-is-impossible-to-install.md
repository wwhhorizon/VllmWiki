# vllm-project/vllm#4011: [Installation]: VLLM is impossible to install. 

| 字段 | 值 |
| --- | --- |
| Issue | [#4011](https://github.com/vllm-project/vllm/issues/4011) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: VLLM is impossible to install. 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.26.3 Libc version: glibc-2.31 Python version: 3.10.13 | packaged by conda-forge | (main, Dec 23 2023, 15:36:39) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.4.0-173-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.0.76 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla P100-PCIE-16GB GPU 1: Tesla P100-PCIE-16GB GPU 2: Tesla P100-PCIE-16GB GPU 3: Tesla P100-PCIE-16GB GPU 4: Tesla P100-PCIE-16GB GPU 5: Tesla P100-PCIE-16GB Nvidia driver version: 525.147.05 cuDNN version: /usr/lib/x86_64-linux-gnu/libcudnn.so.7.0.5 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 46 bits physical, 48 bits virtual CPU(s): 56 On-line CPU(s) list...

## 现有链接修复摘要

#4047 Add troubleshooting advice for building from source

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: VLLM is impossible to install. installation ### Your current environment ```text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug buil
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `text The output of `python collect_env.py` ``` Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s of relevant libraries: [pip3] numpy==1.26.3 [pip3] torch==2.2.1 [pip3] triton==2.2.0 [conda] numpy 1.26.3 py310hb13e2d6_0 conda-forge [conda] torch 2.2.1 pypi_0 pypi [conda] triton 2.2.0

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4047](https://github.com/vllm-project/vllm/pull/4047) | closes_keyword | 0.95 | Add troubleshooting advice for building from source | FIX #4011 (*link existing issues this PR will resolve*) --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> < |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
