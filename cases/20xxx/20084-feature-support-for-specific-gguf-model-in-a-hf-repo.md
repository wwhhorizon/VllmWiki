# vllm-project/vllm#20084: [Feature]: Support for specific GGUF model in a HF Repo

| 字段 | 值 |
| --- | --- |
| Issue | [#20084](https://github.com/vllm-project/vllm/issues/20084) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for specific GGUF model in a HF Repo

### Issue 正文摘录

### 🚀 The feature, motivation and pitch GGUF seems to be one of the most common quantization formats and normally available from day one, but running them with vllm docker is quite complicated, as you can't just specify the HF path and must download locally the specific file you want to run and include it in the volumes. It would be great for the project to accept a full model path when using GGUF, for example: ``` unsloth/Mistral-Small-3.2-24B-Instruct-2506-GGUF/Mistral-Small-3.2-24B-Instruct-2506-BF16.gguf ``` or ``` https://huggingface.co/unsloth/Mistral-Small-3.2-24B-Instruct-2506-GGUF/resolve/main/Mistral-Small-3.2-24B-Instruct-2506-BF16.gguf ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support for specific GGUF model in a HF Repo good first issue;feature request ### 🚀 The feature, motivation and pitch GGUF seems to be one of the most common quantization formats and normally available from d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Support for specific GGUF model in a HF Repo good first issue;feature request ### 🚀 The feature, motivation and pitch GGUF seems to be one of the most common quantization formats and normally available from d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e feature, motivation and pitch GGUF seems to be one of the most common quantization formats and normally available from day one, but running them with vllm docker is quite complicated, as you can't just specify the HF...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ept a full model path when using GGUF, for example: ``` unsloth/Mistral-Small-3.2-24B-Instruct-2506-GGUF/Mistral-Small-3.2-24B-Instruct-2506-BF16.gguf ``` or ``` https://huggingface.co/unsloth/Mistral-Small-3.2-24B-Inst...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: project to accept a full model path when using GGUF, for example: ``` unsloth/Mistral-Small-3.2-24B-Instruct-2506-GGUF/Mistral-Small-3.2-24B-Instruct-2506-BF16.gguf ``` or ``` https://huggingface.co/unsloth/Mistral-Smal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
