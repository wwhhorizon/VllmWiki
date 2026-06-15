# vllm-project/vllm#20670: [Bug]: Tensor dimension mismatch when loading Qwen3-Reranker-4B with tensor parallel > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#20670](https://github.com/vllm-project/vllm/issues/20670) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tensor dimension mismatch when loading Qwen3-Reranker-4B with tensor parallel > 1

### Issue 正文摘录

### 🐛 Describe the bug When trying to load the Qwen3-Reranker-4B model with tensor parallelism enabled (tensor_parallel_size=2), the model initialization fails due to a tensor dimension mismatch error. ## Environment - vLLM version: 0.9.2 - Model: Qwen/Qwen3-Reranker-4B - GPU configuration: 2 GPUs with tensor parallelism - CUDA version: 12.9 ## Steps to reproduce 1. Run vLLM with the following configuration: ```bash --model Qwen/Qwen3-Reranker-4B --task score --enforce_eager True --served_model_name Qwen/Qwen3-Reranker-4B-30k --hf_overrides '{"architectures":["Qwen3ForSequenceClassification"],"classifier_from_token":["no","yes"],"is_original_qwen3_reranker":true}' --tensor_parallel_size 2 --gpu_memory_utilization 0.97 ``` ## Expected behavior The model should load successfully with tensor parallelism across 2 GPUs. ## Actual behavior The model fails to load with the following error: ``` RuntimeError: The size of tensor a (1280) must match the size of tensor b (2560) at non-singleton dimension 1 ``` Full stack trace shows the error occurs in the `load_weights_using_from_2_way_softmax` function when attempting to copy weights to the score layer: ``` File "/usr/local/lib/python3.12/d...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: fails due to a tensor dimension mismatch error. ## Environment - vLLM version: 0.9.2 - Model: Qwen/Qwen3-Reranker-4B - GPU configuration: 2 GPUs with tensor parallelism - CUDA version: 12.9 ## Steps to reproduce 1. Run...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Tensor dimension mismatch when loading Qwen3-Reranker-4B with tensor parallel > 1 bug ### 🐛 Describe the bug When trying to load the Qwen3-Reranker-4B model with tensor parallelism enabled (tensor_parallel_size=2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: el len 40960 INFO 07-09 00:57:09 [arg_utils.py:1596] (Disabling) chunked prefill by default INFO 07-09 00:57:09 [arg_utils.py:1599] (Disabling) prefix caching by default WARNING 07-09 00:57:09 [cuda.py:102] To see benef...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
