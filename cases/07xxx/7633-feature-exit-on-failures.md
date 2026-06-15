# vllm-project/vllm#7633: [Feature]: Exit on failures

| 字段 | 值 |
| --- | --- |
| Issue | [#7633](https://github.com/vllm-project/vllm/issues/7633) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Exit on failures

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Commonly vllm will crash/fail at server/engine level, so no more requests can be made. However, while in some cases the entire server stops and (say in docker) one can auto restart to catch such rare failures, many times the failures leave the server in a mixed state and one cannot easily know if the server is healthy. Sometimes even the health API says it's healthy, when it's not. ### Alternatives per-user crafted solutions to restart the server by detection of API behavior. ### Additional context Example case when left in ambiguous state when can't reach /v1 but server not shutdown: https://github.com/vllm-project/vllm/issues/7632

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: made. However, while in some cases the entire server stops and (say in docker) one can auto restart to catch such rare failures, many times the failures leave the server in a mixed state and one cannot easily know if th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Exit on failures feature request ### 🚀 The feature, motivation and pitch Commonly vllm will crash/fail at server/engine level, so no more requests can be made. However, while in some cases the entire server s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
