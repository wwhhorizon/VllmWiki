# vllm-project/vllm#752: Pipeline parallelism support

| 字段 | 值 |
| --- | --- |
| Issue | [#752](https://github.com/vllm-project/vllm/issues/752) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Pipeline parallelism support

### Issue 正文摘录

Dear vllm team, Congratulations on your acceptance to SOSP! I would like to contribute to the project and found the pipeline parallelism feature in the roadmap. I am curious whether pipeline parallelism is currently developing inside the team internally or is planned. If not, do you guys have any specific directions you planned initially? (I found some comments by Zhuohan about creating new weights for pipeline parallelism)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ide the team internally or is planned. If not, do you guys have any specific directions you planned initially? (I found some comments by Zhuohan about creating new weights for pipeline parallelism)
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Pipeline parallelism support Dear vllm team, Congratulations on your acceptance to SOSP! I would like to contribute to the project and found the pipeline parallelism feature in the roadmap. I am curious whether pipeline...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
