# vllm-project/vllm#6769: [Installation]: Unable to build docker image using Dockerfile.openvino

| 字段 | 值 |
| --- | --- |
| Issue | [#6769](https://github.com/vllm-project/vllm/issues/6769) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Installation]: Unable to build docker image using Dockerfile.openvino

### Issue 正文摘录

### Your current environment ```text (base) user@zahid:~/vllm$ python collect_env.py Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: Could not collect Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.12.1 | packaged by Anaconda, Inc. | (main, Jan 19 2024, 15:51:05) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-1026-intel-iotg-x86_64-with-glibc2.35 Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 57 bits virtual Byte Order: Little Endian CPU(s): 128 On-line CPU(s) list: 0-127 Vendor ID: GenuineIntel Model name: Intel(R) Xeon(R) Gold 6338N CPU @ 2.20GHz CPU family: 6 Model: 106 Thread(s) per core: 2 Core(s) per socket: 32 Socket(s): 2 Stepping:...

## 现有链接修复摘要

#6517 [CI/Build] Build on Ubuntu 20.04 instead of 22.04

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: Unable to build docker image using Dockerfile.openvino installation ### Your current environment ```text (base) user@zahid:~/vllm$ python collect_env.py Collecting environment information... PyTorch versi
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: Could not collect Clang version: Coul...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: (base) user@zahid:~/vllm$ python collect_env.py Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Sto...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: kspace/vllm/requirements-build.txt 20 | # build vLLM with OpenVINO backend 21 | RUN PIP_PRE=1 PIP_EXTRA_INDEX_URL="https://download.pytorch.org/whl/cpu https://storage.openvinotoolkit.org/simple/wheels/nightly/" VLLM_TA...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6517](https://github.com/vllm-project/vllm/pull/6517) | mentioned | 0.45 | [CI/Build] Build on Ubuntu 20.04 instead of 22.04 | om/vllm-project/vllm/commit/1689219ebf01c750de492271832e27c39df38648)[#6517](https://github.com/vllm-project/vllm/pull/6517)[)](https://github.com/vllm-project/vllm/commit/1689219… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
