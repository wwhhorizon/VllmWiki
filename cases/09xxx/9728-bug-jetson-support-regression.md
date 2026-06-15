# vllm-project/vllm#9728: [Bug]:  Jetson support regression

| 字段 | 值 |
| --- | --- |
| Issue | [#9728](https://github.com/vllm-project/vllm/issues/9728) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Jetson support regression

### Issue 正文摘录

### Your current environment see below ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm currently in the process of updating the [nixpkgs build definition](https://github.com/conroy-cheers/nixpkgs/blob/update-vllm-0.6.3/pkgs/development/python-modules/vllm/default.nix) for vLLM from 0.5.3.post1 to 0.6.3.post1. Build works great on x86_64 machine with NVIDIA GPU, and have successfully built for aarch64 Jetson Orin AGX with correct dependency / CUDA library versions. Unfortunately, at runtime on the Jetson, vLLM fails to start engine process: ``` File "/nix/store/x5bz4k7prp7vdvm4i01y0z0lbi4awad7-python3.12-vllm-0.6.3.post1/lib/python3.12/site-packages/vllm/utils.py", line 799, in current_memory_usage return mem ^^^ UnboundLocalError: cannot access local variable 'mem' where it is not associated with a value ``` Have traced this back to the root cause - [newer versions of vLLM use NVML to detect CUDA support](https://github.com/vllm-project/vllm/blob/v0.6.3.post1/vllm/platforms/cuda.py). NVML is not supported on Jetson, so unfortunately it isn't possible to proceed without making changes to vLLM here. I'd be happy to open a PR to add a fallback mode on CUDA platforms wh...

## 现有链接修复摘要

#9735 [Hardware][NVIDIA] Add non-NVML CUDA mode for Jetson

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Describe the bug I'm currently in the process of updating the [nixpkgs build definition](https://github.com/conroy-cheers/nixpkgs/blob/update-vllm-0.6.3/pkgs/development/python-modules/vllm/default.nix) for vLLM from 0....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: reat on x86_64 machine with NVIDIA GPU, and have successfully built for aarch64 Jetson Orin AGX with correct dependency / CUDA library versions. Unfortunately, at runtime on the Jetson, vLLM fails to start engine proces...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Jetson support regression bug ### Your current environment see below ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm currently in the process of updating the [nixpkgs build definition](https://gith...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: without making changes to vLLM here. I'd be happy to open a PR to add a fallback mode on CUDA platforms where NVML isn't supported, if the maintainers would be open to it? Otherwise I will have to maintain a patch downs...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tson support regression bug ### Your current environment see below ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm currently in the process of updating the [nixpkgs build definition](https://github.com/co...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9735](https://github.com/vllm-project/vllm/pull/9735) | closes_keyword | 0.95 | [Hardware][NVIDIA] Add non-NVML CUDA mode for Jetson | Fixes #9728 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
