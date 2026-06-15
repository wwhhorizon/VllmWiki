# vllm-project/vllm#7671: [Bug]: Streaming API: Abort functionality not working as expected

| 字段 | 值 |
| --- | --- |
| Issue | [#7671](https://github.com/vllm-project/vllm/issues/7671) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Streaming API: Abort functionality not working as expected

### Issue 正文摘录

### 🐛 Describe the bug im encountering an issue with the abort functionality when using streaming from the openai api. here are the details: abort requests are not working when streaming is enabled. even pending requests do not get aborted. i've added extensive logging, but the abort functionality still fails. expected behavior: abort requests should work regardless of whether streaming is on or off. current behavior: with streaming off: abort functionality works perfectly fine. with streaming on: abort requests fail to terminate the operation. additional information: i've observed code for aborts with its own finish reason. this code appears to be in place but is not effective when streaming is enabled. is this a known issue with the streaming api? thank you. any assistance or insight would be greatly appreciated.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: reaming api? thank you. any assistance or insight would be greatly appreciated.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: eaming on: abort requests fail to terminate the operation. additional information: i've observed code for aborts with its own finish reason. this code appears to be in place but is not effective when streaming is enable...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: y when using streaming from the openai api. here are the details: abort requests are not working when streaming is enabled. even pending requests do not get aborted. i've added extensive logging, but the abort functiona...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
