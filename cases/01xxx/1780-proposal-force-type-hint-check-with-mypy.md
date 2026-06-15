# vllm-project/vllm#1780: Proposal: force type hint check with mypy

| 字段 | 值 |
| --- | --- |
| Issue | [#1780](https://github.com/vllm-project/vllm/issues/1780) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Proposal: force type hint check with mypy

### Issue 正文摘录

## Why While I am learning the source code, I found it challenging to understand asyncio. Taking this codebase as an example, I spend quite some time with the following method signature: https://github.com/vllm-project/vllm/blob/7c600440f7560348e571f021f2b2d1469de5264d/vllm/engine/async_llm_engine.py#L394-L399 I realized there was a discrepancy in the return type hint. The original hint was: ```python -> RequestOutput: ``` However, the correct hint should be: ```python -> typing.AsyncIterator[RequestOutput]: ``` For a detailed demonstration of this issue, please see the appendix below. ## Proposal To enhance type checking with mypy, it's advisable to include the following options in mypy.ini, as suggested in [this StackOverflow answer](https://stackoverflow.com/a/70913528): ``` disallow_untyped_defs disallow_incomplete_defs disallow_untyped_calls ``` ## Appendix Below is a complete example that illustrates the correct use of type hints for async iterators: ```python """ For a full check including type hints, run the following command mypy \ --disallow-untyped-defs \ --disallow-incomplete-defs \ --disallow-untyped-calls \ /tmp/a.py """ import asyncio import typing async def foo() -...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: I am learning the source code, I found it challenging to understand asyncio. Taking this codebase as an example, I spend quite some time with the following method signature: https://github.com/vllm-project/vllm/blob/7c6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Proposal: force type hint check with mypy feature request;stale ## Why While I am learning the source code, I found it challenging to understand asyncio. Taking this codebase as an example, I spend quite some time with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
