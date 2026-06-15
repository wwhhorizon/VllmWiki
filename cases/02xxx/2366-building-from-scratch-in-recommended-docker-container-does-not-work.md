# vllm-project/vllm#2366: Building from scratch in recommended Docker container does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#2366](https://github.com/vllm-project/vllm/issues/2366) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Building from scratch in recommended Docker container does not work

### Issue 正文摘录

FYI the [recommended path](https://docs.vllm.ai/en/latest/getting_started/installation.html#build-from-source) to install from source (using the following container: `nvcr.io/nvidia/pytorch:23.10-py3`) is failing. I managed to get it built with `nvidia/cuda:12.1.0-base-ubuntu22.04` instead (after installing `python3-dev` in the container). Additionally, I am not working on the CUDA kernels. Is there a pre-build development container anywhere which has `vllm` installed in editable mode without needing to compile all the kernels? This might make the dev experience better for those working just with python / torch

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Building from scratch in recommended Docker container does not work FYI the [recommended path](https://docs.vllm.ai/en/latest/getting_started/installation.html#build-from-source) to install from source (using the followi
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: a/pytorch:23.10-py3`) is failing. I managed to get it built with `nvidia/cuda:12.1.0-base-ubuntu22.04` instead (after installing `python3-dev` in the container). Additionally, I am not working on the CUDA kernels. Is th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ainer does not work FYI the [recommended path](https://docs.vllm.ai/en/latest/getting_started/installation.html#build-from-source) to install from source (using the following container: `nvcr.io/nvidia/pytorch:23.10-py3...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
