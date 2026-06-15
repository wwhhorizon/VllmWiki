# vllm-project/vllm#25333: [Bug]: Accuracy Discrepancy in Qwen 4B Embeddings: vLLM vs. Transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#25333](https://github.com/vllm-project/vllm/issues/25333) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Accuracy Discrepancy in Qwen 4B Embeddings: vLLM vs. Transformers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I served the Qwen 4B embedding model with Docker using vllm/vllm-openai:v0.10.1. I also designed a test to evaluate the strength of the embeddings. On that dataset, I reached an accuracy of 0.39. However, when I serve it using the transformers library, I achieve an accuracy of 0.41. serve code: ``` vllm serve /app/data/models/Qwen3-Embedding-4B/model \ --gpu-memory-utilization 0.16 \ --dtype bfloat16 \ --max-num-seqs 32 \ --max-model-len 12384 \ --served-model-name Qwen3-Embedding-4B ``` The reason for this accuracy difference is that in vLLM, the multiplications and divisions are not exactly the same as in transformers, which results in higher accuracy with transformers. Is it possible to work on improving the accuracy of embedding models? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nt ### 🐛 Describe the bug I served the Qwen 4B embedding model with Docker using vllm/vllm-openai:v0.10.1. I also designed a test to evaluate the strength of the embeddings. On that dataset, I reached an accuracy of 0.3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: /models/Qwen3-Embedding-4B/model \ --gpu-memory-utilization 0.16 \ --dtype bfloat16 \ --max-num-seqs 32 \ --max-model-len 12384 \ --served-model-name Qwen3-Embedding-4B ``` The reason for this accuracy difference is tha...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Accuracy Discrepancy in Qwen 4B Embeddings: vLLM vs. Transformers bug;stale ### Your current environment ### 🐛 Describe the bug I served the Qwen 4B embedding model with Docker using vllm/vllm-openai:v0.10.1. I a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ls? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Accuracy Discrepancy in Qwen 4B Embeddings: vLLM vs. Transformers bug;stale ### Your current environment ### 🐛 Describe the bug I served the Qwen 4B embedding model with Docker using vllm/vllm-openai:v0.10.1. I a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
