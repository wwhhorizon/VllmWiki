# vllm-project/vllm#7542: [Feature]: Try Catch

| 字段 | 值 |
| --- | --- |
| Issue | [#7542](https://github.com/vllm-project/vllm/issues/7542) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Try Catch

### Issue 正文摘录

### 🚀 The feature, motivation and pitch 数据量大了，可能就会有一些损坏数据，尽管输入之前可以先调用一遍processor，来检查数据，但是这样效率太低了。但是vllm启动的server每次遇到错误，服务都会直接挂断，可不可以支持一下异常处理呀... ![image](https://github.com/user-attachments/assets/e9c43310-1f98-45b4-b09f-521242017a98) ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Try Catch feature request;stale ### 🚀 The feature, motivation and pitch 数据量大了，可能就会有一些损坏数据，尽管输入之前可以先调用一遍processor，来检查数据，但是这样效率太低了。但是vllm启动的server每次遇到错误，服务都会直接挂断，可不可以支持一下异常处理呀... ![image](https://github.com/use...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
