# vllm-project/vllm#1367: cannot import name 'activation_ops' from 'vllm'

| 字段 | 值 |
| --- | --- |
| Issue | [#1367](https://github.com/vllm-project/vllm/issues/1367) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> cannot import name 'activation_ops' from 'vllm'

### Issue 正文摘录

We discovered some issues while experimenting with the framework. Some packages are missing in the vllm directory： 1. ImportError: cannot import name 'cuda_utils' from partially initialized module 'vllm' (most likely due to a circular import) 2. ImportError: cannot import name 'activation_ops' from 'vllm' Our run command is：python3 -m vllm.entrypoints.api_server

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: cannot import name 'activation_ops' from 'vllm' We discovered some issues while experimenting with the framework. Some packages are missing in the vllm directory： 1. ImportError: cannot import name 'cuda_utils' from par...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: are missing in the vllm directory： 1. ImportError: cannot import name 'cuda_utils' from partially initialized module 'vllm' (most likely due to a circular import) 2. ImportError: cannot import name 'activation_ops' from...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
