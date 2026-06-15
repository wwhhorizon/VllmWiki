# vllm-project/vllm#408: feature request: Support user-defined conversation template

| 字段 | 值 |
| --- | --- |
| Issue | [#408](https://github.com/vllm-project/vllm/issues/408) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> feature request: Support user-defined conversation template

### Issue 正文摘录

We need to change the conversation template when we use our fine-tuned MPT 30b model. https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/api_server.py#L66 I think this feature is important especially when we use vLLM in production (with fine-tuned models).

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /main/vllm/entrypoints/openai/api_server.py#L66 I think this feature is important especially when we use vLLM in production (with fine-tuned models).
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d to change the conversation template when we use our fine-tuned MPT 30b model. https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/api_server.py#L66 I think this feature is important especially when...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: feature request: Support user-defined conversation template feature request We need to change the conversation template when we use our fine-tuned MPT 30b model. https://github.com/vllm-project/vllm/blob/main/vllm/entry...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
