# vllm-project/vllm#3908: [Usage]: I have two Gpus, how do I make my model run on 2 gpus

| 字段 | 值 |
| --- | --- |
| Issue | [#3908](https://github.com/vllm-project/vllm/issues/3908) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: I have two Gpus, how do I make my model run on 2 gpus

### Issue 正文摘录

### Your current environment ```text python -m vllm.entrypoints.openai.api_server --served-model-name Qwen1.5-0.5B-Chat --model /home/project/models/qwen-0.5b ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: I have two Gpus, how do I make my model run on 2 gpus usage ### Your current environment ```text python -m vllm.entrypoints.openai.api_server --served-model-name Qwen1.5-0.5B-Chat --model /home/project/models/q...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
