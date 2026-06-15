# vllm-project/vllm#293: Why use tensor parallelism when model can easily fit on a single GPU ?

| 字段 | 值 |
| --- | --- |
| Issue | [#293](https://github.com/vllm-project/vllm/issues/293) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why use tensor parallelism when model can easily fit on a single GPU ?

### Issue 正文摘录

If the model can fit on a single GPU, wouldn't it be better to use something like DDP instead? What are the advantages of using tensor parallelism if the model is small enough to fit on a single GPU ?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Why use tensor parallelism when model can easily fit on a single GPU ? If the model can fit on a single GPU, wouldn't it be better to use something like DDP instead? What are the advantages of using tensor parallelism i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Why use tensor parallelism when model can easily fit on a single GPU ? If the model can fit on a single GPU, wouldn't it be better to use something like DDP instead? What are the advantages of using tensor parallelism i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
