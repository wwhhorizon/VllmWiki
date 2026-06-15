# vllm-project/vllm#12964: [Installation]: install from source stuck for a long time

| 字段 | 值 |
| --- | --- |
| Issue | [#12964](https://github.com/vllm-project/vllm/issues/12964) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: install from source stuck for a long time

### Issue 正文摘录

### Your current environment Dockerfile ```text # Use NVIDIA PyTorch as base image FROM nvcr.io/nvidia/pytorch:23.10-py3 # Install system dependencies RUN apt-get update && apt-get install -y \ git \ && rm -rf /var/lib/apt/lists/* ENV MAX_JOBS=6 # Clone and install vLLM RUN git clone https://github.com/vllm-project/vllm.git && \ cd vllm && \ pip install -e .``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: install from source stuck for a long time installation ### Your current environment Dockerfile ```text # Use NVIDIA PyTorch as base image FROM nvcr.io/nvidia/pytorch:23.10-py3 # Install system dependenci
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
