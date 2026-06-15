# vllm-project/vllm#8263: [New Model]: Support for Idefics3 8B Llama3

| 字段 | 值 |
| --- | --- |
| Issue | [#8263](https://github.com/vllm-project/vllm/issues/8263) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support for Idefics3 8B Llama3

### Issue 正文摘录

### The model to consider. https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3 ### The closest model vllm already supports. The model is built on top of two pre-trained models: [google/siglip-so400m-patch14-384](https://huggingface.co/google/siglip-so400m-patch14-384) and [meta-llama/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct). ### What's your difficulty of supporting the model you want? As for now no model of the Idefics architectures are supported by vLLM Idefics3ForConditionalGeneration Idefics2ForConditionalGeneration see also https://github.com/vllm-project/vllm/issues/4124 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Support for Idefics3 8B Llama3 new-model ### The model to consider. https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3 ### The closest model vllm already supports. The model is built on top of two pre-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ty of supporting the model you want? As for now no model of the Idefics architectures are supported by vLLM Idefics3ForConditionalGeneration Idefics2ForConditionalGeneration see also https://github.com/vllm-project/vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
