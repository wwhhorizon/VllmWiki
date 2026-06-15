# vllm-project/vllm#2604: Build times too long since LoRA has been merged

| 字段 | 值 |
| --- | --- |
| Issue | [#2604](https://github.com/vllm-project/vllm/issues/2604) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Build times too long since LoRA has been merged

### Issue 正文摘录

Since we merged LoRA, the build times have gone up a lot. We should probably not build punica by default for developers and only do it for the final wheels. @Yard1 How much work would it be to do that?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Build times too long since LoRA has been merged Since we merged LoRA, the build times have gone up a lot. We should probably not build punica by default for developers and only do it for the final wheels. @Yard1 How muc

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
