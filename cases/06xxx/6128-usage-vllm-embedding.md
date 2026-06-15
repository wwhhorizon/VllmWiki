# vllm-project/vllm#6128: [Usage]: vllm现在支持embedding输入吗，没有发现相关接口

| 字段 | 值 |
| --- | --- |
| Issue | [#6128](https://github.com/vllm-project/vllm/issues/6128) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm现在支持embedding输入吗，没有发现相关接口

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vllm现在支持embedding输入吗，没有发现相关接口 usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
