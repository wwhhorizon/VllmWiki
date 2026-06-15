# vllm-project/vllm#29862: [Model loading error]: quantized version of Llama-3.2-11B-Vision-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#29862](https://github.com/vllm-project/vllm/issues/29862) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;multimodal_vlm;quantization |
| 子分类 | env_compat |
| Operator 关键词 | quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Model loading error]: quantized version of Llama-3.2-11B-Vision-Instruct

### Issue 正文摘录

### The model to consider. quantized version of Llama-3.2-11B-Vision-Instruct (4 bit or 8 bit) https://huggingface.co/unsloth/Llama-3.2-11B-Vision-Instruct-bnb-4bit or https://huggingface.co/pbatra/Llama-3.2-11B-Vision-Instruct-GGUF or any 4 bit / 8 bit version of this LLM ### The closest model vllm already supports. https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct (official non quantized ### What's your difficulty of supporting the model you want? I have tried to load a 4 bit version of Llama-3.2-11B-Vision-Instruct but I got errors I have used official vllm docker running on two diffrent machines ( nvidia tesla T4 16 GB and Nvidia H100 96 GB) the non quantized version: https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct worked on nvidia h100 The error happens because the Llama 3.2 Vision model uses a specialized vision processor (MllamaProcessor), and the current vLLM code (even in the latest nightly build, v0.11.2.dev347) doesn't have the expected function (_get_num_multimodal_tokens) implemented for that processor type. This issue is deep within the vLLM framework's handling of the model's multimodal components ### Before submitting a new issue... -...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Model loading error]: quantized version of Llama-3.2-11B-Vision-Instruct stale ### The model to consider. quantized version of Llama-3.2-11B-Vision-Instruct (4 bit or 8 bit) https://huggingface.co/unsloth/Llama-3.2-11B
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Model loading error]: quantized version of Llama-3.2-11B-Vision-Instruct stale ### The model to consider. quantized version of Llama-3.2-11B-Vision-Instruct (4 bit or 8 bit) https://huggingface.co/unsloth/Llama-3.2-11B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cker running on two diffrent machines ( nvidia tesla T4 16 GB and Nvidia H100 96 GB) the non quantized version: https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct worked on nvidia h100 The error happens bec...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Model loading error]: quantized version of Llama-3.2-11B-Vision-Instruct stale ### The model to consider. quantized version of Llama-3.2-11B-Vision-Instruct (4 bit or 8 bit) https://huggingface.co/unsloth/Llama-3.2-11B...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Llama-3.2-11B-Vision-Instruct (4 bit or 8 bit) https://huggingface.co/unsloth/Llama-3.2-11B-Vision-Instruct-bnb-4bit or https://huggingface.co/pbatra/Llama-3.2-11B-Vision-Instruct-GGUF or any 4 bit / 8 bit version of th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
