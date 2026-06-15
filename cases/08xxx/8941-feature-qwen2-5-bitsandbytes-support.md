# vllm-project/vllm#8941: [Feature]: Qwen2.5 bitsandbytes support

| 字段 | 值 |
| --- | --- |
| Issue | [#8941](https://github.com/vllm-project/vllm/issues/8941) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen2.5 bitsandbytes support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Description: Qwen2.5 (32B) is a state-of-the-art model, especially interesting in 4-bit precision (bitsandbytes). - I tried integrating it, but the model did not work as expected. the model output is just "!!!!!" - I created a [Colab](https://colab.research.google.com/drive/1Eyh7v_9Y7zyQV4hwYQ9eC3jY0iKTNCQp?usp=sharing) showing Qwen2.5 works in the transformers library but fails in vllm after my modification. in this notebook i show how the model is working using hugginface, and how after adding bitsandbytes support the output is gibberish i tried to add this lines, under `Qwen2ForCausalLM` class: ``` bitsandbytes_stacked_params_mapping = { # shard_name, weight_name, index "q_proj": ("qkv_proj", 0), "k_proj": ("qkv_proj", 1), "v_proj": ("qkv_proj", 2), "gate_proj": ("gate_up_proj", 0), "up_proj": ("gate_up_proj", 1), } ``` - There is similar [PR](https://github.com/vllm-project/vllm/pull/8338) just merge where adding bitsandbytes to Gemma2 bad output example > Prompt: 'The future of AI is', Generated text: '!!!!!!!!!!!!!!!!' ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make su...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Qwen2.5 bitsandbytes support feature request ### 🚀 The feature, motivation and pitch Description: Qwen2.5 (32B) is a state-of-the-art model, especially interesting in 4-bit precision (bitsandbytes). - I tried...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: en2.5 (32B) is a state-of-the-art model, especially interesting in 4-bit precision (bitsandbytes). - I tried integrating it, but the model did not work as expected. the model output is just "!!!!!" - I created a [Colab]...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n and pitch Description: Qwen2.5 (32B) is a state-of-the-art model, especially interesting in 4-bit precision (bitsandbytes). - I tried integrating it, but the model did not work as expected. the model output is just "!...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: the model output is just "!!!!!" - I created a [Colab](https://colab.research.google.com/drive/1Eyh7v_9Y7zyQV4hwYQ9eC3jY0iKTNCQp?usp=sharing) showing Qwen2.5 works in the transformers library but fails in vllm after my...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nes, under `Qwen2ForCausalLM` class: ``` bitsandbytes_stacked_params_mapping = { # shard_name, weight_name, index "q_proj": ("qkv_proj", 0), "k_proj": ("qkv_proj", 1), "v_proj": ("qkv_proj", 2), "gate_proj": ("gate_up_p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
