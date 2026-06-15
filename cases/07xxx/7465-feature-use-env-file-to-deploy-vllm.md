# vllm-project/vllm#7465: [Feature]: Use .env file to deploy vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#7465](https://github.com/vllm-project/vllm/issues/7465) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Use .env file to deploy vllm

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It would be helpful if vllm could use a .env file and respect this priority : default values < .env file < env values < CLI I can implement it if anyone is interested. ### Alternatives _No response_ ### Additional context Related to [#7350](https://github.com/vllm-project/vllm/issues/7350)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Use .env file to deploy vllm feature request ### 🚀 The feature, motivation and pitch It would be helpful if vllm could use a .env file and respect this priority : default values < .env file < env values < CLI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
