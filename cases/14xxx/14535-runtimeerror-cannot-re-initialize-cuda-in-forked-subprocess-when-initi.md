# vllm-project/vllm#14535: `RuntimeError: Cannot re-initialize CUDA in forked subprocess` when initializing vLLM with tensor parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#14535](https://github.com/vllm-project/vllm/issues/14535) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> `RuntimeError: Cannot re-initialize CUDA in forked subprocess` when initializing vLLM with tensor parallelism

### Issue 正文摘录

### Description When attempting to initialize a vLLM instance with a custom model and tensor parallelism, I encounter a `RuntimeError: Cannot re-initialize CUDA in forked subprocess` error across multiple worker processes. The error suggests that CUDA cannot be re-initialized in a forked subprocess and recommends using the `'spawn'` start method for multiprocessing. This issue prevents the model from loading successfully. The error occurs consistently when running the provided code snippet on a system with CUDA-enabled GPUs and tensor parallelism set to 8. ### Steps to Reproduce 1. Install the dependencies as listed in the [environment](#environment) section. 2. Run the following Python code: ```python import vllm model_name = '/QwQ-32B/' llm = vllm.LLM(model_name, tensor_parallel_size=8) ``` 3. Observe the error output in the logs. ### Expected Behavior The vLLM instance should initialize successfully, with all worker processes starting and the model loading without errors. ### Actual Behavior The initialization fails with the following error across multiple worker processes: ``` RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: enabled GPUs and tensor parallelism set to 8. ### Steps to Reproduce 1. Install the dependencies as listed in the [environment](#environment) section. 2. Run the following Python code: ```python import vllm model_name =...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: distributed inference WARNING 03-10 11:30:28 arg_utils.py:1187] Chunked prefill is enabled by default for models with max_model_len > 32K. Currently, chunked prefill might not work with some features or models. If you e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, disable_custom_al...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_ti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Description When attempting to initialize a vLLM instance with a custom model and tensor parallelism, I encounter a `RuntimeError: Cannot re-initialize CUDA in forked subprocess` error across multiple worker processes....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
