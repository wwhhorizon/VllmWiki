# vllm-project/vllm#3794: [Feature]: Make `outlines` dependency optional

| 字段 | 值 |
| --- | --- |
| Issue | [#3794](https://github.com/vllm-project/vllm/issues/3794) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make `outlines` dependency optional

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm using a newer version of `outlines` than v0.0.34, and my application needs the fixes implemented in newer versions of that package. It would be great if `vllm` could make its structured generation dependencies optional, as I'm not using the internal `vllm` structured generation, but rather using the logits processors from `outlines` directly. ### Alternatives _No response_ ### Additional context This prevents me from updating to `vllm==0.4.0`.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: Make `outlines` dependency optional feature request;unstale ### 🚀 The feature, motivation and pitch I'm using a newer version of `outlines` than v0.0.34, and my application needs the fixes implemented in newe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Make `outlines` dependency optional feature request;unstale ### 🚀 The feature, motivation and pitch I'm using a newer version of `outlines` than v0.0.34, and my application needs the fixes implemented in newe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
