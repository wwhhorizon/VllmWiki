# vllm-project/vllm#38687: [Bug]: parity with CUDA: ROCm nightly & release docker images aren't built with Pollara AINIC or Broadcom Thor-2 NICs

| 字段 | 值 |
| --- | --- |
| Issue | [#38687](https://github.com/vllm-project/vllm/issues/38687) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: parity with CUDA: ROCm nightly & release docker images aren't built with Pollara AINIC or Broadcom Thor-2 NICs

### Issue 正文摘录

### Your current environment all the nightly images in https://hub.docker.com/r/vllm/vllm-openai-rocm/tags as of April 1st, 2026 `vllm/vllm-openai-rocm:v0.18.1` `vllm/vllm-openai-rocm:v0.18.0` ### 🐛 Describe the bug hi @hongxiayang +viz @powderluv @chunfangamd @andyluo7 @ChuanLi1101 Unlike ROCm SGLang, `mori` multinode does not work out of the box in these. the drivers for the NIC is missing and MoRI AMD collective library is not built with the NIC types so it is broken. We have a cluster with AMD's Pollara AINIC & have a cluster with Thor-2 NICs. Since there is lots of AMD GPU clusters deployment in the world with AMD Pollara AINIC & there is also lots of AMD GPU clusters deployment in the world with Thor-2 NICs. & the MoRI README says it supports both NICs https://github.com/ROCm/mori the vLLM docker have images that support both. Recommendation would be for the main image to support Pollara AINIC drivers & MoRI built with AINIC and then have concurrent image build in the pipeline to support MoRI Thor-2 NIC. i.e. - `vllm/vllm-openai-rocm:v0.xx.x` (supports MoRI Pollara) - `vllm/vllm-openai-rocm:v0.xx.x-bxnt` (supports MoRI Thor2) Lets ensure that ROCm vLLM has parity with the us...

## 现有链接修复摘要

#40360 [ROCm][MoRI] Add layer for building bnxt (Thor2) NIC stack | #40453 Update Dockerfile.rocm for AINIC & Thor NIC

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: parity with CUDA: ROCm nightly & release docker images aren't built with Pollara AINIC or Broadcom Thor-2 NICs bug;rocm ### Your current environment all the nightly images in https://hub.docker.com/r/vllm/vllm-op...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: parity with CUDA: ROCm nightly & release docker images aren't built with Pollara AINIC or Broadcom Thor-2 NICs bug;rocm ### Your current environment all the nightly images in https://hub.docker.com/r/vllm/vllm-op...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting cuda build_error #40360 [R...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40360](https://github.com/vllm-project/vllm/pull/40360) | closes_keyword | 0.95 | [ROCm][MoRI] Add layer for building bnxt (Thor2) NIC stack  | Fixes #38687. This PR adds installation of Thor2 drivers and userspace libraries directly into `Dockerfile.rocm`. This way the rocm docker can be used directly with MoRI on node |
| [#40453](https://github.com/vllm-project/vllm/pull/40453) | closes_keyword | 0.95 | Update Dockerfile.rocm for AINIC & Thor NIC | Fixes #38687. This PR installs Thor2 and AINIC userspace libraries by default into the ROCm vLLM image. This allows for MoRI to be directly used on MI300/MI355 platforms where A |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
