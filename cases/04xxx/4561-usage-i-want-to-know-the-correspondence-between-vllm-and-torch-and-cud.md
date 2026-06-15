# vllm-project/vllm#4561: [Usage]:   I want to know the correspondence between vllm and torch and cuda

| 字段 | 值 |
| --- | --- |
| Issue | [#4561](https://github.com/vllm-project/vllm/issues/4561) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:   I want to know the correspondence between vllm and torch and cuda

### Issue 正文摘录

For example, my current torch version must be 1.13.1. What version of vllm should I install before I can use it?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ence between vllm and torch and cuda usage For example, my current torch version must be 1.13.1. What version of vllm should I install before I can use it? development cuda env_dependency For example, my current torch v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: I want to know the correspondence between vllm and torch and cuda usage For example, my current torch version must be 1.13.1. What version of vllm should I install before I can use it? development cuda env_depe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
