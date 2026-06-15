# vllm-project/vllm#10263: [Bug]: qwen cannot be quantized in vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#10263](https://github.com/vllm-project/vllm/issues/10263) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen cannot be quantized in vllm

### Issue 正文摘录

### Your current environment gpu A10 vllm version: 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug for qwen series, such as `Qwen/Qwen2.5-7B-Instruct`, it seems that vllm cannot apply quantization to it. no matther for `bitsandbytes` or `awq` . even for `unsloth` version, `unsloth/Qwen2.5-7B-Instruct-bnb-4bit` it does not work either. error message: `AttributeError: Model Qwen2ForCausalLM does not support BitsAndBytes quantization yet.` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen cannot be quantized in vllm bug ### Your current environment gpu A10 vllm version: 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug for qwen series, such as `Qwen/Qwen2.5-7B-Instruct`,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nnot be quantized in vllm bug ### Your current environment gpu A10 vllm version: 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug for qwen series, such as `Qwen/Qwen2.5-7B-Instruct`, it seems that...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: qwen cannot be quantized in vllm bug ### Your current environment gpu A10 vllm version: 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug for qwen series, such as `Qwen/Qwen2.5-7B-Instruct`,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: t.` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: uantization to it. no matther for `bitsandbytes` or `awq` . even for `unsloth` version, `unsloth/Qwen2.5-7B-Instruct-bnb-4bit` it does not work either. error message: `AttributeError: Model Qwen2ForCausalLM does not sup...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
