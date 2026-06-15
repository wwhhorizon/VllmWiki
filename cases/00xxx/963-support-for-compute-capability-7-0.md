# vllm-project/vllm#963: Support for compute capability <7.0

| 字段 | 值 |
| --- | --- |
| Issue | [#963](https://github.com/vllm-project/vllm/issues/963) |
| 状态 | closed |
| 标签 |  |
| 评论 | 30; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support for compute capability <7.0

### Issue 正文摘录

Hi, How tightly coupled is the requirement for compute capability of 7.0 or higher? Is it possible to disable some features, and run on e.g. 6.0? Like a P100 Maybe this is totally unfeasible, but I am limited in my GPU options.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Support for compute capability <7.0 Hi, How tightly coupled is the requirement for compute capability of 7.0 or higher? Is it possible to disable some features, and run on e.g. 6.0? Like a P100 Maybe this is totally unf...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
