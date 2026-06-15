# vllm-project/vllm#24464: [Bug]: Building vLLM with CUDA 13.0

| 字段 | 值 |
| --- | --- |
| Issue | [#24464](https://github.com/vllm-project/vllm/issues/24464) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Building vLLM with CUDA 13.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to build vLLM with CUDA 13.0 is currently failing because of some breaking changes from https://nvidia.github.io/cccl/cccl/3.0_migration_guide.html: ``` #34 62.31 /workspace/csrc/layernorm_kernels.cu(33): error: namespace "cub" has no member "Sum" #34 62.31 variance = BlockReduce(reduceStore).Reduce(variance, cub::Sum{}, blockDim.x); ``` Here is an example build failure from PyTorch CI https://github.com/pytorch/pytorch/actions/runs/17510237984/job/49740804047. With the introduction of CUDA 13.0 support in PyTorch 2.9 https://dev-discuss.pytorch.org/t/pytorch-release-2-9-0-key-dates/3178, vLLM would need to be updated to work with CUDA 13.0 to unblock the use of PyTorch 2.9. For reference, the same breaking changes have been fixed on PyTorch in https://github.com/pytorch/pytorch/pull/153373 cc @simon-mo @youkaichao @atalman @Aidyn-A @zou3519 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#24598 Fixes CCCL/CUB usage for CUDA 13

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Building vLLM with CUDA 13.0 bug ### Your current environment ### 🐛 Describe the bug Trying to build vLLM with CUDA 13.0 is currently failing because of some breaking changes from https://nvidia.github.io/cccl/cc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Building vLLM with CUDA 13.0 bug ### Your current environment ### 🐛 Describe the bug Trying to build vLLM with CUDA 13.0 is currently failing because of some breaking changes from https://nvidia.github.io/cccl/cc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error env_dependency #24598 Fixes CCCL/CUB usage for CUDA 13 Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 33): error: namespace "cub" has no member "Sum" #34 62.31 variance = BlockReduce(reduceStore).Reduce(variance, cub::Sum{}, blockDim.x); ``` Here is an example build failure from PyTorch CI https://github.com/pytorch/pyt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. development ci_build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error env_dependency #24598 Fixes CCCL/CUB usage for CUDA 13 Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24598](https://github.com/vllm-project/vllm/pull/24598) | closes_keyword | 0.95 | Fixes CCCL/CUB usage for CUDA 13 | Fixes #24464 "Building vLLM with CUDA 13.0". ## Test Plan No plans. Just build. --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
