# vllm-project/vllm#1884: How to register user-modified Model and Tokenizer?

| 字段 | 值 |
| --- | --- |
| Issue | [#1884](https://github.com/vllm-project/vllm/issues/1884) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to register user-modified Model and Tokenizer?

### Issue 正文摘录

Currently, our usage is restricted to models specified in the `model_executor/models` and `transformers` directories, along with a limited tokenizer. If we wish to make modifications to both the model and tokenizer, how can we register these changes without incorporating them into either vllm or transformers?

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: How to register user-modified Model and Tokenizer? feature request;stale Currently, our usage is restricted to models specified in the `model_executor/models` and `transformers` directories, along with a limited tokeniz...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r? feature request;stale Currently, our usage is restricted to models specified in the `model_executor/models` and `transformers` directories, along with a limited tokenizer. If we wish to make modifications to both the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How to register user-modified Model and Tokenizer? feature request;stale Currently, our usage is restricted to models specified in the `model_executor/models` and `transformers` directories, along with a limited tokeniz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
