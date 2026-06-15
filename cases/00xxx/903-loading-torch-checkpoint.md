# vllm-project/vllm#903: Loading torch checkpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#903](https://github.com/vllm-project/vllm/issues/903) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Loading torch checkpoint

### Issue 正文摘录

Hi, Is there a simpler way to directly load a torch saved checkpoint in vllm? (chkpt.pth.tar format)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: er way to directly load a torch saved checkpoint in vllm? (chkpt.pth.tar format)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
