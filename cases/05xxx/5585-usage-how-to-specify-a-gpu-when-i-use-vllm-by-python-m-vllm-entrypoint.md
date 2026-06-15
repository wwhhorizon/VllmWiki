# vllm-project/vllm#5585: [Usage]: How to specify a GPU when i use vllm by 'python -m vllm.entrypoints.openai.api_server --served-model-name..'

| 字段 | 值 |
| --- | --- |
| Issue | [#5585](https://github.com/vllm-project/vllm/issues/5585) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to specify a GPU when i use vllm by 'python -m vllm.entrypoints.openai.api_server --served-model-name..'

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Usage]: How to specify a GPU when i use vllm by 'python -m vllm.entrypoints.openai.api_server --served-model-name..' usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would yo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hen i use vllm by 'python -m vllm.entrypoints.openai.api_server --served-model-name..' usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to ru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
