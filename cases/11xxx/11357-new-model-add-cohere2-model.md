# vllm-project/vllm#11357: [New Model]: Add Cohere2 Model

| 字段 | 值 |
| --- | --- |
| Issue | [#11357](https://github.com/vllm-project/vllm/issues/11357) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Add Cohere2 Model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Recently cohere released a [CommandR7B](https://github.com/huggingface/transformers/tree/main/src/transformers/models/cohere2) model in huggingface and I would like to contribute the vllm implementation version of it. @simon-mo PR: https://github.com/vllm-project/vllm/pull/11358 The model also uses the interleave attention like gemma2 and mistral, so kv cache optimization is needed. I saw it is also on the roadmap. https://github.com/vllm-project/vllm/issues/9464 ### Alternatives _No response_ ### Additional context I have integrated and tested it work with all the benchmark scripts and would like to add a feature branch for review. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Add Cohere2 Model new-model ### 🚀 The feature, motivation and pitch Recently cohere released a [CommandR7B](https://github.com/huggingface/transformers/tree/main/src/transformers/models/cohere2) model in hu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ternatives _No response_ ### Additional context I have integrated and tested it work with all the benchmark scripts and would like to add a feature branch for review. ### Before submitting a new issue... - [X] Make sure...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: el in huggingface and I would like to contribute the vllm implementation version of it. @simon-mo PR: https://github.com/vllm-project/vllm/pull/11358 The model also uses the interleave attention like gemma2 and mistral,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ew. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: The model also uses the interleave attention like gemma2 and mistral, so kv cache optimization is needed. I saw it is also on the roadmap. https://github.com/vllm-project/vllm/issues/9464 ### Alternatives _No response_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
