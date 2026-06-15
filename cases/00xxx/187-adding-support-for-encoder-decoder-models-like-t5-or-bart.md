# vllm-project/vllm#187: Adding support for encoder-decoder models, like T5 or BART

| 字段 | 值 |
| --- | --- |
| Issue | [#187](https://github.com/vllm-project/vllm/issues/187) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 33; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Adding support for encoder-decoder models, like T5 or BART

### Issue 正文摘录

Will there be added support for encoder-decoder models, like T5 or BART? All of the currently supported models are decoder-only.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Adding support for encoder-decoder models, like T5 or BART new-model Will there be added support for encoder-decoder models, like T5 or BART? All of the currently supported models are decoder-only.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Adding support for encoder-decoder models, like T5 or BART new-model Will there be added support for encoder-decoder models, like T5 or BART? All of the currently supported models are decoder-only.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
