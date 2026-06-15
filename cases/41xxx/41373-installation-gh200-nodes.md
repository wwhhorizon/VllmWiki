# vllm-project/vllm#41373: [Installation]: GH200 nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#41373](https://github.com/vllm-project/vllm/issues/41373) |
| 状态 | open |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: GH200 nodes

### Issue 正文摘录

### Your current environment Hi all, I am attempting to install vllm on the Jupiter supercomputing system: https://www.fz-juelich.de/en The system consists of 4xGH200 nodes and only supports CUDA 13.1 for loading modules. Compute nodes do not have access to the internet. Vllm fails to install in the created environment. I am not sure whether the ARM systems with CUDA 13.1 are currently supported. Is it required to build vllm from source? Any help would be greatly appreciated. Thank you, Enrico ### How you are installing vllm ```sh uv pip install vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: GH200 nodes installation ### Your current environment Hi all, I am attempting to install vllm on the Jupiter supercomputing system: https://www.fz-juelich.de/en The system consists of 4xGH200 nodes and
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: fz-juelich.de/en The system consists of 4xGH200 nodes and only supports CUDA 13.1 for loading modules. Compute nodes do not have access to the internet. Vllm fails to install in the created environment. I am not sure wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
