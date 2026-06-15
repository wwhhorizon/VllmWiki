# vllm-project/vllm#13172: [New Model]: Surya OCR

| 字段 | 值 |
| --- | --- |
| Issue | [#13172](https://github.com/vllm-project/vllm/issues/13172) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Surya OCR

### Issue 正文摘录

### The model to consider. I'm trying to port this model - https://huggingface.co/vikp/surya_rec2 to vLLM. I'm hitting a few roadblocks that I need guidance on ### The closest model vllm already supports. https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mllama.py is the closest model, as it takes image inputs as cross-attention, unlike LLaVA-style models ### What's your difficulty of supporting the model you want? The model has the following architecture - Image Encoder (Swin Based) -> Text Encoder -> Decoder The Text Encoder performs cross attention over `encoder_input_ids` and `image_embeds` from the image encoder. The Decoder further performs cross attention over `decoder_input_ids` and `text_encoder_hidden_states`. Implementing the text encoder and decoder mostly follows that of mllama. However, porting the image encoder fully to vLLM is tricky due to the implementation of the SwinTransformers-Style attention windowing etc. Is there a way to use the (original) image encoder to produce image embeds, and explicitly cache these for usage by the (Text Encoder + Decoder) stack? I know this is kind of how it works for LLaVA style models, but I am unclear how...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Surya OCR new-model;stale ### The model to consider. I'm trying to port this model - https://huggingface.co/vikp/surya_rec2 to vLLM. I'm hitting a few roadblocks that I need guidance on ### The closest mode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [New Model]: Surya OCR new-model;stale ### The model to consider. I'm trying to port this model - https://huggingface.co/vikp/surya_rec2 to vLLM. I'm hitting a few roadblocks that I need guidance on ### The closest mode...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ay to use the (original) image encoder to produce image embeds, and explicitly cache these for usage by the (Text Encoder + Decoder) stack? I know this is kind of how it works for LLaVA style models, but I am unclear ho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ifficulty of supporting the model you want? The model has the following architecture - Image Encoder (Swin Based) -> Text Encoder -> Decoder The Text Encoder performs cross attention over `encoder_input_ids` and `image_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: - https://huggingface.co/vikp/surya_rec2 to vLLM. I'm hitting a few roadblocks that I need guidance on ### The closest model vllm already supports. https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
