# vllm-project/vllm#6824: [Usage]: How do I deploy a model on two GPUs with different memory?

| 字段 | 值 |
| --- | --- |
| Issue | [#6824](https://github.com/vllm-project/vllm/issues/6824) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How do I deploy a model on two GPUs with different memory?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. I have two GPUS with 30G and 50G memory left, how do I set them up to get the most out of the 80G? I checked the documentation and didn't seem to find any directives related to it

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. I have two GPUS with 30G and 50G memory left, how do I set them up to get t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: How do I deploy a model on two GPUs with different memory? usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
