# vllm-project/vllm#5609: [Feature]: Initial LLM token

| 字段 | 值 |
| --- | --- |
| Issue | [#5609](https://github.com/vllm-project/vllm/issues/5609) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Initial LLM token

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Not sure that this has been implemented but could add in initial tokens (i.e. text) to the beginning of the generation process be possible. So basically having the first few tokens be "Sure Thing!", for example, then the model continues generating tokens from that point on. ### Alternatives _No response_ ### Additional context This is in effort to have more control of the model output for returning certain formats and to reduce randomness in the responses.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ally having the first few tokens be "Sure Thing!", for example, then the model continues generating tokens from that point on. ### Alternatives _No response_ ### Additional context This is in effort to have more control...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Initial LLM token feature request;stale ### 🚀 The feature, motivation and pitch Not sure that this has been implemented but could add in initial tokens (i.e. text) to the beginning of the generation process b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
