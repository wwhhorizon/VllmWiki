# vllm-project/vllm#4080: [Usage]: how to use tools/tool_choice while using open api endpoints

| 字段 | 值 |
| --- | --- |
| Issue | [#4080](https://github.com/vllm-project/vllm/issues/4080) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to use tools/tool_choice while using open api endpoints

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a mistral 8X7B model.I want to utilize function calling / tools while inferencing using open ai compatible API endpoints but I am not able to get details around it. is this supported? if not what is the timeline of having this.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: stral 8X7B model.I want to utilize function calling / tools while inferencing using open ai compatible API endpoints but I am not able to get details around it. is this supported? if not what is the timeline of having t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ow would you like to use vllm I want to run inference of a mistral 8X7B model.I want to utilize function calling / tools while inferencing using open ai compatible API endpoints but I am not able to get details around i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
