# vllm-project/vllm#1969: Proposal: pre-commit instead of format.sh

| 字段 | 值 |
| --- | --- |
| Issue | [#1969](https://github.com/vllm-project/vllm/issues/1969) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Proposal: pre-commit instead of format.sh

### Issue 正文摘录

It seems that tools called in `./format.sh` could be easily configured to be call by pre-commit by adding them to the file `/.pre-commit-config.yaml`. Once we do this, every time, contributors run `git commit`, they could run these tool with the **new content**, which shouldn't take much time. Also, we could create a GitHub action to run `pre-commit run --all-files` to check the consistent project style. Is this a good idea? Thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Proposal: pre-commit instead of format.sh It seems that tools called in `./format.sh` could be easily configured to be call by pre-commit by adding them to the file `/.pre-commit-config.yaml`. Once we do this, every tim...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
