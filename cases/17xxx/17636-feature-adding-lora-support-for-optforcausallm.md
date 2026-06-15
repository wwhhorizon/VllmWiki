# vllm-project/vllm#17636: [Feature]: Adding LoRA support for OPTForCausalLM.

| 字段 | 值 |
| --- | --- |
| Issue | [#17636](https://github.com/vllm-project/vllm/issues/17636) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Adding LoRA support for OPTForCausalLM.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm running ``` vllm serve unsloth/qwen3-4b-unsloth-bnb-4bit --enable-lora --lora-modules adapter_name=checkpoint_xxx --dtype auto --api-key xxx ``` and unfortunately getting this error: ``` ValueError: OPTForCausalLM does not support LoRA yet. ``` My pretrained model is a `PeftModelForCausalLM`, fine-tuned with `unsloth`. I'm trying to build an OpenAI-compatible server with this model, and it would be great if vllm support it! Or, is there any alternative solution for this? Or am I doing it in the wrong way? Please let me know! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 🚀 The feature, motivation and pitch I'm running ``` vllm serve unsloth/qwen3-4b-unsloth-bnb-4bit --enable-lora --lora-modules adapter_name=checkpoint_xxx --dtype auto --api-key xxx ``` and unfortunately getting this err...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: el is a `PeftModelForCausalLM`, fine-tuned with `unsloth`. I'm trying to build an OpenAI-compatible server with this model, and it would be great if vllm support it! Or, is there any alternative solution for this? Or am...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: loth-bnb-4bit --enable-lora --lora-modules adapter_name=checkpoint_xxx --dtype auto --api-key xxx ``` and unfortunately getting this error: ``` ValueError: OPTForCausalLM does not support LoRA yet. ``` My pretrained mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: st ### 🚀 The feature, motivation and pitch I'm running ``` vllm serve unsloth/qwen3-4b-unsloth-bnb-4bit --enable-lora --lora-modules adapter_name=checkpoint_xxx --dtype auto --api-key xxx ``` and unfortunately getting t...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
