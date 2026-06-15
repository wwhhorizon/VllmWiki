# vllm-project/vllm#4833: [New Model]: Google's Paligemma family of models

| 字段 | 值 |
| --- | --- |
| Issue | [#4833](https://github.com/vllm-project/vllm/issues/4833) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Google's Paligemma family of models

### Issue 正文摘录

### The model to consider. https://huggingface.co/google/paligemma-3b-pt-896 ### The closest model vllm already supports. I think the only visual language model supported right now is LLava but I could be wrong. ### What's your difficulty of supporting the model you want? _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Google's Paligemma family of models new-model ### The model to consider. https://huggingface.co/google/paligemma-3b-pt-896 ### The closest model vllm already supports. I think the only visual language model...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [New Model]: Google's Paligemma family of models new-model ### The model to consider. https://huggingface.co/google/paligemma-3b-pt-896 ### The closest model vllm already supports. I think the only visual language model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
