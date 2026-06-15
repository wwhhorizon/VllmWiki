# vllm-project/vllm#1948: Remove "cuda" and use xpu abstraction

| 字段 | 值 |
| --- | --- |
| Issue | [#1948](https://github.com/vllm-project/vllm/issues/1948) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Remove "cuda" and use xpu abstraction

### Issue 正文摘录

Currently, vLLM has many `cuda`s throughout its codebase. This is only compatible with NVIDAI/AMD/Intel GPUs, and not with other accelerators. A more general abstraction (like xpu in DeepSpeed) is required to support more diverse hardware.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Remove "cuda" and use xpu abstraction Currently, vLLM has many `cuda`s throughout its codebase. This is only compatible with NVIDAI/AMD/Intel GPUs, and not with other accelerators. A more general abstraction (like xpu i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
