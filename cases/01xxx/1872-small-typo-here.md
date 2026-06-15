# vllm-project/vllm#1872: Small typo here.

| 字段 | 值 |
| --- | --- |
| Issue | [#1872](https://github.com/vllm-project/vllm/issues/1872) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Small typo here.

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/66785cc05c05c7f19f319533c23d1998b9d80bf9/vllm/sampling_params.py#L72 Special is not correct.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 66785cc05c05c7f19f319533c23d1998b9d80bf9/vllm/sampling_params.py#L72 Special is not correct.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Small typo here. https://github.com/vllm-project/vllm/blob/66785cc05c05c7f19f319533c23d1998b9d80bf9/vllm/sampling_params.py#L72 Special is not correct.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
