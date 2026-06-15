# vllm-project/vllm#1842: Are Cache Events needed?

| 字段 | 值 |
| --- | --- |
| Issue | [#1842](https://github.com/vllm-project/vllm/issues/1842) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Are Cache Events needed?

### Issue 正文摘录

was wondering whether cache events were actually needed, it seems that the operations are done on the same stream so everything will run in a synchronous fashion anyway, not sure what `event.wait()` serves exactly unless I'm missing something. https://github.com/vllm-project/vllm/blob/a7b3e33078469943d2a11b1c3d634e220b71bf76/vllm/worker/cache_engine.py#L51 https://github.com/vllm-project/vllm/blob/a7b3e33078469943d2a11b1c3d634e220b71bf76/vllm/model_executor/layers/attention.py#L263

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/a7b3e33078469943d2a11b1c3d634e220b71bf76/vllm/model_executor/layers/attention.py#L263

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
