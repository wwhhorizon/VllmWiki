# vllm-project/vllm#16978: [Bug]: unable automatically set CUDA_VISIBLE_DEVICES correctly for v0 engine data parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#16978](https://github.com/vllm-project/vllm/issues/16978) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: unable automatically set CUDA_VISIBLE_DEVICES correctly for v0 engine data parallel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am testing data parallelism using the latest version of vLLM with the `data_parallel.py` example script (`https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/data_parallel.py`). My setup includes: - **dp-size=2**, **tp-size=2**, **enable_expert_parallel=False** (other parameters are default). - Single node with **4x H20 GPUs**. When using the **v1 engine** (`VLLM_USE_V1=1`), vLLM works as expected without issues. However, when switching to the **v0 engine** (`export VLLM_USE_V1=0`), I encounter the following error: #### Error output with `export VLLM_LOGGING_LEVEL=DEBUG`: ``` DEBUG 04-22 18:36:47 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 04-22 18:36:47 [__init__.py:34] Checking if TPU platform is available. DEBUG 04-22 18:36:47 [__init__.py:44] TPU platform is not available because: No module named 'libtpu' DEBUG 04-22 18:36:47 [__init__.py:101] Checking if ROCm platform is available. DEBUG 04-22 18:36:47 [__init__.py:115] ROCm platform is not available because: No module named 'amdsmi' DEBUG 04-22 18:36:47 [__init__.py:123] Checking if HPU platform is available. DEBUG 04-22...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: cally set CUDA_VISIBLE_DEVICES correctly for v0 engine data parallel bug;stale ### Your current environment ### 🐛 Describe the bug I am testing data parallelism using the latest version of vLLM with the `data_parallel.p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### 🐛 Describe the bug I am testing data parallelism using the latest version of vLLM with the `data_parallel.py` example script (`https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/data_parallel....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: unable automatically set CUDA_VISIBLE_DEVICES correctly for v0 engine data parallel bug;stale ### Your current environment ### 🐛 Describe the bug I am testing data parallelism using the latest version of vLLM wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
