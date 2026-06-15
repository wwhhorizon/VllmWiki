# vllm-project/vllm#5605: [Feature]: Access to user information in scheduler

| 字段 | 值 |
| --- | --- |
| Issue | [#5605](https://github.com/vllm-project/vllm/issues/5605) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Access to user information in scheduler

### Issue 正文摘录

### 🚀 The feature, motivation and pitch To my knowledge, there is no user awareness in the core implementation of vLLM. However, in order to perform optimizations having the final user in mind, it would be very useful to be able to receive and use this information. I see that there is a parameter called _user_ in the openAI API, i.e. (line 353 of file vllm/entrypoints/openai/protocol.py), but this information is not transferred further to the core of vLLM. ```python class CompletionRequest(OpenAIBaseModel): [...] user: Optional[str] = None ``` Specifically, I am interested in creating scheduling policies based on the users, i.e., a scheduler that divides service fairly among multiple users. For that, it would be necessary to receive the user identifier in the scheduler. The scheduler only receives _SequenceGroup_ objects without user information in method _add_seq_group_ (line 320 of file vllm/core/scheduler.py). Is there any way to access this information through other ways? ### Alternatives _No response_ ### Additional context We have modified the code to add the user information in the call _add_seq_group_ of the scheduler, with all required changes to receive this information...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Access to user information in scheduler feature request;stale ### 🚀 The feature, motivation and pitch To my knowledge, there is no user awareness in the core implementation of vLLM. However, in order to perfo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Access to user information in scheduler feature request;stale ### 🚀 The feature, motivation and pitch To my knowledge, there is no user awareness in the core implementation of vLLM. However, in order to perfo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: uest(OpenAIBaseModel): [...] user: Optional[str] = None ``` Specifically, I am interested in creating scheduling policies based on the users, i.e., a scheduler that divides service fairly among multiple users. For that,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
