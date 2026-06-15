# vllm-project/vllm#1225: Installation Error

| 字段 | 值 |
| --- | --- |
| Issue | [#1225](https://github.com/vllm-project/vllm/issues/1225) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Installation Error

### Issue 正文摘录

When I install vLLM, I have pull the docker as the tutorial and install from source. But there are an error encountered, how can I fix this: `ValueError: Unsupported CUDA arch (5.2). Valid CUDA arch strings are: ['7.0', '7.5', '8.0', '8.6', '8.9', '9.0', '7.0+PTX', '7.5+PTX', '8.0+PTX', '8.6+PTX', '8.9+PTX', '9.0+PTX'].`

## 现有链接修复摘要

#1239 Fix error message on `TORCH_CUDA_ARCH_LIST`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Installation Error bug When I install vLLM, I have pull the docker as the tutorial and install from source. But there are an error encountered, how can I fix this: `ValueError: Unsupported CUDA arch (5.2). Valid CUDA arc
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e are an error encountered, how can I fix this: `ValueError: Unsupported CUDA arch (5.2). Valid CUDA arch strings are: ['7.0', '7.5', '8.0', '8.6', '8.9', '9.0', '7.0+PTX', '7.5+PTX', '8.0+PTX', '8.6+PTX', '8.9+PTX', '9...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#1239](https://github.com/vllm-project/vllm/pull/1239) | closes_keyword | 0.95 | Fix error message on `TORCH_CUDA_ARCH_LIST` | Fixes #1225 This PR fixes the error message when the `TORCH_CUDA_ARCH_LIST` includes an unsupported CUDA architecture. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
