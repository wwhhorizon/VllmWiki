# vllm-project/vllm#7792: [New Model]: Snowflake Arctic Embed  (Family)

| 字段 | 值 |
| --- | --- |
| Issue | [#7792](https://github.com/vllm-project/vllm/issues/7792) |
| 状态 | closed |
| 标签 | new-model;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Snowflake Arctic Embed  (Family)

### Issue 正文摘录

### The model to consider The Snowflake arctic embed family of embeddings models - a very small but performant-for-size series of embedding models. https://huggingface.co/Snowflake/snowflake-arctic-embed-xs https://huggingface.co/Snowflake/snowflake-arctic-embed-s https://huggingface.co/Snowflake/snowflake-arctic-embed-m https://huggingface.co/Snowflake/snowflake-arctic-embed-m-long https://huggingface.co/Snowflake/snowflake-arctic-embed-l ### The closest model vllm already supports. Closest supported embedding model: https://huggingface.co/intfloat/e5-mistral-7b-instruct Closest model by family: https://huggingface.co/Snowflake/snowflake-arctic-instruct ### What's your difficulty of supporting the model you want? Only mistral embeddings are supported at this time.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Snowflake Arctic Embed (Family) new-model;unstale ### The model to consider The Snowflake arctic embed family of embeddings models - a very small but performant-for-size series of embedding models. https://...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: onsider The Snowflake arctic embed family of embeddings models - a very small but performant-for-size series of embedding models. https://huggingface.co/Snowflake/snowflake-arctic-embed-xs https://huggingface.co/Snowfla...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Snowflake Arctic Embed (Family) new-model;unstale ### The model to consider The Snowflake arctic embed family of embeddings models - a very small but performant-for-size series of embedding models. https://...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
