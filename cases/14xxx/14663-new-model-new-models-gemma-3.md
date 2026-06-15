# vllm-project/vllm#14663: [New Model]: New models Gemma 3

| 字段 | 值 |
| --- | --- |
| Issue | [#14663](https://github.com/vllm-project/vllm/issues/14663) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: New models Gemma 3

### Issue 正文摘录

### The model to consider. Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions. Gemma 3 models are well-suited for a variety of text generation and image understanding tasks, including question answering, summarization, and reasoning. Inputs and outputs Input: Text string, such as a question, a prompt, or a document to be summarized Images, normalized to 896 x 896 resolution and encoded to 256 tokens each Total input context of 128K tokens for the 4B, 12B, and 27B sizes, and 32K tokens for the 1B size Output: Generated text in response to the input, such as an answer to a question, analysis of image content, or a summary of a document Total output context of 8192 tokens https://huggingface.co/collections/google/gemma-3-release-67c6c6f89c4f76621268bb6d https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf ### The closest model vllm already supports. Gemma 2 ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner o...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: New models Gemma 3 new-model ### The model to consider. Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions. Gemma 3 m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: port in over 140 languages, and is available in more sizes than previous versions. Gemma 3 models are well-suited for a variety of text generation and image understanding tasks, including question answering, summarizati...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [New Model]: New models Gemma 3 new-model ### The model to consider. Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions. Gemma 3 m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
