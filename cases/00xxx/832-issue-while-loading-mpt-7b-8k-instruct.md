# vllm-project/vllm#832: Issue while loading MPT-7B-8K-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#832](https://github.com/vllm-project/vllm/issues/832) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issue while loading MPT-7B-8K-instruct

### Issue 正文摘录

Newbie Question: I thought support for all MPT models is enabled by default, but when I try to load 8K variant of the MPT-7B model. I'm running into the following error while instantiation: ``` ValueError: Invalid shape for attention bias: torch.Size([32, 10, 10]) (expected (1, 32, 10, 10)) query.shape: torch.Size([1, 10, 32, 128]) key.shape : torch.Size([1, 10, 32, 128]) value.shape: torch.Size([1, 10, 32, 128]) ``` Can someone help/ guide me on this issue?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g MPT-7B-8K-instruct bug Newbie Question: I thought support for all MPT models is enabled by default, but when I try to load 8K variant of the MPT-7B model. I'm running into the following error while instantiation: ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
