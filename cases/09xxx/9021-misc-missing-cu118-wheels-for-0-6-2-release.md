# vllm-project/vllm#9021: [Misc]: Missing cu118 wheels for 0.6.2 release

| 字段 | 值 |
| --- | --- |
| Issue | [#9021](https://github.com/vllm-project/vllm/issues/9021) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Missing cu118 wheels for 0.6.2 release

### Issue 正文摘录

Hello, For version 0.6.2, the cu118 wheels are not available on the release page: [0.6.2 release page](https://github.com/vllm-project/vllm/releases/tag/v0.6.2) While 0.6.1.post2 has them: [0.6.1.post2 release page](https://github.com/vllm-project/vllm/releases/tag/v0.6.1.post2) Are you planning on continuing to release those wheels or should we start building vllm+cu118 from source?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Misc]: Missing cu118 wheels for 0.6.2 release stale Hello, For version 0.6.2, the cu118 wheels are not available on the release page: [0.6.2 release page](https://github.com/vllm-project/vllm/releases/tag/v0.6.2) While...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Missing cu118 wheels for 0.6.2 release stale Hello, For version 0.6.2, the cu118 wheels are not available on the release page: [0.6.2 release page](https://github.com/vllm-project/vllm/releases/tag/v0.6.2) While...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
