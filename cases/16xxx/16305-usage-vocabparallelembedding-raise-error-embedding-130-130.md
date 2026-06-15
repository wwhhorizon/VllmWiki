# vllm-project/vllm#16305: [Usage]: VocabParallelEmbedding raise error embedding: [-130., -130., .....]

| 字段 | 值 |
| --- | --- |
| Issue | [#16305](https://github.com/vllm-project/vllm/issues/16305) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: VocabParallelEmbedding raise error embedding: [-130., -130., .....]

### Issue 正文摘录

### Your current environment I was trying to integrate a new multimodal model architecture into vLLM, but I ran into a numerical error when using VocabParallelEmbedding to get the embeddings. Below are the embedding results for token IDs 151665~151669, where the embeddings for 151666, 151668, and 151669 were reset to -130. I’m pretty sure the weights in my safetensors are correct. Do you have any idea what might cause this kind of issue? ![Image](https://github.com/user-attachments/assets/eb4caa27-a967-4488-bbfc-41d66b23e3f8) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ntegrate a new multimodal model architecture into vLLM, but I ran into a numerical error when using VocabParallelEmbedding to get the embeddings. Below are the embedding results for token IDs 151665~151669, where the em...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 8) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sage;stale ### Your current environment I was trying to integrate a new multimodal model architecture into vLLM, but I ran into a numerical error when using VocabParallelEmbedding to get the embeddings. Below are the em...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ur current environment I was trying to integrate a new multimodal model architecture into vLLM, but I ran into a numerical error when using VocabParallelEmbedding to get the embeddings. Below are the embedding results f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ocabParallelEmbedding raise error embedding: [-130., -130., .....] usage;stale ### Your current environment I was trying to integrate a new multimodal model architecture into vLLM, but I ran into a numerical error when...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
