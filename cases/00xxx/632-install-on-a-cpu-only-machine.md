# vllm-project/vllm#632: Install on a CPU-only machine.

| 字段 | 值 |
| --- | --- |
| Issue | [#632](https://github.com/vllm-project/vllm/issues/632) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> Install on a CPU-only machine.

### Issue 正文摘录

Is it possible to install vLLM on CPU-only(no CUDA) machine?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Install on a CPU-only machine. Is it possible to install vLLM on CPU-only(no CUDA) machine? development cuda Is it possible to install vLLM on CPU-only(no CUDA) machine?
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: all on a CPU-only machine. Is it possible to install vLLM on CPU-only(no CUDA) machine? development cuda Is it possible to install vLLM on CPU-only(no CUDA) machine?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
