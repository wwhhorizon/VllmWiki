# vllm-project/vllm#2043: The returned results using prompt_logprobs=1

| 字段 | 值 |
| --- | --- |
| Issue | [#2043](https://github.com/vllm-project/vllm/issues/2043) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The returned results using prompt_logprobs=1

### Issue 正文摘录

It seems that setting prompt_logprobs=1 will return the scoring of the context (i.e., prompt). However, the returned results are a little confusing: When I used a Llama-2-7b to score a sequece, the returned results look as follow: [None, {15043: -7.584228515625, 917: -2.512939214706421}, {29892: -1.4937736988067627}, {590: -1.8308428525924683, 306: -1.3464678525924683}, {1024: -0.11963547021150589}, {338: -0.01794273406267166}] The first and third positions have two keys while the other positions have only 1 key. Is that because the position's word is not the word with the highest prob?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t). However, the returned results are a little confusing: When I used a Llama-2-7b to score a sequece, the returned results look as follow: [None, {15043: -7.584228515625, 917: -2.512939214706421}, {29892: -1.4937736988...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: The returned results using prompt_logprobs=1 documentation;stale It seems that setting prompt_logprobs=1 will return the scoring of the context (i.e., prompt). However, the returned results are a little confusing: When...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
