# vllm-project/vllm#6584: [Feature]: LLM2Vec (Fine-Tuned Embeddings) Support

| 字段 | 值 |
| --- | --- |
| Issue | [#6584](https://github.com/vllm-project/vllm/issues/6584) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: LLM2Vec (Fine-Tuned Embeddings) Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **[LLM2Vec](https://huggingface.co/McGill-NLP/LLM2Vec-Meta-Llama-3-8B-Instruct-mntp) is a powerful approach to convert LLMs into embedding models. They show strong results on the MTEB and it's also possible to fine-tune LoRA adapters for the embeddings. Would it be possible to support these embedding models,** in particular for Llama3? ### Additional context The embedding models are similar to base LLM models except for enabling bidirectional attention. I trained a LoRA adapter for the Llama3 (LlamaForCausalLM, Meta-Llama3-8B-Instruct) and merged it. Per default, it gets merged as a "LlamaBiModel", which is currently not supported. When I played around and replaced the architecture with LlamaForCausalLM), I get KeyError: "embed_tokens.weight", so it's not simply replacable. If it's not possible to take on this feature right now, I'd greatly appreciate any guidance or resources that could help me start working on it. This request is related to the [discussion of embedding models in general](https://github.com/vllm-project/vllm/discussions/310).

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: uest;stale ### 🚀 The feature, motivation and pitch **[LLM2Vec](https://huggingface.co/McGill-NLP/LLM2Vec-Meta-Llama-3-8B-Instruct-mntp) is a powerful approach to convert LLMs into embedding models. They show strong resu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: LLM2Vec (Fine-Tuned Embeddings) Support feature request;stale ### 🚀 The feature, motivation and pitch **[LLM2Vec](https://huggingface.co/McGill-NLP/LLM2Vec-Meta-Llama-3-8B-Instruct-mntp) is a powerful approac...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: If it's not possible to take on this feature right now, I'd greatly appreciate any guidance or resources that could help me start working on it. This request is related to the [discussion of embedding models in general]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: which is currently not supported. When I played around and replaced the architecture with LlamaForCausalLM), I get KeyError: "embed_tokens.weight", so it's not simply replacable. If it's not possible to take on this fea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
