# vllm-project/vllm#32373: [Bug]: Fail to load vLLM on new NVIDIA driver

| 字段 | 值 |
| --- | --- |
| Issue | [#32373](https://github.com/vllm-project/vllm/issues/32373) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 44; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fail to load vLLM on new NVIDIA driver

### Issue 正文摘录

### Your current environment I can't run `collect_env.py` because importing PyTorch itself is failing. ### 🐛 Describe the bug After https://github.com/vllm-project/vllm/pull/30784, I start seeing vLLM failing to load on its benchmark job. I suspect that the change doesn't work with newer NVIDIA driver that the job is using to be compatible with CUDA 13.0 ``` +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 580.105.08 Driver Version: 580.105.08 CUDA Version: 13.0 | +-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA B200 Off | 00000000:D1:00.0 Off | 0 | | N/A 32C P0 141W / 750W | 0MiB / 183359MiB | 0% Default | | | | Disabled | +-----------------------------------------+------------------------+----------------------+ +-----------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID...

## 现有链接修复摘要

#32377 [Docker] Remove CUDA compatibility library loading; fixes #32373 | #32474 [Docker][Hotfix] CUDA compatibility enablement | #33992 [Bugfix] Fix CUDA compatibility path setting for both datacenter and consumer NVIDIA GPUs | #34821 [Bugfix] Make CUDA compat library loading opt-in to fix consumer GPUs

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: r bug ### Your current environment I can't run `collect_env.py` because importing PyTorch itself is failing. ### 🐛 Describe the bug After https://github.com/vllm-project/vllm/pull/30784, I start seeing vLLM failing to l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ork with newer NVIDIA driver that the job is using to be compatible with CUDA 13.0 ``` +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 580.105.08 Driver Version:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: vllm-project/vllm/pull/30784, I start seeing vLLM failing to load on its benchmark job. I suspect that the change doesn't work with newer NVIDIA driver that the job is using to be compatible with CUDA 13.0 ``` +--------...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: GI CI PID Type Process name GPU Memory | | ID ID Usage | |=========================================================================================| | No running processes

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32377](https://github.com/vllm-project/vllm/pull/32377) | closes_keyword | 0.95 | [Docker] Remove CUDA compatibility library loading; fixes #32373 | fixes #32373 which is a bug introduced by #30784 . ## Purpose ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist < |
| [#32474](https://github.com/vllm-project/vllm/pull/32474) | closes_keyword | 0.95 | [Docker][Hotfix] CUDA compatibility enablement | Fixes #32373 |
| [#33992](https://github.com/vllm-project/vllm/pull/33992) | closes_keyword | 0.95 | [Bugfix] Fix CUDA compatibility path setting for both datacenter and consumer NVIDIA GPUs | Fix #32373 Fix #33369 Closes #34226 Fixes the core problem in https://github.com/vllm-project/vllm/issues/32373 and https://github.com/vllm-project/vllm/issues/33369, introduced f |
| [#34821](https://github.com/vllm-project/vllm/pull/34821) | closes_keyword | 0.95 | [Bugfix] Make CUDA compat library loading opt-in to fix consumer GPUs | Fixes #32373 Related: #33992, #34226 ### Changes 1. **`docker/Dockerfile`**: Replace persistent `cuda-compat.conf` ldconfig entries with `ENV VLLM_ENABLE_CUDA_COMPATIBILITY=0` in |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
