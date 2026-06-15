# vllm-project/vllm#5721: [New Model]: Chameleon support

| 字段 | 值 |
| --- | --- |
| Issue | [#5721](https://github.com/vllm-project/vllm/issues/5721) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Chameleon support

### Issue 正文摘录

### The model to consider. https://huggingface.co/facebook/chameleon (as of now, the models can be downloaded using the [model form](https://ai.meta.com/resources/models-and-libraries/chameleon-downloads/)) Chameleon is an interesting multimodal model architecture based on Llama 2. It adds image inputs and outputs to Llama 2 by tokenizing images using a VQ-VAE and adding the codebook to Llama's tokenizer vocabulary. In principle, it supports text and images as input and output in arbitrary combination. However, the released models were finetuned to prevent image generation. ### The closest model vllm already supports. LlamaForCausalLM ### What's your difficulty of supporting the model you want? For text->text support, the implementation should actually be fairly easy. The model is based on Llama-2 with the following differences: * QK norm * reordering the norm similar to Swin Transformer (normalizing the outputs of the attention and ffn blocks instead of the inputs) To enable image inputs, image tokenization using the provided VQ-VAE needs to be added. Further info: * Original paper: https://arxiv.org/abs/2405.09818 * Reference implementation: https://github.com/facebookresearch/c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Chameleon support new-model ### The model to consider. https://huggingface.co/facebook/chameleon (as of now, the models can be downloaded using the [model form](https://ai.meta.com/resources/models-and-libr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a VQ-VAE and adding the codebook to Llama's tokenizer vocabulary. In principle, it supports text and images as input and output in arbitrary combination. However, the released models were finetuned to prevent image gene...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ies/chameleon-downloads/)) Chameleon is an interesting multimodal model architecture based on Llama 2. It adds image inputs and outputs to Llama 2 by tokenizing images using a VQ-VAE and adding the codebook to Llama's t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ar to Swin Transformer (normalizing the outputs of the attention and ffn blocks instead of the inputs) To enable image inputs, image tokenization using the provided VQ-VAE needs to be added. Further info: * Original pap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
