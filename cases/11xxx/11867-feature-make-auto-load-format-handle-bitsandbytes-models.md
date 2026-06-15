# vllm-project/vllm#11867: [Feature]: Make `auto` load format handle bitsandbytes models

| 字段 | 值 |
| --- | --- |
| Issue | [#11867](https://github.com/vllm-project/vllm/issues/11867) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make `auto` load format handle bitsandbytes models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Common bitsandbytes models like `unsloth/meta-llama-3.1-8b-bnb-4bit` require the user to pass `--load-format bitsandbytes --quantization bitsandbytes` command-line arguments. I could be wrong, but I believe both of these could be auto-detected by vLLM. The default load format `auto` could select `bitsandbytes` if a bitsandbytes model is selected. AFAIK this detection should work: ```python config.get("quantization_config", {}).get("quant_method") == "bitsandbytes" ``` Similarly the `--quantization bitsandbytes` argument seems redundant since the quantization is specified in the model config, but if the user omits it then this happens: ``` File "/usr/local/lib/python3.12/dist-packages/vllm/engine/arg_utils.py", line 1034, in create_engine_config raise ValueError( ValueError: BitsAndBytes load format and QLoRA adapter only support 'bitsandbytes' quantization, but got None ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/l...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Make `auto` load format handle bitsandbytes models feature request ### 🚀 The feature, motivation and pitch Common bitsandbytes models like `unsloth/meta-llama-3.1-8b-bnb-4bit` require the user to pass `--load...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tion bitsandbytes` argument seems redundant since the quantization is specified in the model config, but if the user omits it then this happens: ``` File "/usr/local/lib/python3.12/dist-packages/vllm/engine/arg_utils.py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: -3.1-8b-bnb-4bit` require the user to pass `--load-format bitsandbytes --quantization bitsandbytes` command-line arguments. I could be wrong, but I believe both of these could be auto-detected by vLLM. The default load...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 🚀 The feature, motivation and pitch Common bitsandbytes models like `unsloth/meta-llama-3.1-8b-bnb-4bit` require the user to pass `--load-format bitsandbytes --quantization bitsandbytes` command-line arguments. I could...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
