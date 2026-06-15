# vllm-project/vllm#3126: Conda Forge Package

| 字段 | 值 |
| --- | --- |
| Issue | [#3126](https://github.com/vllm-project/vllm/issues/3126) |
| 状态 | closed |
| 标签 | keep-open |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Conda Forge Package

### Issue 正文摘录

Any plans to release vllm via conda-forge? It's generally much easier to manage CUDA versions, etc. with conda. Happy to take a stab at a feedstock if there's interest but would prefer if one of the project owners could be a maintainer.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: release vllm via conda-forge? It's generally much easier to manage CUDA versions, etc. with conda. Happy to take a stab at a feedstock if there's interest but would prefer if one of the project owners could be a maintai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns to release vllm via conda-forge? It's generally much easier to manage CUDA versions, etc. with conda. Happy to take a stab at a feedstock if there's interest but would prefer if one of the project owners could be a m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
