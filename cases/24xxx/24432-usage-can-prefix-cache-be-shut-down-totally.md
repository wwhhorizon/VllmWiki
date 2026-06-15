# vllm-project/vllm#24432: [Usage]: Can prefix cache be shut down totally?

| 字段 | 值 |
| --- | --- |
| Issue | [#24432](https://github.com/vllm-project/vllm/issues/24432) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can prefix cache be shut down totally?

### Issue 正文摘录

I modified vllm to support my own model, but encounted a problem. If I send a request with image first time, it success. But I request again, the input image of preprocessor will be None, which will result in a bug. I set **enable_prefix_caching = False and no_enable_prefix_caching = True**, but not success. Can prefix cache be totally shut down?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Can prefix cache be shut down totally? usage;stale I modified vllm to support my own model, but encounted a problem. If I send a request with image first time, it success. But I request again, the input image o...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: Can prefix cache be shut down totally? usage;stale I modified vllm to support my own model, but encounted a problem. If I send a request with image first time, it success. But I request again, the input image o...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: be None, which will result in a bug. I set **enable_prefix_caching = False and no_enable_prefix_caching = True**, but not success. Can prefix cache be totally shut down?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ache be shut down totally? usage;stale I modified vllm to support my own model, but encounted a problem. If I send a request with image first time, it success. But I request again, the input image of preprocessor will b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
