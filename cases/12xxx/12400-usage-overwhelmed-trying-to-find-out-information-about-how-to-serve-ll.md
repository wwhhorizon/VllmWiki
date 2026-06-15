# vllm-project/vllm#12400: [Usage]: Overwhelmed trying to find out information about how to serve Llama-3 70b to multiple users with 128k context

| 字段 | 值 |
| --- | --- |
| Issue | [#12400](https://github.com/vllm-project/vllm/issues/12400) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Overwhelmed trying to find out information about how to serve Llama-3 70b to multiple users with 128k context

### Issue 正文摘录

Hey everyone, I am having a really hard time finding out the requirements and expected results for my planned set-up. I want to use vLLM to serve Llama-3.3-70b to about 5 people with a full context window of 128k tokens. And I'm already confused, because Llama-3.3 isn't listed as supported model in the vLLM docs, so I guess, I'd have to use Llama-3.1. But how do I find out, how much VRAM I need for serving the model at 8-bit/6-bit with its full context window? How do I find out, how many people could use the model at the same time, how many t/s to expect, etc.? Sorry, if this is an obvious question, but I would really appreciate any help.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Overwhelmed trying to find out information about how to serve Llama-3 70b to multiple users with 128k context usage;stale Hey everyone, I am having a really hard time finding out the requirements and expected r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t, etc.? Sorry, if this is an obvious question, but I would really appreciate any help.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: about how to serve Llama-3 70b to multiple users with 128k context usage;stale Hey everyone, I am having a really hard time finding out the requirements and expected results for my planned set-up. I want to use vLLM to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
