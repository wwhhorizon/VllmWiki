# vllm-project/vllm#2220: Issue with obtaining logits.

| 字段 | 值 |
| --- | --- |
| Issue | [#2220](https://github.com/vllm-project/vllm/issues/2220) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issue with obtaining logits.

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/56470984/f150d087-a874-48a1-acbc-c7d24537d1f9) I used the CodeLlama model with the given prompt, but when obtaining the logits, the shape is torch.Size([32016]). Shouldn't it be torch.Size([4, 32016])?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lm/assets/56470984/f150d087-a874-48a1-acbc-c7d24537d1f9) I used the CodeLlama model with the given prompt, but when obtaining the logits, the shape is torch.Size([32016]). Shouldn't it be torch.Size([4, 32016])?

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
