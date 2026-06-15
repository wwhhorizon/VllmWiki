# vllm-project/vllm#24327: [Bug]: vLLM engine v1 with Qwen/Qwen3-Reranker-0.6B crashes with long input

| 字段 | 值 |
| --- | --- |
| Issue | [#24327](https://github.com/vllm-project/vllm/issues/24327) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM engine v1 with Qwen/Qwen3-Reranker-0.6B crashes with long input

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The vLLM server crashes when processing reranking requests with long documents using the default V1 engine, but works correctly with the V0 engine. vLLM Version: 0.10.1.1 Model: Qwen/Qwen3-Reranker-0.6B Task: score (reranking) Platform: CUDA Python Version: 3.11.13 GPU: A100 Steps to Reproduce 1. Start vLLM server with V1 engine (default): `vllm serve Qwen/Qwen3-Reranker-0.6B --task score --port 8080` 2. Send reranking request with long documents: 5 documents ~3,000 characters each Expected Behavior: The server should process the reranking request successfully and return relevance scores. Actual Behavior: The vLLM server crashes when processing the request. Workaround: Using the V0 engine resolves the issue `VLLM_USE_V1=0 vllm serve Qwen/Qwen3-Reranker-0.6B --task score --port 8080` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ing the default V1 engine, but works correctly with the V0 engine. vLLM Version: 0.10.1.1 Model: Qwen/Qwen3-Reranker-0.6B Task: score (reranking) Platform: CUDA Python Version: 3.11.13 GPU: A100 Steps to Reproduce 1. St...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: vLLM engine v1 with Qwen/Qwen3-Reranker-0.6B crashes with long input bug;stale ### Your current environment ### 🐛 Describe the bug The vLLM server crashes when processing reranking requests with long documents using the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 10.1.1 Model: Qwen/Qwen3-Reranker-0.6B Task: score (reranking) Platform: CUDA Python Version: 3.11.13 GPU: A100 Steps to Reproduce 1. Start vLLM server with V1 engine (default): `vllm serve Qwen/Qwen3-Reranker-0.6B --ta...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vLLM engine v1 with Qwen/Qwen3-Reranker-0.6B crashes with long input bug;stale ### Your current environment ### 🐛 Describe the bug The vLLM server crashes when processing reranking requests with long documents us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
