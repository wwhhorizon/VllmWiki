# vllm-project/vllm#6165: [Feature]: Return hidden states (in progress?)

| 字段 | 值 |
| --- | --- |
| Issue | [#6165](https://github.com/vllm-project/vllm/issues/6165) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Return hidden states (in progress?)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I know this feature request sort of already exists: https://github.com/vllm-project/vllm/issues/5950 (and older, semi related requests) https://github.com/vllm-project/vllm/issues/3594 https://github.com/vllm-project/vllm/issues/1857 This is a similar pitch but I am creating a new issue as I noticed newer developments in the codebase. The pitch is to support returning hidden states when generating sequences. This enables many potential behaviors such as output classification, guardrails, etc. Whereas #5950 suggested a different step for embedding, I would suggest building it in as an option to EngineArgs or as an option that can be passed in with each generation request. I see that in `v0.5.1` there is already some new code in `ModelDriverBase` to support `return_hidden_states`. However, I don't see that supported yet in the LLM engine yet (not an input to `EngineArgs`). Basically, it seems like this feature is under development. I am mainly wondering what the timeline is for that? And what is the approach being taken so that I and the community can develop accordingly? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Return hidden states (in progress?) feature request;unstale ### 🚀 The feature, motivation and pitch I know this feature request sort of already exists: https://github.com/vllm-project/vllm/issues/5950 (and ol...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Whereas #5950 suggested a different step for embedding, I would suggest building it in as an option to EngineArgs or as an option that can be passed in with each generation request. I see that in `v0.5.1` there is alrea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ion request. I see that in `v0.5.1` there is already some new code in `ModelDriverBase` to support `return_hidden_states`. However, I don't see that supported yet in the LLM engine yet (not an input to `EngineArgs`). Ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
