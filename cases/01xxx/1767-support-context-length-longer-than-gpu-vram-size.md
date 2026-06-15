# vllm-project/vllm#1767: Support context length longer than GPU VRAM size

| 字段 | 值 |
| --- | --- |
| Issue | [#1767](https://github.com/vllm-project/vllm/issues/1767) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support context length longer than GPU VRAM size

### Issue 正文摘录

Is there any plan in progress to support very long context length model? If there isn't, may I know is there any approaches that I could help implement to extend the use of longer context length? E.g. Yi-34B model has 200k context length. However, due to insufficient VRAM per GPU e.g. 80GB, I can only deploy the model with context length of approximately 40k only.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ength? E.g. Yi-34B model has 200k context length. However, due to insufficient VRAM per GPU e.g. 80GB, I can only deploy the model with context length of approximately 40k only.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: M size Is there any plan in progress to support very long context length model? If there isn't, may I know is there any approaches that I could help implement to extend the use of longer context length? E.g. Yi-34B mode...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
