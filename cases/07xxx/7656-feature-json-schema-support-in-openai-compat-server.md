# vllm-project/vllm#7656: [Feature]: json_schema support in OpenAI compat server

| 字段 | 值 |
| --- | --- |
| Issue | [#7656](https://github.com/vllm-project/vllm/issues/7656) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: json_schema support in OpenAI compat server

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It would be great now that OpenAI supports JSONSchema to be able to support the `repsonse_format.type == 'json_schema'` in vLLM to make it easy to switch between the two formats. ### Alternatives _No response_ ### Additional context https://platform.openai.com/docs/guides/structured-outputs/

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: now that OpenAI supports JSONSchema to be able to support the `repsonse_format.type == 'json_schema'` in vLLM to make it easy to switch between the two formats. ### Alternatives _No response_ ### Additional context http...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: json_schema support in OpenAI compat server feature request ### 🚀 The feature, motivation and pitch It would be great now that OpenAI supports JSONSchema to be able to support the `repsonse_format.type == 'js...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
