# vllm-project/vllm#4260: [Feature]: Add argument terminators "eos_token_id" to serving models api_server.py

| 字段 | 值 |
| --- | --- |
| Issue | [#4260](https://github.com/vllm-project/vllm/issues/4260) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add argument terminators "eos_token_id" to serving models api_server.py

### Issue 正文摘录

### 🚀 The feature, motivation and pitch New models as LLama-3 use different end terminator, that are need to be specified. For example when using the API the client response return "me know if this is correct! assistant \n\nThat\'s correct! The output is", thats seems the roles are not well parsed. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Add argument terminators "eos_token_id" to serving models api_server.py feature request ### 🚀 The feature, motivation and pitch New models as LLama-3 use different end terminator, that are need to be specifie...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: w models as LLama-3 use different end terminator, that are need to be specified. For example when using the API the client response return "me know if this is correct! assistant \n\nThat\'s correct! The output is", that...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ument terminators "eos_token_id" to serving models api_server.py feature request ### 🚀 The feature, motivation and pitch New models as LLama-3 use different end terminator, that are need to be specified. For example whe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
