# vllm-project/vllm#1565: Adding support for switch-transformer / NLLB-MoE

| 字段 | 值 |
| --- | --- |
| Issue | [#1565](https://github.com/vllm-project/vllm/issues/1565) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Adding support for switch-transformer / NLLB-MoE

### Issue 正文摘录

Hi vLLM Team, Thanks again for the great work! Recently my collaborator and I have been working on MoE and like to try to integrate vLLM with SwitchTransformer / FairSeq. I was wondering if you mind sharing if there is any effort already going on and what would be the major challenges? https://huggingface.co/docs/transformers/main/model_doc/nllb-moe https://github.dev/huggingface/transformers/blob/main/src/transformers/models/switch_transformers/modeling_switch_transformers.py Thanks, Lisa

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: effort already going on and what would be the major challenges? https://huggingface.co/docs/transformers/main/model_doc/nllb-moe https://github.dev/huggingface/transformers/blob/main/src/transformers/models/switch_trans...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Adding support for switch-transformer / NLLB-MoE Hi vLLM Team, Thanks again for the great work! Recently my collaborator and I have been working on MoE and like to try to integrate vLLM with SwitchTransformer / FairSeq....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
