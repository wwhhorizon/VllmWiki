# vllm-project/vllm#6432: [Bug]: autogen can't work with vllm v0.5.1

| 字段 | 值 |
| --- | --- |
| Issue | [#6432](https://github.com/vllm-project/vllm/issues/6432) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: autogen can't work with vllm v0.5.1

### Issue 正文摘录

### Your current environment Can't provide it as I don't have access to vllm server side, and I believe it is not related to this bug. ### 🐛 Describe the bug Looks like from vllm v0.5.0, vllm starts to support a new feature "OpenAI tools support named functions". After that, every message returned by vllm includes an empty "tools_call" list if user prompt doesn't intend to call a tool. This empty "tools_call" list leads autogen to misbehavior. Details please see https://github.com/microsoft/autogen/issues/3120 @marklysze

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: autogen can't work with vllm v0.5.1 bug;stale ### Your current environment Can't provide it as I don't have access to vllm server side, and I believe it is not related to this bug. ### 🐛 Describe the bug Looks li...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
