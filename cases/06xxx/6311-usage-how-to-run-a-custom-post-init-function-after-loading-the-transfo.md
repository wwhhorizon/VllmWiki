# vllm-project/vllm#6311: [Usage]: How to run a custom post_init() function after loading the transformers model using LLM class

| 字段 | 值 |
| --- | --- |
| Issue | [#6311](https://github.com/vllm-project/vllm/issues/6311) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to run a custom post_init() function after loading the transformers model using LLM class

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I have a specific use case where I want to run a custom function. Something like `post_init()` in `transformers` after loading a model using `LLM()`. Is there a way to achieve this?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hon collect_env.py` ``` ### How would you like to use vllm I have a specific use case where I want to run a custom function. Something like `post_init()` in `transformers` after loading a model using `LLM()`. Is there a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: How to run a custom post_init() function after loading the transformers model using LLM class usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: it() function after loading the transformers model using LLM class usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I have a specific use case...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
