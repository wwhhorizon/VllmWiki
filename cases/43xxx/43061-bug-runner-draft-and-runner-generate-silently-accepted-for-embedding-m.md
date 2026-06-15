# vllm-project/vllm#43061: [Bug]: --runner draft and --runner generate silently accepted for embedding models but crash during weight loading with opaque ValueError

| 字段 | 值 |
| --- | --- |
| Issue | [#43061](https://github.com/vllm-project/vllm/issues/43061) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --runner draft and --runner generate silently accepted for embedding models but crash during weight loading with opaque ValueError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving an embedding model (`Qwen3-Embedding-8B`) with `--runner draft` or `--runner generate`, the CLI and config validation both accept the combination without complaint, but the server crashes during weight loading with an opaque `ValueError` about a missing module named `layers`. The real cause — that these runner modes are incompatible with embedding model architectures — is never surfaced to the user. The crash occurs early in model loading (before any weights are transferred to GPU), but the error message gives no indication that the problem is a runner/architecture mismatch. A user seeing this error would have no way to understand what went wrong or how to fix it. ## Steps to Reproduce **Case 1: `--runner draft`** ```bash vllm serve \ --host 127.0.0.1 \ --port 18115 \ --runner draft ``` **Case 2: `--runner generate`** ```bash vllm serve \ --host 127.0.0.1 \ --port 18116 \ --runner generate ``` Both commands are accepted by the CLI and pass argument validation, but the server exits before becoming healthy. ## Expected Behavior One of the following should happen: 1. vLLM detects at config validation time that `--runner...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: atible with embedding model architectures and exits with a clear, user-facing error such as `--runner draft/generate is only supported for causal LM models and cannot be used with embedding models`, or 2. The combinatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: g]: --runner draft and --runner generate silently accepted for embedding models but crash during weight loading with opaque ValueError bug ### Your current environment ### 🐛 Describe the bug When serving an embedding mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: --runner draft and --runner generate silently accepted for embedding models but crash during weight loading with opaque ValueError bug ### Your current environment ### 🐛 Describe the bug When serving an embedding...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
