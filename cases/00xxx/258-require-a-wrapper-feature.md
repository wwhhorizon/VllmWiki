# vllm-project/vllm#258: Require a "Wrapper" feature

| 字段 | 值 |
| --- | --- |
| Issue | [#258](https://github.com/vllm-project/vllm/issues/258) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Require a "Wrapper" feature

### Issue 正文摘录

It will be perfect to have a wrapper function to turn the model into the vllm-enhanced model. (like PEFT). It is useful if we have a lora model, we can "merge_and_unload" it with the base model, and then wrap it, or in the case that we need to pull from some specific model revision from HF.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: apper" feature It will be perfect to have a wrapper function to turn the model into the vllm-enhanced model. (like PEFT). It is useful if we have a lora model, we can "merge_and_unload" it with the base model, and then...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: odel, and then wrap it, or in the case that we need to pull from some specific model revision from HF.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
