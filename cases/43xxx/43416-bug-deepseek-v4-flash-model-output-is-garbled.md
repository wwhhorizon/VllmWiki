# vllm-project/vllm#43416: [Bug]: DeepSeek V4 Flash Model Output is Garbled

| 字段 | 值 |
| --- | --- |
| Issue | [#43416](https://github.com/vllm-project/vllm/issues/43416) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V4 Flash Model Output is Garbled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Mirror version: vllm/vllm-openai:v0.21.0 Execution parameters: --enable-prefix-caching --trust-remote-code --enable-auto-tool-choice --tensor-parallel-size 8 --max-model-len 8192 --tokenizer-mode deepseek_v4 --tool-call-parser deepseek_v4 --kv-cache-dtype fp8 --disable-custom-all-reduce Output status: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 2 --tokenizer-mode deepseek_v4 --tool-call-parser deepseek_v4 --kv-cache-dtype fp8 --disable-custom-all-reduce Output status: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: bled bug ### Your current environment ### 🐛 Describe the bug Mirror version: vllm/vllm-openai:v0.21.0 Execution parameters: --enable-prefix-caching --trust-remote-code --enable-auto-tool-choice --tensor-parallel-size 8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: l-len 8192 --tokenizer-mode deepseek_v4 --tool-call-parser deepseek_v4 --kv-cache-dtype fp8 --disable-custom-all-reduce Output status: ### Before submitting a new issue... - [x] Make sure you already searched for releva...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: DeepSeek V4 Flash Model Output is Garbled bug ### Your current environment ### 🐛 Describe the bug Mirror version: vllm/vllm-openai:v0.21.0 Execution parameters: --enable-prefix-caching --trust-remote-code --enabl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
