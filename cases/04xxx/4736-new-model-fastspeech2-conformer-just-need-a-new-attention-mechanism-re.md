# vllm-project/vllm#4736: [New Model]: fastspeech2_conformer (just need a new attention mechanism: RelPositionMultiHeadedAttention)

| 字段 | 值 |
| --- | --- |
| Issue | [#4736](https://github.com/vllm-project/vllm/issues/4736) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: fastspeech2_conformer (just need a new attention mechanism: RelPositionMultiHeadedAttention)

### Issue 正文摘录

### The model to consider. https://huggingface.co/espnet/fastspeech2_conformer A complete model is not required, only need a new attention mechanism FastSpeech2ConformerAttention (following is the code): https://github.com/huggingface/transformers/blob/47735f5f0f2752500d115d2f6bd57816032599b6/src/transformers/models/fastspeech2_conformer/modeling_fastspeech2_conformer.py#L463 This new attention mechanism also is known as RelPositionMultiHeadedAttention (following is the code): https://github.com/wenet-e2e/wenet/blob/f2372ae6d97f926688fee821e609e42aaf41571d/wenet/transformer/attention.py#L294 ### The closest model vllm already supports. llama ### What's your difficulty of supporting the model you want? a new attention mechanism

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: fastspeech2_conformer (just need a new attention mechanism: RelPositionMultiHeadedAttention) new-model ### The model to consider. https://huggingface.co/espnet/fastspeech2_conformer A complete model is not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [New Model]: fastspeech2_conformer (just need a new attention mechanism: RelPositionMultiHeadedAttention) new-model ### The model to consider. https://huggingface.co/espnet/fastspeech2_conformer A complete model is not...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
