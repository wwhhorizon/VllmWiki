# vllm-project/vllm#10491: [Feature]: KVPress

| 字段 | 值 |
| --- | --- |
| Issue | [#10491](https://github.com/vllm-project/vllm/issues/10491) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;gemm_linear |
| 子分类 |  |
| Operator 关键词 | cache |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: KVPress

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://github.com/NVIDIA/kvpress Deploying long-context LLMs is costly due to the linear growth of the key-value (KV) cache in transformer models. For example, handling 1M tokens with Llama 3.1-70B in float16 requires up to 330GB of memory. This repository implements multiple KV cache pruning methods and benchmarks using [🤗 transformers](https://huggingface.co/docs/transformers/en/index), aiming to simplify the development of new methods for researchers and developers in this field. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: stly due to the linear growth of the key-value (KV) cache in transformer models. For example, handling 1M tokens with Llama 3.1-70B in float16 requires up to 330GB of memory. This repository implements multiple KV cache...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: KVPress feature request;stale ### 🚀 The feature, motivation and pitch https://github.com/NVIDIA/kvpress Deploying long-context LLMs is costly due to the linear growth of the key-value (KV) cache in transforme...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: memory. This repository implements multiple KV cache pruning methods and benchmarks using [🤗 transformers](https://huggingface.co/docs/transformers/en/index), aiming to simplify the development of new methods for resear...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ransformer models. For example, handling 1M tokens with Llama 3.1-70B in float16 requires up to 330GB of memory. This repository implements multiple KV cache pruning methods and benchmarks using [🤗 transformers](https:/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ers/en/index), aiming to simplify the development of new methods for researchers and developers in this field. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
