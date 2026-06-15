# vllm-project/vllm#3494: [Usage]: memory out of use

| 字段 | 值 |
| --- | --- |
| Issue | [#3494](https://github.com/vllm-project/vllm/issues/3494) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: memory out of use

### Issue 正文摘录

### Your current environment ```text The output of `python multilora_inference.py` ``` 原模型Mixtral-8x7B-v0.1单卡A100可以跑，用了80G内存以内，使用了vllm后，要两张A100才能跑起来，内存达到了160G。这个有什么参数可以优化吗 ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 化吗 ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: The output of `python multilora_inference.py` ``` 原模型Mixtral-8x7B-v0.1单卡A100可以跑，用了80G内存以内，使用了vllm后，要两张A100才能跑起来，内存达到了160G。这个有什么参数可以优化吗 ### How would you like to use vllm I want to run inference of a [specific model](put...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
