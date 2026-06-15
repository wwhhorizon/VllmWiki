# vllm-project/vllm#1899: Remove Yi

| 字段 | 值 |
| --- | --- |
| Issue | [#1899](https://github.com/vllm-project/vllm/issues/1899) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Remove Yi

### Issue 正文摘录

On Nov. 21st, the Yi authors changed their code/config files to be compatible with LLaMA ([ref](https://huggingface.co/01-ai/Yi-34B-200K/commit/00313b6183023bd3a3da86fecb36d966bfc14132)). Therefore, we can _slowly_ remove the model and config code for Yi. While this breaks the compatibility for the users who downloaded the model before Nov. 21st, I think this is acceptable.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Remove Yi On Nov. 21st, the Yi authors changed their code/config files to be compatible with LLaMA ([ref](https://huggingface.co/01-ai/Yi-34B-200K/commit/00313b6183023bd3a3da86fecb36d966bfc14132)). Therefore, we can _sl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
