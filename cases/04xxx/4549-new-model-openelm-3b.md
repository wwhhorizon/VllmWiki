# vllm-project/vllm#4549: [New Model]: OpenELM-3B

| 字段 | 值 |
| --- | --- |
| Issue | [#4549](https://github.com/vllm-project/vllm/issues/4549) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: OpenELM-3B

### Issue 正文摘录

### The model to consider. [apple/OpenELM-3B](https://huggingface.co/apple/OpenELM-3B) ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? OpenELM models have a dynamic head num for each layer, which needs a dynamic kv_cache for page attention: ``` "num_kv_heads": [ 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5 ], "num_query_heads": [ 12, 12, 12, 12, 12, 16, 16, 16, 16, 16, 16, 16, 20, 20, 20, 20 ], "num_transformer_layers": 16, ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: OpenELM-3B new-model ### The model to consider. [apple/OpenELM-3B](https://huggingface.co/apple/OpenELM-3B) ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
