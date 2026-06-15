# vllm-project/vllm#1441: Does vllm support the Mac/Metal/MPS? 

| 字段 | 值 |
| --- | --- |
| Issue | [#1441](https://github.com/vllm-project/vllm/issues/1441) |
| 状态 | closed |
| 标签 |  |
| 评论 | 115; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Does vllm support the Mac/Metal/MPS? 

### Issue 正文摘录

I ran into the error when pip install vllm in Mac: RuntimeError: Cannot find CUDA_HOME. CUDA must be available to build the package.

## 现有链接修复摘要

#36522 [Docs] Add Apple MPS (Metal) GPU installation guide | #36523 [Platform] Add MPS (Apple Metal) platform support for macOS

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Does vllm support the Mac/Metal/MPS? I ran into the error when pip install vllm in Mac: RuntimeError: Cannot find CUDA_HOME. CUDA must be available to build the package. development ci_build cuda build_error #36522 [Doc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: o the error when pip install vllm in Mac: RuntimeError: Cannot find CUDA_HOME. CUDA must be available to build the package. development ci_build cuda build_error #36522 [Docs] Add Apple MPS (Metal) GPU installation guid...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36522](https://github.com/vllm-project/vllm/pull/36522) | closes_keyword | 0.95 | [Docs] Add Apple MPS (Metal) GPU installation guide | resolves ## Related - vLLM #1441 — Feature request for Apple Silicon support (86 reactions) - robtaylor/vllm `mps-platform-support` branch — Implementation - huggingface/kernels |
| [#36523](https://github.com/vllm-project/vllm/pull/36523) | mentioned | 0.6 | [Platform] Add MPS (Apple Metal) platform support for macOS | ids it) - [ ] Verify docs render correctly with mkdocs ## Related - #1441 — Feature request: Apple Silicon support (86 reactions) - huggingface/kernels#308 — Metal kernel builder… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
