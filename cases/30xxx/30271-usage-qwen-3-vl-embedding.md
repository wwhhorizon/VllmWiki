# vllm-project/vllm#30271: [Usage]: Qwen 3 VL Embedding

| 字段 | 值 |
| --- | --- |
| Issue | [#30271](https://github.com/vllm-project/vllm/issues/30271) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Qwen 3 VL Embedding

### Issue 正文摘录

### Your current environment Hi I would like to ask if there is a way to extract Qwen 3 VL multimodal embeddings, similar to Jina Embeddings V4, for retrieval purposes? I've tried to initialize the model this way but it doesn't work: ``` model = LLM( model="Qwen/Qwen3-VL-8B-Instruct", task="embed", trust_remote_code=True, ) ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Qwen 3 VL Embedding usage ### Your current environment Hi I would like to ask if there is a way to extract Qwen 3 VL multimodal embeddings, similar to Jina Embeddings V4, for retrieval purposes? I've tried to i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Qwen 3 VL multimodal embeddings, similar to Jina Embeddings V4, for retrieval purposes? I've tried to initialize the model this way but it doesn't work: ``` model = LLM( model="Qwen/Qwen3-VL-8B-Instruct", task="embed",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
