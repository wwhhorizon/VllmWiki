# vllm-project/vllm#447: scheduler max-length

| 字段 | 值 |
| --- | --- |
| Issue | [#447](https://github.com/vllm-project/vllm/issues/447) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> scheduler max-length

### Issue 正文摘录

I am running mpt-7b-instruct which should support "arbitrary long contexts". However when I provide the model long inputs I get this warning (and the model does not produce any output): ``` Token indices sequence length is longer than the specified maximum sequence length for this model (3622 > 2048). Running this sequence through the model will result in indexing errors WARNING 07-12 15:03:35 scheduler.py:194] Input prompt (3622 tokens) is too long and exceeds limit of 2560 ``` What is this scheduler limit? My understanding is that it is not related to the model. How can I change it?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ce any output): ``` Token indices sequence length is longer than the specified maximum sequence length for this model (3622 > 2048). Running this sequence through the model will result in indexing errors WARNING 07-12 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ich should support "arbitrary long contexts". However when I provide the model long inputs I get this warning (and the model does not produce any output): ``` Token indices sequence length is longer than the specified m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: scheduler max-length bug I am running mpt-7b-instruct which should support "arbitrary long contexts". However when I provide the model long inputs I get this warning (and the model does not produce any output): ``` Tok

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
