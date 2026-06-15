# vllm-project/vllm#30755: [Feature][P1]: Separation of building and final base images on more variants

| 字段 | 值 |
| --- | --- |
| Issue | [#30755](https://github.com/vllm-project/vllm/issues/30755) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature][P1]: Separation of building and final base images on more variants

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now the dockerfiles used to build CUDA-enabled images use different base images for building (`base`) and serving (`vllm-base`). But other variants (e.g. CPU) do not have such a mechanism. The separation itself is meaningful because we have different requirements for them: * The build base image should be as old as possible because we would like to ship the wheel with the most compatibility (especially libc) we can achieve. For CUDA variants, they are often limited by the base devel / runtime image provided by NVIDIA. E.g., there is `cuda:12.9.1-devel-ubuntu20.04` (`manylinux_2_31`), but for CUDA 13.1 we only have `13.1.0-devel-ubuntu22.04` (`manylinux_2_35`). For CPU variants, there is more flexibility. * The serving (called "final" in dockerfile) base image should be kept updated to avoid security vulnerabilities and to allow users to put in their own artifacts. E.g., @junpuf recently mentioned that there is a ffmpeg CVE in the current image, which is based on ubuntu 22.04. As for now, I suggest that we: * Rewrite `Dockerfile.cpu` to implement such separation. E.g., to use `20.04` as build base, and `24.04` as serving base. * Bump the serv...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Feature][P1]: Separation of building and final base images on more variants feature request;stale ### 🚀 The feature, motivation and pitch Now the dockerfiles used to build CUDA-enabled images use different base images...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: # 🚀 The feature, motivation and pitch Now the dockerfiles used to build CUDA-enabled images use different base images for building (`base`) and serving (`vllm-base`). But other variants (e.g. CPU) do not have such a mec...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: Separation of building and final base images on more variants feature request;stale ### 🚀 The feature, motivation and pitch Now the dockerfiles used to build CUDA-enabled images use different base images for building...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting cuda build_error 🚀 The feature, mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
