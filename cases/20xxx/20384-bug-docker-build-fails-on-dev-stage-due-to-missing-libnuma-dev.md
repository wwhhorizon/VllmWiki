# vllm-project/vllm#20384: [Bug]: Docker build fails on dev stage due to missing libnuma-dev

| 字段 | 值 |
| --- | --- |
| Issue | [#20384](https://github.com/vllm-project/vllm/issues/20384) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker build fails on dev stage due to missing libnuma-dev

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Bug Description The Docker build process for the `dev` target fails on a clean environment. This is because a system dependency (`libnuma-dev`) required by the `fastsafetensors` Python package is missing from the base image. ### To Reproduce 1. Use the Dev Containers feature in VS Code / Cursor to build the environment from the `main` branch. 2. The target stage is `dev` in `docker/Dockerfile`. 3. The process will fail during the `RUN uv pip install -r requirements/dev.txt` step. ### Error Log The key error message during the compilation is: [stderr] fastsafetensors/cpp/ext.hpp:22:10: fatal error: numa.h: No such file or directory ### Proposed Solution The issue can be resolved by adding `libnuma-dev` to the `apt-get install` command in the `base` stage of the `docker/Dockerfile`. ```diff - && apt-get install -y ccache software-properties-common git curl sudo \ + && apt-get install -y ccache software-properties-common git curl sudo libnuma-dev \ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](http...

## 现有链接修复摘要

#38950 [Docker] Add fastsafetensors to NVIDIA Dockerfile

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Docker build fails on dev stage due to missing libnuma-dev bug ### Your current environment ### 🐛 Describe the bug ### Bug Description The Docker build process for the `dev` target fails on a clean environment. T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: v \ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency #38950 [Docker] Add fastsafetensors to NVIDIA Dockerfile Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: `fastsafetensors` Python package is missing from the base image. ### To Reproduce 1. Use the Dev Containers feature in VS Code / Cursor to build the environment from the `main` branch. 2. The target stage is `dev` in `d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency #38950 [Docker] Ad...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38950](https://github.com/vllm-project/vllm/pull/38950) | mentioned | 0.6 | [Docker] Add fastsafetensors to NVIDIA Dockerfile | se` Dockerfile stage as a runtime dependency for fastsafetensors (see #20384) ## Test plan - [ ] Build the NVIDIA Docker image and verify `fastsafetensors` is installed - [ ] Run… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
