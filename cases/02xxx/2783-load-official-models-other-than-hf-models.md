# vllm-project/vllm#2783: load official models other than HF models 

| 字段 | 值 |
| --- | --- |
| Issue | [#2783](https://github.com/vllm-project/vllm/issues/2783) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> load official models other than HF models 

### Issue 正文摘录

does vllm load the models which are supported from huggingface ? when i tried to load the official llama models via llm it failed with an error stating config.json is missing

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: load official models other than HF models does vllm load the models which are supported from huggingface ? when i tried to load the official llama models via llm it failed with an error stating config.json is missing
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: load official models other than HF models does vllm load the models which are supported from huggingface ? when i tried to load the official llama models via llm it failed with an error stating config.json is missing

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
