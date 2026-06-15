# vllm-project/vllm#19189: [Bug]: LLM Engine Failure when fp8 kv cache enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#19189](https://github.com/vllm-project/vllm/issues/19189) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLM Engine Failure when fp8 kv cache enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When testing with kv_cache_dtype = 'fp8' with V1 (default) using `vllm/vllm-openai:v0.9.0.1` and `vllm/vllm-openai:v0.8.5.post1` image from https://hub.docker.com/r/vllm/vllm-openai/tags, run into vllm engine failure (debugging_level log with `export VLLM_LOGGING_LEVEL=DEBUG`) ``` DEBUG 06-04 16:44:21 [arg_utils.py:1616] Setting max_num_batched_tokens to 16384 for LLM_CLASS usage context. INFO 06-04 16:44:21 [config.py:1403] Using fp8 data type to store kv cache. It reduces the GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a proper scaling factor INFO 06-04 16:44:21 [config.py:1770] Defaulting to use mp for distributed inference INFO 06-04 16:44:21 [config.py:2003] Chunked prefill is enabled with max_num_batched_tokens=16384. WARNING 06-04 16:44:21 [fp8.py:63] Detected fp8 checkpoint. Please note that the format is experimental and subject to change. DEBUG 06-04 16:44:21 [llm_engine.py:134] Enabling multiprocessing for LLMEngine. Traceback (most recent call last): File " ", line 1, in File "/usr/lib/python3.12/multiprocessing/spawn.py", line 122, in spawn_main exitcode = _main(fd,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nai:v0.9.0.1` and `vllm/vllm-openai:v0.8.5.post1` image from https://hub.docker.com/r/vllm/vllm-openai/tags, run into vllm engine failure (debugging_level log with `export VLLM_LOGGING_LEVEL=DEBUG`) ``` DEBUG 06-04 16:4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: atched_tokens to 16384 for LLM_CLASS usage context. INFO 06-04 16:44:21 [config.py:1403] Using fp8 data type to store kv cache. It reduces the GPU memory footprint and boosts the performance. Meanwhile, it may cause acc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: LLM Engine Failure when fp8 kv cache enabled bug ### Your current environment ### 🐛 Describe the bug When testing with kv_cache_dtype = 'fp8' with V1 (default) using `vllm/vllm-openai:v0.9.0.1` and `vllm/vllm-ope...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: p for distributed inference INFO 06-04 16:44:21 [config.py:2003] Chunked prefill is enabled with max_num_batched_tokens=16384. WARNING 06-04 16:44:21 [fp8.py:63] Detected fp8 checkpoint. Please note that the format is e...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a proper scaling factor INFO 06-04 16:44:21 [config.py:1770] Defaulting to use mp for distributed inference INFO 06-04 16:44...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
