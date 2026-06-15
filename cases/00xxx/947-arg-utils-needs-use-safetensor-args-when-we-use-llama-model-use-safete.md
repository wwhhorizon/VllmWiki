# vllm-project/vllm#947: arg_utils needs “use_safetensor“ args，when we use llama model，use_safetensor will always be True

| 字段 | 值 |
| --- | --- |
| Issue | [#947](https://github.com/vllm-project/vllm/issues/947) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> arg_utils needs “use_safetensor“ args，when we use llama model，use_safetensor will always be True

### Issue 正文摘录

llama.py load_weights function have "use_safetensor" args,but in model_loader.py get_model function call model.load_weights don't have use_safetensor args，when we use llama model，use_safetensor will always be True。

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: arg_utils needs “use_safetensor“ args，when we use llama model，use_safetensor will always be True llama.py load_weights function have "use_safetensor" args,but in model_loader.py get_model function call model.load_weight...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
