# vllm-project/vllm#2242: Windows prebuilt wheels

| 字段 | 值 |
| --- | --- |
| Issue | [#2242](https://github.com/vllm-project/vllm/issues/2242) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> Windows prebuilt wheels

### Issue 正文摘录

Hi there, I want to know if you can build some windows wheels with cuda 12.1?

## 现有链接修复摘要

#14891 [Kernel] vLLM Windows CUDA support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Windows prebuilt wheels Hi there, I want to know if you can build some windows wheels with cuda 12.1? development ci_build cuda build_error #14891 [Kernel] vLLM Windows CUDA support Hi there,
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: eels Hi there, I want to know if you can build some windows wheels with cuda 12.1? development ci_build cuda build_error #14891 [Kernel] vLLM Windows CUDA support Hi there,

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#14891](https://github.com/vllm-project/vllm/pull/14891) | closes_keyword | 0.95 | [Kernel] vLLM Windows CUDA support | FIX #2242 FIX #669 FIX #5086 FIX #5631 FIX #1685 FIX #179 FIX #2309 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
