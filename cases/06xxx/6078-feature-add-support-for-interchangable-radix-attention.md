# vllm-project/vllm#6078: [Feature]: Add support for interchangable radix attention

| 字段 | 值 |
| --- | --- |
| Issue | [#6078](https://github.com/vllm-project/vllm/issues/6078) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for interchangable radix attention

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am working on adjustment of radix attentions now. Thank you for your support for the radix attention. Currently, catching for A that allows for more efficient A+B generation. However, in some tree-of-thoughts settings, we are also interested for caching A+B, A+C, A+D, and thus more efficiently generates A+B+C+D. I think this feature could be developed with some adjustment from the current function of `enable_prefix_caching. I would also really appreciate if you could share some insights on how to implement this function from the current implementation of prefix_caching. Thank you very much for the great work! ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Add support for interchangable radix attention feature request;stale ### 🚀 The feature, motivation and pitch I am working on adjustment of radix attentions now. Thank you for your support for the radix attent...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the radix attention. Currently, catching for A that allows for more efficient A+B generation. However, in some tree-of-thoughts settings, we are also interested for caching A+B, A+C, A+D, and thus more efficiently gener...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
