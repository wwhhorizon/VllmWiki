# vllm-project/vllm#1685: Plans to make the installation work on Windows without WSL?

| 字段 | 值 |
| --- | --- |
| Issue | [#1685](https://github.com/vllm-project/vllm/issues/1685) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Plans to make the installation work on Windows without WSL?

### Issue 正文摘录

I get the following error during install: `No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\` Due to my company's policy we can't have WSL enabled on our GPU machine, are there any plans for making installs possible on Windows without WSL? Thank you,

## 现有链接修复摘要

#14891 [Kernel] vLLM Windows CUDA support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Plans to make the installation work on Windows without WSL? I get the following error during install: `No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\` Due to my comp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: k on Windows without WSL? I get the following error during install: `No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\` Due to my company's policy we can't have WSL ena...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#14891](https://github.com/vllm-project/vllm/pull/14891) | closes_keyword | 0.95 | [Kernel] vLLM Windows CUDA support | FIX #1685 FIX #179 FIX #2309 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
