# vllm-project/vllm#7318: [Usage]: Can we get count for current processing tokens from openai api?

| 字段 | 值 |
| --- | --- |
| Issue | [#7318](https://github.com/vllm-project/vllm/issues/7318) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can we get count for current processing tokens from openai api?

### Issue 正文摘录

### Your current environment Before I added the Enable_prefix_caching=True parameter, I needed to count tokens in order to process requests and not go beyond the maximum number of model tokens (8192), I counted the number of tokens per user and created a queue if there was no free space in the process, now with I don’t know how to implement this with the Enable_prefix_caching parameter.. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ]: Can we get count for current processing tokens from openai api? usage;stale ### Your current environment Before I added the Enable_prefix_caching=True parameter, I needed to count tokens in order to process requests...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: .. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ens in order to process requests and not go beyond the maximum number of model tokens (8192), I counted the number of tokens per user and created a queue if there was no free space in the process, now with I don’t know...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
