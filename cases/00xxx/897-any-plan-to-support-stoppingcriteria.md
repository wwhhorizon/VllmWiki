# vllm-project/vllm#897: Any plan to support StoppingCriteria

| 字段 | 值 |
| --- | --- |
| Issue | [#897](https://github.com/vllm-project/vllm/issues/897) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Any plan to support StoppingCriteria

### Issue 正文摘录

Thanks for your great work first! For models of text generation tasks, early stopping is very important, which can save computational resources. Like the StoppingCriteria from transformers, it is more flexible than a simple stopping list, and can be used to customize the termination strategy. Do you have any plans for this? Looking forward to your reply.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: work first! For models of text generation tasks, early stopping is very important, which can save computational resources. Like the StoppingCriteria from transformers, it is more flexible than a simple stopping list, an...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: y plan to support StoppingCriteria Thanks for your great work first! For models of text generation tasks, early stopping is very important, which can save computational resources. Like the StoppingCriteria from transfor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
