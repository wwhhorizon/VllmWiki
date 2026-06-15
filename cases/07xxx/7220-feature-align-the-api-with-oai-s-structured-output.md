# vllm-project/vllm#7220: [Feature]: Align the API with OAI's structured output

| 字段 | 值 |
| --- | --- |
| Issue | [#7220](https://github.com/vllm-project/vllm/issues/7220) |
| 状态 | closed |
| 标签 | feature request;structured-output;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Align the API with OAI's structured output

### Issue 正文摘录

### 🚀 The feature, motivation and pitch OpenAI API introduced a feature that supports structured output, this is basically the same as our `guided_json` feature. 1. We should simply alias it to support this feature 🌟 2. we might want to consider implementing this also for tools 3. Implement `refusal` ### Alternatives _No response_ ### Additional context https://openai.com/index/introducing-structured-outputs-in-the-api/

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Align the API with OAI's structured output feature request;structured-output;stale ### 🚀 The feature, motivation and pitch OpenAI API introduced a feature that supports structured output, this is basically th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _No response_ ### Additional context https://openai.com/index/introducing-structured-outputs-in-the-api/

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
