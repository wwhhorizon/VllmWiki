# vllm-project/vllm#2232: The same model cannot be loaded by two different users

| 字段 | 值 |
| --- | --- |
| Issue | [#2232](https://github.com/vllm-project/vllm/issues/2232) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The same model cannot be loaded by two different users

### Issue 正文摘录

As pointed out here, the way lockfiles are created prevents the second user from loading any models that a previous user has loaded at any point: https://github.com/vllm-project/vllm/issues/2179 This is still an issue with the only workaround being to force-delete the lockfile created by another user.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: The same model cannot be loaded by two different users As pointed out here, the way lockfiles are created prevents the second user from loading any models that a previous user has loaded at any point: https://github.com...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
